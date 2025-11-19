/* Napraviti konkurentni program sa 2 niti koje imaju isto telo niti. Svaka nit
 * najpre trazi od korisnika da unese svoju visinu. Nakon unosa, nit ispisuje
 * unetu vrednost na terminal.
 *
 * Sinhronizovati pristup terminalu kao deljenom resursu. Kada jedna nit stupi u
 * interakciju sa korisnikom, ne sme biti prekinuta dok se ne zavrsi kompletna
 * interakcija (i unos i ispis).
 */
#include <iostream>
#include <mutex>
#include <thread>

using namespace std;

mutex m; // propusnica za pristup deljenom resursu (u ovom slucaju to je terminal). Posto je globalna promenljiva, obe niti koriste istu propusnicu

void visina() {
  int v;
  // trazimo propusnicu za pristup terminalu
  // u praksi se izbegava ovaj nacin zakljucavanja, jer propusnica moze ostati zakljucana. Programer mora da vodi racuna da otkljuca propusnicu u svakom scenariju izvrsavanja
  m.lock();
  cout << "Koliko ste visoki [cm]?" << endl;
  cin >> v;
  cout << "Vasa visina je " << v << " cm." << endl;
  cout << endl;
  m.unlock(); // otkljucavanje propusnice da bi naredna nit mogla da pristupi terminalu
}

int main() {
  thread t1(visina);
  thread t2(visina);

  t1.join();
  t2.join();

  return 0;
}
