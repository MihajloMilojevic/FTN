// Modelovati salter salu u posti u kojoj postoje 2 saltera.

// Vremensko trajanje uplate (boravak klijenta na salteru) je srazmerno 
// velicini uplate. Za svaku uplacenu hiljadu dinara klijent ceka 1 sec.
// Na salteru se moze uplatiti maksimalno 4 hiljada dinara.
// (podrazumeva se da je ispravna vrednost prosledjena klijentu 
// pri stvaranju niti).

// Kada klijent zeli da uplati sredstava, on poziva operaciju uplati(), 
// cime prakticno ulazi u postu i staje u red.
// Povratna vrednost ove operacije je broj saltera na kojem je klijent
// izvrsio uplatu i svota koja je do tog trenutka na salteru uplacena.

// Treba stvoriti 7 klijenata.


struct povratna_vrednost {
   int salter;
   int uplaceno;
   povratna_vrednost(int s, int u) : salter{s}, uplaceno{u} {}
};

class posta {
public:
   posta();
   povratna_vrednost uplati(int svota);
};

void klijent(posta& p, int svota) {
   static mutex term_m;
   {
      unique_lock<mutex> l(term_m);
      cout << "Klijent broj: " << this_thread::get_id() 
           << " zeli da uplati " << svota
           << " hiljada dinara." << endl;
   }
   auto ret = p.uplati(svota);
   {
      unique_lock<mutex> l(term_m);
      cout << "Klijent broj: " << this_thread::get_id() << " ("
           << svota << ") salter " << ret.salter 
           << " (" << ret.uplaceno << ")"<< endl;
   }
}

