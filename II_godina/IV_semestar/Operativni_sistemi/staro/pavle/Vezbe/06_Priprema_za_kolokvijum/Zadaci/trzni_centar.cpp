/*
Modelovati placanje robe u trznom centru. U trznom centru postoje 2 kase za placanje.
Kupac pri placanju staje u red na onu kasu na kojoj ceka manji broj kupaca. 
Kupac vrsi placanje pozivom metode kupi() koja kao parametar dobija broj artikala koje kupac placa.
Placanje robe traje onoliko sekundi koliko ima artikala.
Povratna vrednost metode je identifikator kase na kojoj je placanje izvrseno.
*/

class Prodavnica {
    public:
        int kupi(int broj_artikala);
};

mutex term_m;
void kupac(Prodavnica &p, int kolicina) {
    thread::id i = this_thread::get_id();
    {
        unique_lock<mutex> l(term_m);
        cout << "Kupac " << i << " zeli da kupi "
             << kolicina << " komada robe." << endl;
    }
    int kasa = p.kupi(kolicina);
    {
        unique_lock<mutex> l(term_m);
        cout << "Kupac " << i << " kupio na kasi " << kasa
             << ", " << kolicina << " komada robe." << endl;
    }
}