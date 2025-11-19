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
