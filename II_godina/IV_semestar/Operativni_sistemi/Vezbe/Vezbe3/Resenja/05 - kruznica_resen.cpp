/* Napraviti konkurentni program koji određuje najbližu tačku kružnici (iz
 * velikog vektora tačaka - npr 100000000 elemenata).
 *
 * Program realizovati uz pomoć 2 klase:
 *
 * 1) Klasa Closest_point modelira najbližu tačku kružnici.
 * Interfejs klase sadrži sledeće metode:
 *
 * class Closest_point {
 *     void test_and_set(const Point& p, double d);
 *     friend ostream& operator<<(ostream& os, Closest_point& cp);
 * };
 *
 * Metoda test and set treba da proveri da li je prosleđena tačka p bliža od
 * trenutno najbliže tačke i da ako jeste postavi parametre nove najbliže tačke.
 * Operator služi za ispis koordinata najbliže tačke na ekran.
 *
 * 2) Klasa Circle modeluje kruznicu.
 * Interfejs klase sadrži sledeće metode:
 *
 * class Circle {
 *    double circle(const Point& t);
 *    void find_closest(VPci p_begin, VPci p_end, Closest_point& cpoint);
 * };
 *
 * pri cemu je VPci je definisan kao
 *
 * typedef vector<Point>::const_iterator VPci;
 *
 * Metoda circle_distance treba da izračuna udaljenost tačke od kružnice.
 * Operator služi za prolazak kroz vektor tačaka i poređenje pojedinačnih tačaka
 * vektora sa trenutno najbližom tačkom (globalnom tačkom). Dato poređenje se
 * realizuje pozivanjem metode test_and_set na objektu najbliže tačke (cpoint).
 *
 * Kreirati jedan globalni objekat najbliže tačke.
 *
 * Kreirati 3 niti, pri cemu tela niti predstavlja data funkcija f
 *
 * void f(Circle& c, VPci p_begin, VPci p_end, Closest_point& cpoint) {
 *     c.find_closest(p_begin, p_end, cpoint);
 * }
 *
 * Svakoj niti se prosledjuje referenca na kruznicu koja se posmatra,1/3 vektora
 * tačaka kao i referenca na globalni objekat najbliže tačke. Nakon završetka
 * niti ispisati koodrdinate najbliže tačke.
 *
 * Napomena: konstruktore klasa Closest_point i Circle realizovati samostalno.
 * Kreirati veliki vektor tačaka (npr. 10000 elemenata) sa slučajnim vrednostima
 * koordinata tačaka (ne predalekim od kružnice).
 */
#include <cmath>
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>

using namespace std;

struct Point {
  double x, y;
};

class Closest_point {
  bool empty;
  Point p0;    // Point's coordinates
  double dist; // Distance
  mutex m;

public:
  Closest_point() : empty(true) {}
  void test_and_set(const Point &p, double d) {
    unique_lock<mutex> lock(m);
    if (!empty) {
      if (!(d < dist))
        return;
    }
    p0.x = p.x;
    p0.y = p.y;
    dist = d;
    empty = false;
  }
  friend ostream &operator<<(ostream &os, Closest_point &cp) {
    unique_lock<mutex> lock(cp.m);
    os << "(" << cp.p0.x << "," << cp.p0.y << ")" << endl;
    return os;
  }
};

typedef vector<Point>::const_iterator VPci;

class Circle {
  Point p0;
  double r;

public:
  Circle(const Point &t, const double r_) : p0(t), r(r_) {}
  double circle_distance(const Point &t) {
    return abs(sqrt(pow(p0.x - t.x, 2) + pow(p0.y - t.y, 2)) - r);
  }
  void find_closest(VPci p_begin, VPci p_end, Closest_point &cpoint) {
    for (; p_begin != p_end; ++p_begin) {
      cpoint.test_and_set(*p_begin, circle_distance(*p_begin));
    }
  }
};

void f(Circle &c, VPci p_begin, VPci p_end, Closest_point &cpoint) {
  c.find_closest(p_begin, p_end, cpoint);
}

int main() {
  double x_center = 0, y_center = 0, radius = 3;
  double random_x, random_y;
  Circle k({x_center, y_center}, radius);
  vector<Point> p(10000);
  srand(time(NULL));

  for (int i = 0; i < 10000; i++) {
    random_x = rand() % (2 * (int)radius) + radius / 2; // distance x close to the circle center
    random_y = rand() % (2 * (int)radius) + radius / 2; // distance y close to the circle center
    p[i] = {random_x, random_y};
    ;
  }

  Closest_point cp;
  Closest_point cp1;

  thread t1(f, ref(k), p.begin(), p.begin() + p.size() / 3, ref(cp));
  thread t2(f, ref(k), p.begin() + p.size() / 3, p.begin() + p.size() / 3 * 2, ref(cp));
  thread t3(f, ref(k), p.begin() + p.size() / 3 * 2, p.end(), ref(cp));
  thread t4(f, ref(k), p.begin(), p.end(), ref(cp1));
  t1.join();
  t2.join();
  t3.join();
  t4.join();

  cout << cp;
  cout << cp1;

  return 0;
}
