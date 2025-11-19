/* Sabrati korespodentne elemente vektora a i b, a zbirove smestiti na
 * odgovarajuce pozicije vektora c. Obezbediti da svako sabiranje obavlja
 * posebna nit.
 */
#include <iostream>
#include <thread>
#include <vector>

using namespace std;

double f(double a, double b, double *c) { // Funkcija za sabiranje 2 broja.
  *c = a + b;
}

int main() {
  vector<double> a = {1, 2, 3, 4, 5, 6, 7, 8}; // Vektor a.
  vector<double> b = {2, 1, 3, 4, 5, 2, 8, 2}; // Vektor b.
  int size = a.size();
  vector<double> c(size); // Kreiranje vektora c iste duzine kao vektori a i b.
  thread niti[size];      // Deklaracija onoliko niti koliko ima elemenata u vektorima a i b.

  for (int i = 0; i < size; ++i) {
    niti[i] = thread(f, a[i], b[i], &c[i]); // Kreiranje niti. Svaka nit izvrsava funkciju f, u okviru koje se sabiraju respektivni elementi vektora a i b i smestaju u odgovarajuci element vektora c.
  }

  for (int i = 0; i < size; ++i) {
    niti[i].join(); // Main ceka da se sve niti zavrse.
  }

  cout << "Vektor c je : ";
  for (int i = 0; i < size; ++i) {
    cout << c[i] << " "; // Ispis elemenata vektora c.
  }

  return 0;
}
