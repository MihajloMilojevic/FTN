/* Napraviti konkurentni program sa tri niti.
 * Nit a ispisuje: "Ja sam nit a."
 * Nit b ispisuje: "Ja sam nit b."
 * Nit c ispisuje: "Ja sam nit c."
 * Obezbediti da se niti a i b, uvek izvrse pre niti c.
 */
#include <iostream>
#include <thread>

using namespace std;

class koordinator {
  const int cekam_niti; // Konstanta koja govori koliko niti se ceka na zavrsetak pre nego sto se aktivira poslednja.
  int zavrseno_niti;    // Brojac koji govori koliko je niti zavrseno. Uporedjuje se sa konstantom cekam_niti.
  mutex m;              // Mutex i uslovna promenljiva. Neophodni UVEK za eksplicitnu sinhronizaciju izmedju niti.
  condition_variable c;

public:
  koordinator(int cn) : cekam_niti(cn), zavrseno_niti(0) {} // Konstruktor. Ceka se niti koliko se prosledi.

  void zavrsio() { // Funkcija koju na svom KRAJU zovu niti (a i b) koje ne cekaju (izvrsavaju se odmah).
    unique_lock<mutex> lock(m);
    if (++zavrseno_niti == cekam_niti) // Provera brojaca. Ukoliko je zavrseno niti == cekam_niti, obavestavaju se sve niti (c)
      c.notify_all();                  // koje cekaju da se prethodne niti (a i b) zavrse. Ovo se naziva i barijera.
  }

  void cekam() { // Funkcija koju na svom POCETKU zovu niti (c) koje cekaju (ne izvrsavaju se odmah).
    unique_lock<mutex> lock(m);
    while (!(zavrseno_niti == cekam_niti)) // Provera brojaca. Ukoliko zavrseno_niti != cekam_niti, nit pozivaoc (c) ulazi
      c.wait(lock);                        // u cekanje ispunjenosti uslova. Mora WHILE. Jos jedan tip uslova osim enumeracije
  }                                        // jeste brojac (kao ovde). Takodje moguci su i bool uslovi.
};

mutex term_mx;           // Globalni mutex terminala da bi se sprecila stetna preplitanja na terminalu.
void a(koordinator &k) { // Nit a. Prosledjuje se referenca na koordinator, kako bi sve niti radile na istom k.
  {
    unique_lock<mutex> lock(term_mx);
    cout << "Ja sam nit a." << endl;
  }
  k.zavrsio();
}

void b(koordinator &k) { // Nit b. Prosledjuje se referenca na koordinator, kako bi sve niti radile na istom k.
  {
    unique_lock<mutex> lock(term_mx);
    cout << "Ja sam nit b." << endl;
  }
  k.zavrsio();
}

void c(koordinator &k) { // Nit c. Prosledjuje se referenca na koordinator, kako bi sve niti radile na istom k.
  k.cekam();
  unique_lock<mutex> lock(term_mx);
  cout << "Ja sam nit c." << endl;
}

int main() {
  koordinator k{2}; // Kreiranje objekta koordinatora koji se prosledjuje nitima po referenci.

  thread ta(a, ref(k));
  thread tb(b, ref(k));
  thread tc(c, ref(k));

  ta.join();
  tb.join();
  tc.join();

  return 0;
}
