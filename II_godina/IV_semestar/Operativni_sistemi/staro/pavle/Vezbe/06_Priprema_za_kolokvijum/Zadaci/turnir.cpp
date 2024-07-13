/*
Napraviti konkurentni program koji simulira turnir u streljastvu.

Svaki takmicar prvo poziva operaciju pucaj da bi dobio priliku da 
ispuca svojih 10 metaka.
Gadja se kruzna streljacka meta i za svaki metak moze da se osvoji
do 10 poena (kaze se i 'krugova').
Takmicenje se odvija u streljani sa samo jednom trakom, tako da u svakom
trenutku najvise jedan takmicar moze da puca.
Operacija pucaj() vraca broj poena(krugova) koje je takmicar osvojio.

Zatim svaki takmicar poziva operaciju proglasenje_pobednika().
Povratna vrednost ove operacije je mesto koje je takmicar osvojio.

Podrazumeva se dva takmicara nikad nece osvojiti isti broj poena.

*/

class Turnir {
public:
    unsigned pucaj();
    unsigned proglasenje_pobednika();
};

void takmicar(Turnir& t) {
    static mutex term;
    {
        unique_lock<mutex> l(term);
        cout << this_thread::get_id() << " : Idem da pucam..."  << endl;
    }
    auto krugova = t.pucaj();
    {
        unique_lock<mutex> l(term);
        cout << this_thread::get_id() << " : Pogodio sam " << krugova 
             << " krugova." << endl;
    }
    //Takmicar odmara neko vreme pre proglasenja pobednika
    this_thread::sleep_for(chrono::milliseconds(10));
    auto osvojeno_mesto = t.proglasenje_pobednika();
    {
        unique_lock<mutex> l(term);
        cout << this_thread::get_id() << " : Osvojio sam " << osvojeno_mesto
             << ". mesto." << endl;
    }
}

