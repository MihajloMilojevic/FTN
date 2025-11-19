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
#include <iostream>
#include <mutex>
#include <random>
#include <thread>

#define UKUPNO_RACUNA 3

using namespace std;

mutex m; // propusnica za sprecavanje stetnog preplitanja pri prenosu novca sa jednog racuna na drugi

struct retVal {
  double staro; // iznos novca na racunu pre prenosa
  double novo;  // iznos novca na racunu posle prenosa
};

double racuni[UKUPNO_RACUNA]; // svaki elemenat niza predstavlja iznos novca na odgovarajucem racunu

retVal prebaci(int izvor, int cilj, double iznos) { // prebacivanje "iznos" kolicine novca sa racuna "izvor" na racun "cilj"
  retVal r;
  // zakljucavamo propusnicu da ne bi druga nit krenula da radi transfer novca sa istog racuna, pre nego sto je zavrsena kompletna transakcija
  unique_lock<mutex> l(m);
  r.staro = racuni[izvor];                    // trenutni iznos na prvom racunu
  racuni[izvor] -= iznos;                     // umanjimo iznos na prvom racunu
  this_thread::sleep_for(chrono::seconds(1)); // simuliranje trajanja prenosa
  racuni[cilj] += iznos;                      // dodamo iznos na drugi racun
  r.novo = racuni[izvor];                     // novo stanje na prvom racunu
  return r;
}

void transfer() {
  random_device rd;
  uniform_int_distribution<int> izvori(0, UKUPNO_RACUNA - 1), pare(1, 10);
  // deset transakcija se vrsi
  for (int i = 0; i < 10; i++) {
    int izvor = izvori(rd);                 // slucajno izaberemo prvi racun
    int cilj = (izvor + 5) % UKUPNO_RACUNA; // slucajno izaberemo drugi racun
    int iznos = pare(rd);                   // slucajno izaberemo iznos
    retVal r = prebaci(izvor, cilj, iznos); // prebacimo novac sa jednog racuna na drugi
    // razlika izmedju novog i starog iznosa na racunu mora biti jednaka iznosu koji se prebacivao.
    // Ukoliko to nije slucaj, znaci da program ne radi ispravno
    if ((r.staro - r.novo) != iznos)
      cout << "Greska!!! Prebaceno " << iznos << " sa racuna " << izvor << " na racun " // ova poruka se ne sme ispisati ako program radi ispravno
           << cilj << ". Na izvoru bilo " << r.staro << ", a ostalo " << r.novo << endl;
  }
}

// funkcija za racunanje ukupnog iznosa na svim racunima
double ukupno_u_banci() {
  double ukupno = 0;
  for (int i = 0; i < UKUPNO_RACUNA; i++) {
    ukupno += racuni[i];
  }
  return ukupno;
}

int main() {
  double ukupno = 0;
  // inicijalizujemo iznos na svakom racunu
  for (int i = 0; i < UKUPNO_RACUNA; i++) {
    racuni[i] = 10;
  }
  cout << "Inicijalno u banci: " << ukupno_u_banci() << endl; // ukupno novca u banci pre transakcija

  // napravimo 2 niti koje ce vrsiti transfere
  thread t1(transfer);
  thread t2(transfer);

  t1.join();
  t2.join();

  cout << "Na kraju ukupno u banci: " << ukupno_u_banci() << endl; // ukupno novca nakon transakcija

  return 0;
}
