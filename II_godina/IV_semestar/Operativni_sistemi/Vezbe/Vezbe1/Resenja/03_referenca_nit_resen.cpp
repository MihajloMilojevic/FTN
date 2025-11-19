/* Napisati konkurentni program koji stvara jednu nit.
 * Nit od glavnog programa kao parametar dobija ceo broj i ima zadatak da uveca
 * vrednost broja za 1.
 *
 * Ispisati vrednost broja nakon zavrsetka rada niti
 *
 * Napomena: dodati ref(b) kao drugi parametar niti da bi program ispravno 
 * radio
 */
#include <iostream>
#include <thread>

using namespace std;

void increment(int &a) { // Funkcija niti (prima parametar po referenci)
  ++a;
}

int main() {
  int a = 0;
  int b = 0;

  increment(a); // Poziv funkcije increment (standardno prosledjivanje parametra po referenci).

  thread t(increment, b); // Stvaranje niti i pokretanje niti. Prosledjivanje parametra niti po referenci kao obicnoj funkciji (ne radi). Pogledati napomenu.
  t.join();

  cout << "a=" << a << endl; // Ispis vrednosti a (uspesno izmenjena).
  cout << "b=" << b << endl; // Ispis vrednosti b (ostala ista -> greska). Pogledati napomenu.

  return 0;
}
