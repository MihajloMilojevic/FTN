/*
Napraviti konkurentni program za transliranje 2D poligona u ravni za definisani pomeraj po x i y koordinati.
Poligon predstaviti kao skup tacaka definisan u STL kontejneru.

Na pocetku programa pitati korisnika da unese pomeraj za x koordinatu i y koordinatu.

Stvoriti 2 niti. Jedna nit treba da izvrsi translaciju svih x koordinata tacaka za definisani pomeraj, a druga nit
translaciju y koordinata.

Na kraju programa ispisati tacke transliranog poligona.

*/

#include <iostream>
#include <thread>
#include <vector>

using namespace std;

struct Point {
    int x;
    int y;
};

void f(vector<Point>& polygon, int translate, char coord) {
    for (vector<Point>::iterator it = polygon.begin(); it != polygon.end(); it++) {
        if (coord == 'x')
            it->x += translate;
        else
            it->y += translate;
    }
}

int main()
{
    int translate_x, translate_y;
    cout << "Unesite pomeraj za x, odnosno y koordinatu" << endl;
    cin >> translate_x >> translate_y;
    vector<Point> polygon = {Point{0,0}, Point{2,0}, Point{2,2}, Point{0,2}};
    //jedna nit translira x koordinate, druga nit y koordinate
    thread t1(f, ref(polygon), translate_x, 'x');
    thread t2(f, ref(polygon), translate_y, 'y');

    t1.join();
    t2.join();

    for (vector<Point>::iterator it = polygon.begin(); it != polygon.end(); it++)
        cout << "(" << it->x << "," << it->y << ")" << endl;
}


