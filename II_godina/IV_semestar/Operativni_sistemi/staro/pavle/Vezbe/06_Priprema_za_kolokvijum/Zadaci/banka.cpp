// Napraviti konkurentni program koji modeluje kreditno poslovanje banke.
// Banka odobrava kredite u dinarima i u evrima.

// Klijent trazi kredit pozivanjem operacije uzmi_kredit(), 
// kojoj prosledjuje svotu koju zeli da pozajmi od banke 
// i valutu u kojoj zeli da pozajmi.
// Klijent neko vreme koristi pozajmljena sredstva, pa ih vrati banci
// pozivanjem operacije vrati_kredit().

// Banka inicijalno poseduje odredjene svote dinara 
// i evra na dva razlicita racuna, koje pozajmljuje.
// Banka odobrava kredite dok ima sredstava. 
// Kada vise nema sredstava, banka ceka da klijenti vrate 
// pretodno odobrene kredite pre nego sto odobri sledeci kredit.
// Banka odobrava kredite u proizvoljnom redosledu.

// Banka tezi tome da klijent ciji je zahtev moguce ispunitini 
// (postoje sredstva) ne ceka na kredit.

// Komentari su obavezni




class banka {
public:
   enum valute {DINAR=0, EVRO};
   banka(int inicijalni_dsaldo, int inicijalni_esaldo) ;
   int uzmi_kredit( int svota, valute valuta);
   int vrati_kredit(int svota, valute valuta);
};

string naziv_valute(banka::valute valuta) {
   if(valuta==banka::DINAR)  return "dinar";
   else                      return "evro";
}

void klijent(banka& b, int svota, banka::valute valuta) {
   static mutex term_m;
   thread::id id = this_thread::get_id();
   int saldo;
   {
   unique_lock<mutex> l(term_m);
   cout << "Klijent: " << id << " trazi na zajam " << svota 
        << ", valuta: " << naziv_valute(valuta) << endl;
   }
   saldo = b.uzmi_kredit(svota, valuta);
   {
   unique_lock<mutex> l(term_m);
   cout << "Klijent: " << id << " dobio " << svota 
        << ", u banci ostalo: " << saldo 
        << ", valuta: " << naziv_valute(valuta) << endl;
   }
   // klijent koristi pozajmljeni novac
   this_thread::sleep_for(chrono::seconds(1));
   saldo = b.vrati_kredit(svota, valuta);
   unique_lock<mutex> l(term_m);
   cout << "Klijent: " << id << " vratio " << svota
        << ", u banci ostalo: " << saldo
        << ", valuta: " << naziv_valute(valuta) << endl;
}


