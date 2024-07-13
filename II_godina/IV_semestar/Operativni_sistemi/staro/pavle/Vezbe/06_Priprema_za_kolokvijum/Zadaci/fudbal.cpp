/*
Modelovati napadacku akciju fudbalskog kluba Barselona.
Tim sadrzi 11 igraca. Ponasanje igraca predstavljeno je datom funkcijom igrac.
Igraci medjusobno dodaju loptu, koja je predstavljena datom klasom Lopta.

Igrac mora da saceka da dobije loptu. Kada dobije loptu, igrac drzi loptu slucajan
vremenski period izmedju 1 i 3 sekunde i predaje je bilo kojem drugom igracu.
Pri predaji, lopta moze da ide unapred
(prema protivnickom golu) ili unazad. 2/3 predaja lopti ide ka napred.

Nakon 12 predaja lopti unapred, Barselona postize gol, cime se program zavrsava.
Ako pri predaji lopte igrac postigne gol, metoda dodaj_loptu vraca broj dresa igraca koji je postigao gol.
Nakon postignut gola, za sve ostale igrace metoda dodaj_loptu treba da vrati vrednost 0.
Ako gol nije postignut, metoda vraca vrednost "-1".

Barselona nikad ne gubi loptu.
*/



class Lopta {
    public:
        int dodaj_loptu(int broj_dresa);
};

mutex term_m;
void igrac(Lopta &lopta, int broj_dresa) {
    {
        unique_lock<mutex> l(term_m);
        cout << "Igrac sa brojem " << broj_dresa << " je izasao na teren." << endl;
    }
    int strelac = -1;
    do {
        strelac = lopta.dodaj_loptu(broj_dresa);
        cout << "Igrac " << broj_dresa << " dodao loptu." << endl;
        this_thread::sleep_for(seconds(1));
        if (strelac > 0) {
            unique_lock<mutex> l(term_m);
            cout << "GOOOOL!!! Pogodak je postigao igrac sa brojem " << strelac << "!" << endl;
        }
    } while (strelac == -1);
}

