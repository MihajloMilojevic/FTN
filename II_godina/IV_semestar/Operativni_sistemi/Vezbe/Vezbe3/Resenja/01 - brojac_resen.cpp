/* Napraviti konkurentni program koji sadrzi main funkciju i 2 niti. Obe niti
 * pristupaju istoj celobrojnoj promenljivoj brojac, koja inicijalno ima
 * vrednost 0.
 * Prva nit 1000000 puta uvecava vrednost brojaca.
 * Druga nit isti broj puta smanjuje vrednost brojaca.
 *
 * Ukoliko je program ispravno napisan, na kraju programa vrednost brojaca mora
 * biti 0.
 */
#include <iostream>
#include <mutex>
#include <thread>

using namespace std;

const int ITERATIONS = 1000000;

int brojac = 0; // brojac je globalna promenljiva da bi obe niti menjale isti brojac

mutex m; // globalna propusnica za sprecavanje stetnog preplitanja pri pristupu brojacu

void inkrement() {
  for (int i = 0; i < ITERATIONS; ++i) {
    m.lock(); // zakljuca se propusnica pre pristupa deljenoj promenljivoj
    ++brojac;
    m.unlock();
  }
}

void dekrement() {
  for (int i = 0; i < ITERATIONS; ++i) {
    m.lock(); // zakljuca se propusnica pre pristupa deljenoj promenljivoj
    --brojac;
    m.unlock();
  }
}

int main() {
  thread t1(inkrement);
  thread t2(dekrement);

  t1.join();
  t2.join();

  cout << brojac << endl;

  return 0;
}
