/* Napisati konkurentni program koji koristi STL kontejner <map>. U main-u
 * inicijalizovati mapu tako da sadrzi 10 elemenata pri cemu je kljuc broj od
 * 1-10 a vrednost id niti main.
 * 
 * Kreirati 10 niti klasom thread. Svakoj niti se prosleduje njen redni broj
 * prilikom stvaranja i referenca na mapu. Svaka nit u mapi treba upise svoj id
 * na element kojem je kljuc redni broj date niti (1-10).
 * 
 * Na kraju programa iz mape ispisati id-eve niti u obrnutom redosledu rednog
 * broja niti.
 */
#include <iostream>
#include <thread>
#include <map>

using namespace std;

typedef map<int, thread::id>::reverse_iterator Mi;      //reverse iterator na mapu. Omogucava kretanje u obrnutom redosledu.

void nit(int rbr, map<int,thread::id>& m) {         //Funkcija niti. Prima redni broj i referencu na mapu id-eva.
    m[rbr] = this_thread::get_id();         //Nit upisuje svoj id u element mape indeksiran njenim rednim brojem rbr.
}

int main () {
    map<int,thread::id> m;                  //Mapa id-jeva.
    thread t[10];                           

    for (int i=0; i<10; i++) {
        m[i+1] = this_thread::get_id();     //incijalizacija mape
    }

    for (int i=0; i<10; i++) {
        t[i] = thread(nit, i+1, ref(m));        //Stvaranje niti
    }

    for (int i=0; i<10; i++) {
        t[i].join();
    }

    for (Mi it = m.rbegin(); it!=m.rend(); it++ ) {         //Ispis niza id-eva iz mape, u obrnutom redosledu!
        cout << "Kljuc: " << it->first << " vrednost: " << it->second << endl;
    }

    return 0;
}
