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

#include <iostream>
#include <mutex>

using namespace std;

/****************************************************************************/
// Ove funkcije se koriste za ispis poruka na standardni izlaz. U implementaciji
// zadatka treba na odgovarajucim mestima pozvati funkcije kamera_se_pomerila
// i pretrcao_u_sektor. Ostale funkcije su vec pozvane gde treba.

mutex term_m;

// br - redni broj zatvorenika
// sektor_spavaonice - redni broj sektora spavaonice
void zatvorenik_krenuo_u_beg(int br, int sektor_spavaonice) {
    unique_lock<mutex> l(term_m);
    cout << "Zatvorenik " << br << " pokusava da pobegne "
         << " iz spavaonice u sektoru " << sektor_spavaonice << endl;
}

// br - redni broj zatvorenika koji je pobegao
void zatvorenik_pobegao(int br) {
    unique_lock<mutex> l(term_m);
    cout << "Zatvorenik " << br << " pobegao. " << endl;
}

// br - redni broj zatvorenika
// zeljeni_sektor - redni broj sektora u koji je zatvorenik pretrcao
void zatvorenik_pretrcao_u_sektor(int br, int zeljeni_sektor) {
    unique_lock<mutex> l(term_m);
    cout << "Zatvorenik " << br << " pretrcao u sektor "
         << zeljeni_sektor << "." << endl;
}

// sektor - redni broj sektora koji kamera posmatra
void kamera_se_pomerila(int sektor) {
    unique_lock<mutex> l(term_m);
    cout << "Kamera se pomerila na sektor " << sektor << "." << endl;
}
/****************************************************************************/

class Zatvor {
private:
    // TODO dodati polja klase
public:
    // TODO implementirati navedene metode
    Zatvor();
    void pretrci(int ulaz, int br); //ulaz - sektor odakle krece (onaj u kojem je spavaonica). br - zatvorski broj zatvorenika
    void nadgledaj();
};

void zatvorenik(Zatvor& z, int sektor_spavaonice, int br) {
    zatvorenik_krenuo_u_beg(br, sektor_spavaonice);
    z.pretrci(sektor_spavaonice, br);
    zatvorenik_pobegao(br);
}

void kamera(Zatvor& z) {
    z.nadgledaj();
}

int main() {
    // TODO Implementirati
}