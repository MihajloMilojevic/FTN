/* Napraviti konkurentni program koji modeluje klasu brojača.
 * Interfejs klase sadrži sledeće metode:
 *
 * class brojac {
 * public:
 *     void inc();
 *     void dec();
 *     friend ostream& operator<<(ostream& , brojac& );
 * };
 *
 * Metode inc i dec povećavaju, odnosno smanjuju vrednost brojača za 1. Operator
 * << služi za ispis brojača na ekran. Klasa mora biti thread-safe (da garantuje
 * ispravan rad i ako se objektu klase pristupa iz razlicitih niti).
 *
 * Kreirati jednu instancu date klase kojoj pristupaju 2 niti.
 *
 * Jedna nit poziva metodu uvećavanja brojača 1000000 puta, a druga metodu
 * smanjivanja brojača 1000000 puta.
 *
 * Na kraju programa ispisati konačnu vrednost brojača.
 */
#include <iostream>
#include <mutex>
#include <thread>

using namespace std;

const int ITERATIONS = 1000000;

// klasa u sebi sadrzi podatke i obezbedjuje thread-safe pristup ovim podacima
// dakle medjusobna iskljucivost je enkapsulirana u klasu, pozivalac operacija ne mora da vodi racuna o medjusobnoj iskljucivosti
class brojac {
  mutex m;  // propusnica pripada klasi i obezbedjuje sprecavanje stetnog preplitanja pri vrsenju operacija nad objektima klase
  int broj; // vrednost brojaca
public:
  brojac() : broj(0) {} // inicijalno je brojac nula
  void inc() {
    unique_lock<mutex> l(m);
    ++broj;
  } // operacija povecava brojac, ali pre toga zakljucava propusnicu i na taj nacin sprecava stetno preplitanja pri izmeni brojaca
  void dec() {
    unique_lock<mutex> l(m);
    --broj;
  }                                                    // operacija smanjuje brojac, ali pre toga zakljucava propusnicu i na taj nacin sprecava stetno preplitanja pri izmeni brojaca
  friend ostream &operator<<(ostream &os, brojac &b) { // preklopljen operator za ispis objekta klase brojac. Ispisuje se atribut "broj" iz objekta
    unique_lock<mutex> l(b.m);                         // pre pristupa broju, zakljucava se propusnica da bi se sprecilo stetno preplitanje
    os << b.broj << endl;
    return os;
  }
};

brojac br; // da bi obe niti menjale isti brojac, on je definisan kao globalna promenljiva

void inkrement() {
  // specificirani broj puta se zatrazi povecavanje brojaca. Pozivalac ne vodi racuna o stetnom preplitanju, to je odgovornost klase
  for (int i = 0; i < ITERATIONS; ++i)
    br.inc();
}

void dekrement() {
  for (int i = 0; i < ITERATIONS; ++i) // specificirani broj puta se zatrazi smanjivanje brojaca
    br.dec();
}

int main() {
  thread t1(inkrement);
  thread t2(dekrement);

  t1.join();
  t2.join();

  cout << br << endl; // moze ovako, posto je operator za ispis za klasu brojac preklopljen

  return 0;
}
