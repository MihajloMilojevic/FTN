/* Definisati klasu parking koja modeluje parking prostor kapaciteta N mesta.
 * Kapacitet parkinga proslediti kao argument konstruktoru, pri instanciranju
 * deljene promenljive.
 *
 * Klasa parking ima operacije:
 *
 *     void parking::udji();
 *     void parking::izadji();
 *
 * Automobili koji dolaze na parking su predstavljeni nitima. Za ulazak na
 * parking, automobil poziva metodu udji(). Za izlazak sa parkinga, automobil
 * poziva metodu izadji(). Automobil se na parkingu zadrzava 3 sekunde.
 *
 * Pri ulasku, ukoliko su sva parking mesta zauzeta, automobil mora da saceka da
 * se neko parking mesto oslobodi.
 */
#include <condition_variable>
#include <iostream>
#include <mutex>
#include <thread>

using namespace std;

class parking {
  int br_mesta;      // dovoljno je da koristimo prost brojac jer ne moramo da razlikujemo pojedinacna parking mesta
  mutex evidencija;  // deljena promenljiva je evidencija o broju slobodnih mesta na parkingu, tj. polje br_mesta, ciji pristup sinhronizujemo
  condition_variable kolona;

public:
  parking(int N) : br_mesta(N) {}
  void udji() {
    unique_lock<mutex> ev(evidencija);
    while (!br_mesta)
      kolona.wait(ev);

    br_mesta--;
  }
  void izadji() {
    unique_lock<mutex> ev(evidencija);
    br_mesta++;
    ev.unlock();  // minimizujemo kriticnu sekciju

    kolona.notify_one();
  }
};

mutex terminal;
void automobil(parking &p) {
  p.udji();
  {
    unique_lock<mutex> l(terminal);
    cout << "Automobil " << this_thread::get_id() << " usao na parking." << endl;
  }
  this_thread::sleep_for(chrono::seconds(3));
  p.izadji();
  {
    unique_lock<mutex> l(terminal);
    cout << "Automobil " << this_thread::get_id() << " izasao sa parkinga." << endl;
  }
}

const int br_automobila = 7;

int main() {
  parking ispred_zgrade(5);
  thread automobili[br_automobila];

  for (thread &autic : automobili)
    autic = thread(automobil, ref(ispred_zgrade));

  for (thread &autic : automobili)
    autic.join();

  return 0;
}