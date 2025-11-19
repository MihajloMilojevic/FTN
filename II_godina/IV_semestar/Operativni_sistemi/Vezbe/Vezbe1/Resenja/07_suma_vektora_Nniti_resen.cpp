/* Napraviti konkrentni program koji izračunava sumu svih elemenata vektora,
 * koristeći funkciju f():
 *
 * f(ci begin, ci end, double& zbir);
 *
 * pri cemu je ci definisano kao
 *
 * typedef vector<double>::const_iterator ci;
 *
 * Podeliti racunanje sume na N delova tako svaka nit sabira duzina vektora/broj
 * niti elemenata vektora.
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

  cout << "Koliko niti da stvorim? "; // Korisnicki unos kolicine niti (proizvoljan). Ne unositi vise niti nego sto ima elemenata vektora.
  int n;
  cin >> n;
  double zbir[n];

  ci begin = v.begin();          // Iterator na pocetak vektora.
  ci end = begin + v.size() / n; // Iterator na kraj prvog dela vektora. Vektor se deli na N delova, pri cemu je kraj prvog dela na begin + v.size()/n.
  thread t[n];                   // Niz od N niti (objekata niti).

  for (int i = 0; i < n - 1; ++i) {
    t[i] = thread(f, begin, end, ref(zbir[i])); // Svaka nit uzima pocetak i kraj svog dela vektora (iteratore) kao i jedan od zbirova iz niza zbirova.
    begin = end;                                // Pocetak sledeceg dela vektora koji se obradjuje je kraj prethodnog dela.
    end += v.size() / n;                        // Kraj sledeceg dela vektora koji se obradjuje je kraj prethodnog dela + v.size()/n.
  }
  t[n - 1] = thread(f, begin, v.end(), ref(zbir[n - 1])); // Posebno izdvojen zadnji zbir (deo vektora). Ovo se radi iz razloga sto broj elemenata vektora ne mora biti deljiv
                                                          // sa brojem niti. Npr. 10/3, pa moramo da odvojimo i posebno obradimo zadnji deo vektora. U 10/3 verziji prve
                                                          // 2 niti bi obradjivale po 3 elementa vektora a zadnja nit 4.
  for (int i = 0; i < n; ++i) {
    t[i].join(); // Cekanje niti main da se sve niti niza niti t zavrse.
  }

  double z = 0;
  for (int i = 0; i < n; ++i) { // Ispis pojedinacnih zbirova svih niti i spajanje konacnog zbira.
    cout << "zbir[" << i << "]= " << zbir[i] << endl;
    z += zbir[i];
  }

  cout << "ukupno=" << z << endl;

  return 0;
}
