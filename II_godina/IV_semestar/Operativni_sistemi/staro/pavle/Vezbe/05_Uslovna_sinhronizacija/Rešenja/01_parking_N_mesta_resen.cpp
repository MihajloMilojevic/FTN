/*
    Definisati klasu parking koja modeluje parking prostor kapaciteta N mesta.
    Kapacitet parkinga proslediti kao argument konstruktoru, pri instanciranju deljene promenljive.
    
	Klasa parking ima operacije:
        void parking::udji(); 
        void parking::izadji();

	Automobili koji dolaze na parking su predstavljeni nitima.
	Za ulazak na parking, automobil poziva metodu udji().
	Za izlazak sa parkinga, automobil poziva metodu izadji().
	Automobil se na parkingu zadrzava 3 sekunde.
    Pri ulasku, ukoliko su sva parking mesta zauzeta, automobil mora da saceka da se neko parking
    mesto oslobodi.
*/
#include<iostream>
#include<thread>

using namespace std;

class parking {
    mutex m;
    condition_variable slobodan;
    int slobodnih_mesta;                        //Broj slobodnih mesta. Slicno kao kod zadatka a_i_b_pre_c, ovde ce brojac
                                                //predstavljati stanje deljene promenljive (parkinga).
  public:
    parking(int N) : slobodnih_mesta(N) {}      //Na pocetku ima N slobodnih mesta na parkingu (realniji scenario nego samo 1).
    void udji();
    void izadji();
};

void parking::udji() {
    unique_lock<mutex> l(m);
    while (slobodnih_mesta == 0) {              //Dogod NEMA slobodnih mesta na parkignu svaki novi automobil mora da ceka.
        slobodan.wait(l);
    }
    --slobodnih_mesta;                          //Ukoliko je uspeo da udje na parking, automobil smanjuje broj slobodnih mesta.
}

void parking::izadji() {
    unique_lock<mutex> l(m);
    slobodan.notify_one();                      //Kada izlazi automobil povecava broj slobodnih mesta i notificira jednog od
    ++slobodnih_mesta;                          //automobila koji cekaju u redu.
}

mutex m;
void automobil(parking& p) {
   p.udji();
   { unique_lock<mutex> l(m);
      cout << "Automobil " << this_thread::get_id() << " usao na parking." << endl;
   }
   this_thread::sleep_for(chrono::seconds(rand()%3 + 1));       //Automobil se zadrzava izmedju 1 i 3 sekunde na parkingu.
                                                                //Ovo se radi da ne bi svi ulazili i izlazili u ista vremena.
   p.izadji();
   { unique_lock<mutex> l(m);
      cout << "Automobil " << this_thread::get_id() << " izasao sa parkinga." << endl;
   }
}

const int automobila = 10;
const int KAPACITET = 3;
int main() {
   parking p(KAPACITET);                //Parking ima na pocetku KAPACITET slobodnih mesta.
   thread t[automobila];
   for(int i=0; i<automobila; i++)
      t[i] = thread(automobil, ref(p));
   for(int i=0; i<automobila; i++)
      t[i].join();
}
