/* Napraviti konkurentni program koji pita korisnika koliko niti da stvori, a
 * zatim stvara zadati broj niti. Pri instanciranju nit dobija redni broj pod
 * kojim je stvorena. Svaka nit ispisuje svoj redni broj i svoj identifikator.
 */
#include <iostream>
#include <thread>

using namespace std;

void f(int rBr) {                                                                                   // Funkcija od koje nastaju niti.
  cout << "Moj redni broj je: " << rBr << " a identifikator je: " << this_thread::get_id() << endl; // Funkcija ispisuje redni broj niti kao i njen identifikator.
}

int main() {
  int n;
  cout << "Unesite broj niti: ";
  cin >> n;
  thread *niti = new thread[n]; // Kreiranje dinamickog niza niti od n elemenata (zauzimanje memorije).

  for (int i = 0; i < n; ++i) {
    niti[i] = thread(f, i + 1); // Kreiranje niti od funkcije f. Svaka nit dobija svoj redni broj.
  }

  for (int i = 0; i < n; ++i) {
    niti[i].join(); // main ceka da se sve niti zavrse.
  }

  delete[] niti; // Oslobadjanje memorije zauzete za dinamicki niz niti.

  return 0;
}
