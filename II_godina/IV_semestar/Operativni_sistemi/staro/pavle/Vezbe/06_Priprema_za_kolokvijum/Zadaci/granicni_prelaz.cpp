
/*
Modelovati pogranicni prelaz sa 4 rampe za propustanje (gledano samo u jednom pravcu) pri cemu su tri rampe za automobile, a jedna za kamione. 

Od toga je jedna automobilska rampa za automobile iz Evropske unije a ostale 2 za automobile iz ostalih zemalja. Automobili ulaze na rampe (ako postoji slobodna odgovarajuceg tipa a u suprotnom cekaju). 

Obicni automobili cekaju na jednoj od 2 rampe za obicne automobile, sa tim sto cekaju na rampi na kojoj je red cekanja kraci. Zadrzavaju se na rampama onoliko sekundi koliko ima putnika (maksimalno 5). 

Kamioni se zadrzavaju na rampi onoliko sekundi koliko imaju robe u sebi.

Zadatak se radi 2 sata i 45 minuta

Komentari su obavezni!
*/



void vozilo (tip_vozila tip, int redni_broj_vozila, int kolicina_robe_ili_putnika) {
   static mutex term_m;
   {
      unique_lock<mutex> l(term_m);
      cout << "Vozilo broj: " << redni_broj_vozila << " tipa "
           << tip << " nosi " << kolicina_robe_ili_putnika;
      if((tip == eu) || (tip == obicni)) cout << " putnika" << endl;
      else          cout << " tona robe" << endl;
   }
   string prelaz = gp.predji_prelaz(tip, kolicina_robe_ili_putnika);
   {
      unique_lock<mutex> l(term_m);
      cout << "Vozilo broj: " << redni_broj_vozila
           << " preslo prelaz " << prelaz << " (nosio " << kolicina_robe_ili_putnika;
     if((tip == eu) || (tip == obicni)) cout << "; putnika.)" << endl;
     else          cout << "; tona robe)." << endl;
   }

}


