/*
	Modelovati koriscenje zaletista na atletskom mitingu.
	Isto zaletiste koriste dve discipline: skok u dalj i bacanje koplja.
	Zaletiste ne mogu istovremeno da koriste dva takmicara.
	Discipline se naizmenicno smenjuju na zaletistu (jedan skakac u dalj, pa jedan bacac koplja i tako redom).
	
	Skok u dalj za jednog takmicara traje 1 sekundu. Bacanje koplja 2 sekunde.
	Metodu skaci poziva skakac u dalj. Metoda vraca duzinu u metrima koliko je takmicar skocio 
	(izmedju 0 i 9 metara moze skociti) i koliko je ukupno trebalo vremena da zavrsi skok 
	(koliko je zajedno trajalo cekanje i skakanje).
	Metodu baciKoplje poziva bacac koplja. Metoda vraca duzinu u metrima koliko je takmicar bacio koplje 
	(izmedju 0 i 100 metara moze baciti) i koliko je ukupno trebalo vremena da zavrsi bacanje koplja
	(koliko je zajedno trajalo cekanje i bacanje koplja).
*/

#include <thread>
#include <iostream>
#include <map>
#include <mutex>
#include <condition_variable>

using namespace std;
using namespace chrono;

struct povratna_vrednost {                      // Struktura koja opisuje povratnu vrednost, duzinu skoka ili bacanja i 
    int duzina;                                 // trajanje skoka i bacanja u milisekundama.
	int rezultat;
    duration<double, milli> trajanje;
};

class AtletskaStaza {                           
	private:
		mutex m;
		bool slobodno;                          // Da li je staza zauzeta.
		condition_variable skakaci, bacaci;     // Red cekanja za skakace i bacace.
		int skakaca, bacaca;                 	// Broj skakaca i bacaca koji cekaju.
    public:
        AtletskaStaza() {                       
            skakaca = 0;
            bacaca = 0;
            slobodno = true;
        }

		povratna_vrednost skaci() {             // Funkcija skakanja. Zovu je niti skakaca.
		    steady_clock::time_point dosao = steady_clock::now(); // Belezi se vreme dolaska.
			unique_lock<mutex> l(m);
			++skakaca;                          // Povecavamo broj skakaca u redu. Neophodno ovde a ne posle waita.
			while (!slobodno)                   
                skakaci.wait(l);                // Ukoliko je staza slobodna skaci, ako nije cekaj.    
            skakaca--;                          // Posle waita se smanjuje broj skakaca koji cekaju u redu, jer izlazi iz while ako je slobodno i skace
            slobodno = false;                   // Zauzimanje staze.
			l.unlock();
			this_thread::sleep_for(seconds(2)); // Izmedju 5 i 10 milisekundi mu treba da pretrci 10 m
            steady_clock::time_point zavrsio = steady_clock::now();   // Belezimo vreme zavrsetka skakanja
			l.lock();
            slobodno = true;                    // Oslobadjanje staze.
			if (bacaca > 0)                     // Provera da li ima bacaca koji cekaju. Ako ima obavesti ih da mogu bacati.
                bacaci.notify_one();
			else
                skakaci.notify_one();           // U suprotnom obavesti sledeceg skakaca da moze skociti.

            povratna_vrednost pv;
            pv.rezultat = rand()%10;            // Rezultat skoka je random broj do 10 metara
            pv.trajanje = zavrsio - dosao; 

            return pv;
		}

		povratna_vrednost baciKoplje() {
		    steady_clock::time_point dosao = steady_clock::now();
			unique_lock<mutex> l(m);
            ++bacaca;                           // Povecavamo broj bacaca u redu. Neophodno ovde a ne posle waita.
			while (!slobodno) {                 // Ukoliko je staza slobodna baci koplje, ako nije cekaj.  
                bacaci.wait(l);
			}
			bacaca--;                           // Posle waita se smanjuje broj bacaca koji cekaju u redu.
            slobodno = false;                   // Ostatak funkcije je istovetan funkciji skaci()...
			l.unlock();
			this_thread::sleep_for(seconds(1)); // Izmedju 5 i 10 milisekundi mu treba da pretrci 10 m
			steady_clock::time_point zavrsio = steady_clock::now();
			l.lock();
            slobodno = true;
			if (skakaca > 0)
                skakaci.notify_one();
			else
                bacaci.notify_one();

            povratna_vrednost pv;
            pv.rezultat = rand() % 100;           // Koplje leti do 100 metara.
            pv.trajanje = zavrsio - dosao;

            return pv;
		}
};

void skakac(AtletskaStaza& staza, int rbr) {
	povratna_vrednost rez = staza.skaci();
	cout << "Takmicar sa brojem " << rbr << " skocio " << rez.duzina << " metara"
         << ", a cekao " << rez.trajanje.count() << " milisekundi. " << endl;
}

void bacac(AtletskaStaza& staza, int rbr) {
	povratna_vrednost rez = staza.baciKoplje();
	cout << "Takmicar sa brojem " << rbr << " bacio koplje " << rez.duzina << " metara"
         << ", a cekao " << rez.trajanje.count() << " milisekundi. " << endl;
}

const int SKAKACA = 10;
const int BACACA = 10;
int main() {
    AtletskaStaza staza;
    thread skakaci[SKAKACA];                           
    thread bacaci[BACACA];

    for (int i = 0; i < 10; ++i) {
        skakaci[i] = thread(skakac, ref(staza), i+1);
        bacaci[i] = thread(bacac, ref(staza), i+1);
    }

    for (int i = 0; i < BACACA; ++i)
        bacaci[i].join();

    for (int i = 0; i < SKAKACA; ++i)
        skakaci[i].join();

}
