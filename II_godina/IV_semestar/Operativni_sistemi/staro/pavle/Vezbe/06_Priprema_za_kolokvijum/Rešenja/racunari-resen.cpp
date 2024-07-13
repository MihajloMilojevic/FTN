/*
Modelovati koriscenje racunara u racunarskoj ucionici. Broj racunara u ucionici se prosledjuje pri inicijalizaciji.
Student pozivom operacije zauzmi() dolazi u ucionicu i zauzima prvi slobodan racunar, ukoliko takav racunar postoji.
Ukoliko su svi racunari zauzeti, student mora sacekati da se neki racunar oslobodi.
Operacija zauzmi() vraca redni broj racunara koji je student zauzeo.
Student koristi racunar neki slucajan broj sekundi.
Operacijom oslobodi(), student zavrsava rad u ucionici. Parametar metode je redni broj racunara koji student koristi i koji
treba da se oslobodi.
*/

#include <thread>
#include <iostream>
#include <mutex>
#include <condition_variable>

using namespace std;

#define MAX 50                                  // maksimalni broj racunara u ucionici

class RC {
private:
    bool slobodni[MAX];                         // za svaki racunar evidentira se podatak da li se trenutno koristi
    condition_variable c;                       // red cekanja na bilo koji slobodan racunar (svi korisnici cekaju u jednom zajednickom redu)
    int broj_slobodnih;                         // broj trenutno slobodnih racunara
    int broj_racunara;                          // ukupan broj racunara u ucionici
    mutex m;                                    // propusnica za sprecavanje stetnog preplitanja prilikom pristupa atributima klase
public:
    RC(int br);
    int zauzmi();
    void oslobodi(int id_racunara);
};

RC::RC(int br) {
    broj_racunara = br;                         // ukupan broj racunara je prosledjen spolja pri instanciranju
    broj_slobodnih = broj_racunara;             // inicijalno su svi racunari slobodni
    for (int i = 0; i < broj_slobodnih; ++i)    // za svaki racunar se evidentira da je slobodan
        slobodni[i] = true;
}

int RC::zauzmi() {
    unique_lock<mutex> l(m);                    // zauzimanje propusnice pre pristupa deljenim promenljivim
    while (broj_slobodnih == 0)                 // dok god nijedan racunar nije slobodan, korisnik mora da saceka
        c.wait(l);

    int retVal;                                 // povratna vrednost metode - broj racunara koji je zauzet
    for (int i = 0; i < broj_racunara; ++i) {   // trazimo racunar koji se oslobodio
        if (slobodni[i]) {
            slobodni[i] = false;                // zauzimamo racunar koji smo pronasli kao slobodan
            retVal = i + 1;                     // upamtimo indeks racunara (dodamo 1 da bi brojevi isli od 1, a ne od 0 kao indeksi)
            break;                              // nema potrebe da se dalje pretrazuje kada je racunar pronadjen
        }
    }
    --broj_slobodnih;                           // nakon zauzimanja racunara, ima jedan slobodan racunar manje
    return retVal;
}

void RC::oslobodi(int id_racunara) {
    unique_lock<mutex> l(m);
    ++broj_slobodnih;                           // oslobadjanjem racunara, ima jedan slobodan racunar vise
    slobodni[id_racunara-1] = true;             // oznacimo da je racunar sa prosledjenim brojem slobodan (umanjujemo prosledjenu vrednost za 1, jer indeksi u nizu idu od 0, a brojevi racunara od 1)
    c.notify_one();                             // javimo nekom od korisnika koji cekaju da se pojavio slobodan racunar
}

mutex term_mx;                                  // propusnica za sprecavanje stetnog preplitanja prilikom pristupa terminalu

void student(RC &rc, int br_indeksa) {
    {
        unique_lock<mutex> l(term_mx);
        cout << "Student " << br_indeksa << " zeli da koristi ucionicu. " << endl;
    }
    int id_racunara  = rc.zauzmi();             // zauzimanje racunara (uz moguce cekanje)
    {
        unique_lock<mutex> l(term_mx);
        cout << "Student " << br_indeksa << " seo za racunar " << id_racunara << endl;
    }
    this_thread::sleep_for(chrono::seconds(rand()%5 + 1)); //simuliranje koriscenja racunara uspavljivanjem niti
    rc.oslobodi(id_racunara);                   // oslobadjanje racunara sa navedenim brojem
    {
        unique_lock<mutex> l(term_mx);
        cout << "Student " << br_indeksa << " zavrsio rad u ucionici." << endl;
    }
}

const int STUDENATA = 10;

int main() {
    RC rc(3);
    thread t[STUDENATA];
    for (int i = 0; i < STUDENATA; ++i)
        t[i] = thread(student, ref(rc), i + 1);

    for (int i = 0; i < STUDENATA; ++i)
        t[i].join();

}
