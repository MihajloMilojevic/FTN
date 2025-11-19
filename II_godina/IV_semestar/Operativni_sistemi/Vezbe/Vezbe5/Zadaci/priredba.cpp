/*
Napraviti konkurentni program koji bira najviseg ucenika i najvisu ucenicu
iz razreda, koji ce na skolskoj priredbi predstavljati svoj razred.
(Bilo bi logicno da se traze najlepsi - u pitanju je priredba, ali ne znam 
kako se meri lepota. I zato trazimo najvise.)

Ucenici (oba pola) su modelovani nitima nastalim od funkcije ucenik.
Pri stvaranju niti se zadaje pol i visina ucenika.
Podrazumeva se da u razredu ne postoje dva ucenika iste visine.
Svaki ucenik poziva operaciju prijava(),
koja vraca true ucenicima koji su izbrani, a false ostalima.

Organizator priredbe (funkcija main) poziva operaciju predstavnici() 
koja vraca identifiktore ucenika koji su izabrani 
da budu predstavnici razreda na priredbi.
Organizator ispisuje identifikatore izabranih ucenika.

Napomena:
main poziva operaciju predstavnici() _pre_ join(), a ispisuje 
predstavnike _posle_ join().
*/

enum Pol {M, Z};
class Priredba {
public:
    bool prijava(Pol pol, unsigned visina);
    std::pair<thread::id, thread::id> predstavnici();
};

void ucenik(Priredba& priredba, Pol pol, unsigned visina) {
    static mutex term;
    {
        unique_lock<mutex> l(term);
        cout << this_thread::get_id() << " : Pol " << (pol==M ? "M" : "Z")
             << ", visina " << visina << ". Prijavljujem se..."  << endl;
    }
    auto izabran_sam = priredba.prijava(pol, visina);
    {
        unique_lock<mutex> l(term);
        cout << this_thread::get_id() << " : Pol " << (pol==M ? "M" : "Z")
             << ", visina " << visina << ". "
             << (izabran_sam ? "JUUUUHUU!" : "Rasticu ja jos...") << endl;
    }
}

const unsigned UCENIKA = 10;
int main() {
    Priredba priredba(UCENIKA/2, UCENIKA/2);
    thread t[UCENIKA];
    for(auto i=0u; i<UCENIKA; ++i)
        t[i] = thread(ucenik, ref(priredba), static_cast<Pol>(i%2), i);
        
    auto p = priredba.predstavnici();
           
    for(auto i=0u; i<UCENIKA; ++i)
        t[i].join();
            
    cout << "Predstavnici su: " << p.first << " i " << p.second << endl;       
}
