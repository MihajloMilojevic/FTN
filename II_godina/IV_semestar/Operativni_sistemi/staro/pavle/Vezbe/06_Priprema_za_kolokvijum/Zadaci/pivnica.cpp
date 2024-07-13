// Napisati konkurentni program koji modeluje pivnicu.
// U pivnici postoji ogranicen broj mesta (konstanta STOLICA_U_PIVNICI).

// Pivopija poziva operaciju udji() kada zeli da udje u pivnicu.
// Pivopija ulazi u pivnicu ako u pivnici ima mesta, inace ceka da se 
// pojavi slobodno mesto.

// Kada udje u pivnicu, pivopija narucuje pivo pozivanjem operacije naruci().
// Tocenje velikog piva traje 2 sekunde, a malog 1 sekundu.
// Tokom tocenja barmen je zauzet i ne moze da opsluzuje druge pivopije.

// Kada dobije pivo pivopija provede jos neko vreme u pivnici pijuci ga,
// a zatim napusti pivnicu pozivom operacije izadji().

// Stvoriti 10 pivopija (5 piju malo, a 5 veliko pivo)

// Komentari su obavezni.


#include<iostream>

using namespace std;

class Pivnica {
public:
    enum Pivo { VELIKO, MALO };
    Pivnica(int stolica);
    void udji();
    void izadji();
    void naruci(Pivo velicina_piva);
};

void pivopija(Pivnica& pivnica, Pivnica::Pivo velicina_piva) {
    static mutex term_m;
    {
        unique_lock<mutex> l(term_m);
        cout  << this_thread::get_id() << " Pokusavam da udjem u pivnicu..." << endl;
    }
    pivnica.udji();
    {
        unique_lock<mutex> l(term_m);
        cout  << this_thread::get_id() << " Usao u pivnicu. Narucujem";
        if(velicina_piva == Pivnica::VELIKO)
            cout << " VELIKO ";
        else
            cout << " MALO ";
        cout << "pivo." << endl;
    }
    pivnica.naruci(velicina_piva);
    // 3 sekunde pivopija pije pivo, a zatim napusta pivnicu.
    this_thread::sleep_for(chrono::seconds(3));
    {
        unique_lock<mutex> l(term_m);
        cout  << this_thread::get_id() << " Popio. Odoh..." << endl;
    }
    pivnica.izadji();
};

