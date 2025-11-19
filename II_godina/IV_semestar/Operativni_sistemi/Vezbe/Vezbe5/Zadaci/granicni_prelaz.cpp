
/*
Modelovati pogranicni prelaz sa 4 rampe za propustanje (gledano samo u jednom pravcu) pri cemu su tri rampe za automobile, a jedna za kamione. 

Od toga je jedna automobilska rampa za automobile iz Evropske unije a ostale 2 za automobile iz ostalih zemalja. Automobili ulaze na rampe (ako postoji slobodna odgovarajuceg tipa a u suprotnom cekaju). 

Obicni automobili cekaju na jednoj od 2 rampe za obicne automobile, sa tim sto cekaju na rampi na kojoj je red cekanja kraci. Zadrzavaju se na rampama onoliko sekundi koliko ima putnika (maksimalno 5). 

Kamioni se zadrzavaju na rampi onoliko sekundi koliko imaju robe u sebi.

Zadatak se radi 2 sata i 45 minuta

Komentari su obavezni!
*/
#include <iostream>
#include <mutex>
#include <map>
#include <thread>
#include <condition_variable>
#include <vector>
#include <random>
#include <sstream>

using namespace std;

#define BROJ_VOZILA 10

enum tip_vozila {eu = 0, obicni, kamion};

struct GranicniPrelaz {
   mutex m;
   map<tip_vozila, vector<vector<std::thread::id> > > rampe;
   map<tip_vozila, vector<unique_ptr<std::condition_variable>>> c;
   GranicniPrelaz() {
      rampe[eu].push_back(vector<std::thread::id>());
      rampe[obicni].push_back(vector<std::thread::id>());
      rampe[obicni].push_back(vector<std::thread::id>());
      rampe[kamion].push_back(vector<std::thread::id>());
      
      c[eu].push_back(make_unique<condition_variable>());
      c[obicni].push_back(make_unique<condition_variable>());
      c[obicni].push_back(make_unique<condition_variable>());
      c[kamion].push_back(make_unique<condition_variable>());
   }
   string predji_prelaz(tip_vozila tip, int kolicina) {
      int index = 0;
         auto id = this_thread::get_id();
      {
         unique_lock<mutex> l(m);
         index = _najkraći_red(tip);
         rampe[tip][index].push_back(id);
         while (rampe[tip][index][0] != id) 
         {
            c[tip][index]->wait(l);
         }
      }
      this_thread::sleep_for(chrono::seconds(kolicina));
      {
         unique_lock<mutex> l(m);
         rampe[tip][index].erase(rampe[tip][index].begin());
         c[tip][index]->notify_all();
         return _ime_rampe(tip, index);
      }
   }
   string _ime_rampe(tip_vozila tip, int index) {
      stringstream ss;
      switch (tip)
      {
      case eu: 
         ss << "EU";
         break;
      case obicni:
         ss << "OBICNA";
         break;
      case kamion:
         ss <<"KAMION";
         break;
      default:
         ss << "Nepoznato";
         break;
      }
      ss << "-" << index + 1;
      return ss.str();
   }
   int _najkraći_red(tip_vozila tip) {
      // Funkcija pretpostavlja da je već zaključana
      int min_index = 0;
      auto& r = rampe[tip];
      for(int i = 1; i < r.size(); ++i)
         if (r[i].size() < r[min_index].size())
            min_index = i;
      return min_index;
   }
};

GranicniPrelaz gp;

ostream& operator <<(ostream& out, tip_vozila t) {
   switch (t)
   {
   case eu:
      out << "EU";
      break;
   case obicni:
      out << "OBICNI";
      break;
   case kamion:
      out << "KAMION";
      break;
   default:
      out << "Nepoznat";
      break;
   }
   return out;
}

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

int main() {
   thread t[BROJ_VOZILA];
   for(int i = 0; i < BROJ_VOZILA; ++i)
      t[i] = thread(vozilo, tip_vozila(rand() % 3), i, rand() % 5);
   
   for(int i = 0; i < BROJ_VOZILA; ++i)
      t[i].join();
   
}