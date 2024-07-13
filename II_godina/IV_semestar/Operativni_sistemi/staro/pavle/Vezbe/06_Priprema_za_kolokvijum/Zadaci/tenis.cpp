/*
Modelovati prvo kolo teniskog turnira koje se odrzava u teniskom klubu sa n terena.
Svaki teren ima svoj broj. (Brojevi su od 1 do n).

Na terenima se igraju teniski mecevi prvog kola teniskog turnira. U prvom kolu ucestvuje X takmicara, 
tako da ima M = X/2 teniska meca. Za svaki mec u startu se definise na kojem terenu ce biti odigran. 
Raspored meceva po terenima pravi se tako da se mecevi ravnomerno rasporede po terenima. 
Znaci, na svakom terenu se u proseku igraju n/M meca. Svaki mec ima svoj identifikator (broj).

Svaki mec traje slucajan vremenski period izmedju 1 i 5 sekundi. Naredni mec na terenu ne moze da pocne dok 
se prethodni mec na tom terenu ne zavrsi.

Za svaki mec potrebno je evidentirati kada su takmicari dosli na teren, kada je mec poceo i koliko je mec trajao.

Napomene:
    Komentari su obavezni.    
	Za dobijanje slucajnog broja koristiti datu funkciju rand_sync
*/

#include <cstdlib>

int rand_sync() {
        static mutex mx;
        unique_lock<mutex> l(mx);
        return rand();
}

struct podaci {
    int brojMeca;
    duration<double, milli> trajanje;
    monotonic_clock::time_point dosao;
    monotonic_clock::time_point pocetak;
};

class TeniskiKlub {
    public:
        TeniskiKlub(int ukupnoTerena);
        podaci odigrajMec(int, int);
};

mutex term_mx;

void mec(TeniskiKlub& tk, int brojMeca, int naTerenu) {
    podaci v = tk.odigrajMec(brojMeca, naTerenu);

    duration<double, milli> cekao = v.pocetak - v.dosao;
    unique_lock<mutex> l(term_mx);
    cout << "Mec " << v.brojMeca + 1 << " odigran na terenu " << naTerenu + 1 << " trajao " << v.trajanje.count() << " milisekundi. Takmicari su na pocetak meca cekali " << cekao.count()
        << " milisekundi. " << endl;
}