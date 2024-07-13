// Modelovati benzinsku pumpu na kojoj se toce 3 vrste goriva:
// bezolovni, dizel i super.
// Svako vozilo koje zeli da natoci gorivo mora da stane u red za tu vrstu goriva.
// Tocenje bezolovnog traje 1 sekundu, dizela 2, a supera 3 sekunde.

// Vozilo koje zeli da natoci gorivo poziva operaciju natoci() i prosledjuje joj 
// vrstu goriva koja mu je potrebna.

// Treba stvoriti po 4 vozila za svaku vrstu goriva.

// Komentari su obavezni.




class benzinska_pumpa {
public:
   enum vrsta_goriva { BEZOLOVNI=0, DIZEL, SUPER };
   benzinska_pumpa();
   void natoci(vrsta_goriva gorivo);
};

string naziv_goriva(benzinska_pumpa::vrsta_goriva gorivo) {
   if(gorivo==benzinska_pumpa::BEZOLOVNI)  return "bezolovni";
   else if(gorivo==benzinska_pumpa::SUPER) return "super";
   else                                    return "dizel";
}

void vozilo(benzinska_pumpa& pumpa, benzinska_pumpa::vrsta_goriva gorivo) {
   static mutex term_m;
   { 
   unique_lock<mutex> l(term_m);
   cout << "Vozilu " << this_thread::get_id() 
        << " je potrban " << naziv_goriva(gorivo) << endl;
   }
   pumpa.natoci(gorivo);
   unique_lock<mutex> l(term_m);
   cout << "Vozilo " << this_thread::get_id() 
        << " je natocilo " << naziv_goriva(gorivo) << endl;
}
