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

class parking { 
  public:
	parking(int N);
	void udji();
	void izadji();
};

mutex m;
void automobil(parking& p) {
   p.udji();
   { unique_lock<mutex> l(m);
      cout << "Automobil " << this_thread::get_id() << " usao na parking." << endl;
   }
   this_thread::sleep_for(chrono::seconds(3));
   p.izadji();
   { unique_lock<mutex> l(m);
      cout << "Automobil " << this_thread::get_id() << " izasao sa parkinga." << endl;
   }
}