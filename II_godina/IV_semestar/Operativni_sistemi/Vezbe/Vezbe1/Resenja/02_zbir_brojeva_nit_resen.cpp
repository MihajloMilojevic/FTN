/* Napraviti program koji kreira jednu nit kojoj se prosledjuju dva cela broja
 * a i b. U okviru niti sabrati brojeve i ispisati njihov zbir
 */
#include <iostream>
#include <thread>

using namespace std;

void kod_niti(const int a, const int b) { // Funkcija niti. Funkcija sabira 2 broja.
  cout << "Zbir brojeva " << a << " i " << b
       << " je " << a + b << endl;
}

int main() {
  thread t(kod_niti, 5, 3); // Stvaranje niti t i pokretanje niti. Prosledjivanje parametara niti t se vrsi kao kod poziva obicne funkcije (a = 5, b = 3).
  t.join();                 // Poziv operacije join() na niti t. Nit main ceka da se nit t zavrsi.

  return 0;
}
