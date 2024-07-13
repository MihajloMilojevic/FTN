/*
Napraviti konkurentni program koji simulira bezbednosne
propuste pri nadzoru zatvora.

Zatvorski krug podeljen je u 8 sektora.
Na sredini zatvorskog kruga je stub na kojem je postavljena kamera.
Kamera u jednom trenutku nadzire samo jedan sektor.
Dve sekunde nadzire jedan sektor i nakon toga se pomera na
naredni sektor (pomera se kruzno uvek u istu stranu,
u smeru kazaljke na satu).
Rad kamere predstavljen je koriscenjem niti koja izvrsava
datu funkciju "kamera".

10 zatvorenika pokusava da pobegne iz zatvora.
Njihova spavaonica se nalazi u sektoru 0, koji kamera
inicijalno nadgleda. Kako se kamera pomera,
zatvorenici se krecu za njom, u istom smeru, tako da su
uvek u sektoru koji kamera ne nadgleda.
Zatvoreniku treba jedna sekunda da pretrci iz jednog sektora u
drugi.

Izlaz iz zatvora je u sektoru 4.

Zatvorenici su predstavljeni nitima koji izvrsavaju funkciju
zatvorenik.

Pomoc: Nad niti koja izvrsava funkciju "kamera",
pozvati operaciju "detach" umesto "join",
jer ova nit stalno radi i ne treba cekati da se zavrsi.

Zbog lakseg pracenja rada programa, u okviru funkcije "pretrci" 
ispisati na konzolu da je zatvorenik pretrcao u drugi sektor 
(kada se ovo desi), kao i da se kamera pomerila (u trenutku kada se pomeri).

Napomena: KOMENTARI SU OBAVEZNI!
*/

class Zatvor {
    public:
        Zatvor();
        void pretrci(int ulaz, int br); //ulaz - sektor odakle krece (onaj u kojem je spavaonica). br - zatvorski broj zatvorenika
        void nadgledaj();
};

mutex term_m;

void zatvorenik(Zatvor& z, int sektor_spavaonice, int br) {
    {
        unique_lock<mutex> l(term_m);
        cout << "Zatvorenik " << br << " pokusava da pobegne "
            << " iz spavaonice u sektoru " << sektor_spavaonice << endl;
    }
    z.pretrci(sektor_spavaonice, br);
    {
        unique_lock<mutex> l(term_m);
        cout << "Zatvorenik " << br << " pobegao. " << endl;
    }
}

void kamera(Zatvor& z) {
    z.nadgledaj();
}