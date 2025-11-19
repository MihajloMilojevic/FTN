/* Napraviti konkrentni program koji izračunava sumu svih elemenata vektora,
 * koristeći funkciju f():
 *
 * f(ci begin, ci end, double& zbir);
 *
 * pri cemu je ci definisano kao
 *
 * typedef vector<double>::const_iterator ci;
 *
 * Podeliti racunanje sume na 2 dela tako da prvu polovinu vektora sumira prva
 * nit, a drugu polovinu druga nit.
 *
 * Napomena: ovakva optimizacija sumiranja je znacajna kada se radi na
 * dvojezgarnom procesoru za vektore velike duzine.
 */
#include <iostream>
#include <thread>
#include <vector>

using namespace std;

typedef vector<double>::const_iterator ci; // Pogledati resenje suma_vektora_sekvencijalno.cpp za objasnjenje const_iteratora i funkcije f.

void f(ci begin, ci end, double &zbir) {
  zbir = 0;
  for (; begin != end; ++begin)
    zbir += *begin;
}

int main() {
  vector<double> v = {1, 2, 3, 4, 5, 6, 7, 8, 9};
  double zbir1, zbir2;

  ci polovina = v.begin() + v.size() / 2; // Odredjivanje iteratora (pokazivaca) na sredinu vektora. Sredina se nalazi na v.begin() + polovina duzine vektora.

  thread t1(f, v.begin(), polovina, ref(zbir1)); // Stvaranje i pokretanje niti t1. Nit t1 sabira prvu polovinu vektora, tj. od iteratora v.begin() do iteratora polovina.
  thread t2(f, polovina, v.end(), ref(zbir2));   // Stvaranje i pokretanje niti t2. Nit t2 sabira drugu polovinu vektora, tj. od iteratora polovina do iteratora v.end().
  t1.join();
  t2.join();

  cout << "zbir1=" << zbir1 << endl; // Ispis zbira moze da se izvrsi tek nakon zavrsetka obe niti! (nakon oba joina).
  cout << "zbir2=" << zbir2 << endl;
  cout << "ukupno=" << zbir1 + zbir2 << endl;

  return 0;
}
