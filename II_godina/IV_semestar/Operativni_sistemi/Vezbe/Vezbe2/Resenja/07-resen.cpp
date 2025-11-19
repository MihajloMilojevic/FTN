/* Napraviti program za evidenciju identifikatora niti. U programu definisati
 * STL kontejner sa 5 elemenata (isto toliko ce biti i niti). Elementi
 * kontejnera su objekti koji predstavljaju identifikatore niti. Svaka nit treba
 * u dati STL kontejner da upise svoj identifikator i to u odgovarajuci element.
 *
 * Dakle, prva nit upisuje svoj identifikator u prvi element vektora, druga nit
 * u drugi element i tako redom. Kada se sve niti zavrse, potrebno je ispisati
 * identifikatore uskladistene u STL kontejneru.
 */
#include <iostream>
#include <thread>
#include <vector>

using namespace std;

const int N = 5;

void f(vector<thread::id>::iterator it) { // Funkcija niti. Postavlja id niti u jedan od elemenata vektora.
  *it = this_thread::get_id();
}

int main() {
  vector<thread::id> identifikatori;
  identifikatori.resize(N); // resize daje duzinu N vektoru indektifikatori (vrednost elemenata je nebitna).
  thread niti[N];

  for (int i = 0; i < N; i++)
    niti[i] = thread(f, identifikatori.begin() + i); // Svaka nit uzima jedan pokazivac na element vektora.

  for (int i = 0; i < N; i++)
    niti[i].join();

  for (vector<thread::id>::const_iterator it = identifikatori.begin(); // Prodji kroz sve elemente vektora i ispisi
       it != identifikatori.end(); it++)                               // ih. Tj. ispisi identifikatore.
    cout << *it << endl;

  return 0;
}
