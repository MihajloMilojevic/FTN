/*
Modelovati soping na rasprodaji.
Kupci dolaze u prodavnicu da kupe odecu.

Kupac najpre probava odecu u jednoj od kabina za probavanje.
Broj kabina za probavanje prosledjuje se pri instanciranju klase Prodavnica.
Ako su sve kabine zauzete, kupac mora da saceka sa probavanjem dok se neka kabina ne oslobodi.

Nakon probavanja odece, kupac vrsi kupovinu, ako mu odeca odgovara.
Sansa da mu odeca odgovara je 50%.
Probavanje odece traje 1 sekundu.

Metoda "kupi" vraca informaciju da li je kupac kupio odecu i koliko dugo je cekao da 
udje u kabinu.

Data funkcija "kupac" modeluje ponasanje kupca.
Ako mu isprobana odeca ne odgovara, kupac odlazi da pronadje
drugi komad odece i onda ponovo odlazi da proba odecu u kabini.
*/



struct povratna_vrednost {
	bool kupio;
	duration<double, milli> cekao_na_kabinu;
};

class Prodavnica {
    public:
        Prodavnica(int n): slobodnih_kabina(n) {}
        povratna_vrednost kupi();
};

mutex term_m;
void kupac(Prodavnica &p, int id_kupca) {
    {
        unique_lock<mutex> l(term_m);
        cout << "Kupac " << id_kupca << " usao u prodavnicu." << endl;
    }
    povratna_vrednost pv;
    do {
        pv = p.kupi();
        unique_lock<mutex> l(term_m);
        if (pv.kupio)
            cout << "Kupac " << id_kupca << " kupio odecu. Cekao na kabinu: "
                << pv.cekao_na_kabinu.count() << " milisekundi." << endl;
        else {
            cout << "Kupac " << id_kupca << " nije kupio odecu. Cekao na kabinu: "
                << pv.cekao_na_kabinu.count() << " milisekundi." << endl;
            this_thread::sleep_for(seconds(1)); //kupac trazi novi komad odece
        }
    } while (!pv.kupio);
}

