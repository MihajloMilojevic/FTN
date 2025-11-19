/* Napraviti program koji simulira prenos novca sa jednog bankovnog racuna na
 * drugi. Iznosi na racunima su predstavljeni datim nizom racuni.
 *
 * Data funkcija transfer() predstavlja telo niti koje vrse prenos novca.
 * Funkcija 10 puta na slucajan nacin bira dva racuna i neki iznos novca i
 * poziva funkciju prebaci() koja skida novac sa prvog racuna i dodaje ga na
 * drugi racun.
 * U funkciji prebaci(), nakon skidanja novca sa prvog racuna potrebno je jedna
 * sekunda da se novac uplati na drugi racun. Povratna vrednost funkcije prebaci
 * je struktura retVal koja sadrzi iznos na prvom racunu pre i posle
 * transakcije.
 *
 * U glavnom programu potrebno je kreirati dve niti koje izvrsavaju funkciju
 * transfer(). Ispisati ukupnu kolicinu novca na svim racunima u banci pre i
 * posle transakcija.
 */
#include <random>

#define UKUPNO_RACUNA 3

using namespace std;

struct retVal {
    double staro;
    double novo;
};

double racuni[UKUPNO_RACUNA];


retVal prebaci(int izvor, int cilj, double iznos);


void transfer() {
    random_device rd;
    uniform_int_distribution<int> izvori(0, UKUPNO_RACUNA - 1), pare(1, 10);
    for (int i = 0; i < 10; i++) {
        int izvor = izvori(rd);
        int cilj = (izvor + 5) % UKUPNO_RACUNA;
        int iznos = pare(rd);
        retVal r = prebaci(izvor, cilj, iznos);
        //ako je program ispravan, mora da se izvornog racuna skine tacno onoliko koliko je iznos
        if ((r.staro - r.novo) != iznos)
            cout << "Greska!!! Prebaceno " << iznos << " sa racuna " << izvor << " na racun "
            << cilj << ". Na izvoru bilo " << r.staro << ", a ostalo " << r.novo << endl;
    }
}