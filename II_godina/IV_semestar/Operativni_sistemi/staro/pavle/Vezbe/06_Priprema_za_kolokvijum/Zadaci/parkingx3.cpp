// Parking sa 3 ulaza.
// Na parking automobili ulaze sa ulaza 0, 1 i 2 po round-robin protokolu
// (jedan udje sa prvog, jedan sa drugog, jedan sa treceg i tako u krug).

// Automobilu se pri stvaranju prosledjuje vreme (u sekundama) koje se on 
// zadrzave na parkingu.
// U programu uvek ima jednak broj automobila na svim ulazima!

class parking {
public:
   parking();
   void udji(int ulaz);
   void izadji();
};

void automobil(parking& p, int ulaz, int ostajem_na_parkingu) {
    static mutex term_m;
    thread::id id = this_thread::get_id();
    {
        unique_lock<mutex> l(term_m);
        cout<<"Automobil "<<id<<" pokusava da udje na parking na ulaz "<< ulaz<<endl;
    }
    p.udji(ulaz);
    {
        unique_lock<mutex> l(term_m);
        cout<<"Automobil "<<id<<" usao na parking na ulaz "<< ulaz<<endl;
    }
    this_thread::sleep_for(chrono::seconds(ostajem_na_parkingu));
    p.izadji();
    unique_lock<mutex> l(term_m);
    cout<<"Automobil "<<id<<" izasao sa parkinga."<<endl;
}

