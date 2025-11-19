/* Napraviti konkurentni program koji kreira 5 niti od kojih svaka izvrsava isti
 * kod (svaka nit ima isto telo niti).
 * Svaka nit dobija svoj redni broj prilikom kreiranja.
 * U telu niti svaka nit treba da ispise svoj redni broj.
 */
#include <iostream>
#include <thread>

using namespace std;

void f(int rbr) {
  cout << rbr;
}

const int BROJ_NITI = 7;

int main() {
  thread t[BROJ_NITI];

  for (int i = 0; i < BROJ_NITI; ++i)
    t[i] = thread(f, i);
  for (int i = 0; i < BROJ_NITI; ++i)
    t[i].join();

  cout << endl;

  return 0;
}
