// Modelovati skladiste koje ima dve identicne rampe za istovar robe iz kamiona.

// Nosivost kamiona je maksimalno 7 tona.
// Kamioni nose obicnu ili zapaljivu robu.
// Kamioni sa zapaljivom robom imaju prednost pri istovaru.

// Kamion koji zeli da ostavi robu u skladistu poziva operaciju istovari().
// Kamion ceka ispred skadista dok jedna od rampi ne postane slobodna.
// Istovar traje onoliko sekundi koliko u kamionu ima tona robe.
// Operacija istovar() vraca pozivaocu informaciju o tome na kojoj rampi je
// kamion istovaren.

// Stvoriti 5 kamiona sa obicnom i 5 sa zapaljivom robom.


class skladiste {
public:
   skladiste();
   int istovari(int kolicina, bool zapaljivo);
};

void kamion(skladiste& s, int kolicina, bool zapaljivo) {
   static mutex term_m;
   {
      unique_lock<mutex> l(term_m);
      cout << "Kamion broj: " << this_thread::get_id() << " nosi "
           << kolicina << " tona ";
      if(zapaljivo) cout << "zapaljive robe" << endl;
      else          cout << "obicne robe" << endl;
   }
   int rampa = s.istovari(kolicina, zapaljivo);
   {
      unique_lock<mutex> l(term_m);
      cout << "Kamion broj: " << this_thread::get_id() 
           << " istovaren na rampi " << rampa << " (nosio " << kolicina;
     if(zapaljivo) cout << "; zapaljivo)." << endl;
     else          cout << "; obicno)." << endl;
   }
}

