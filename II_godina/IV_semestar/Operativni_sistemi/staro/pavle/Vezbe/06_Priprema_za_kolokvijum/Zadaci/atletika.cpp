/*
	Modelovati koriscenje zaletista na atletskom mitingu.
	Isto zaletiste koriste dve discipline: skok u dalj i bacanje koplja.
	Zaletiste ne mogu istovremeno da koriste dva takmicara.
	Discipline se naizmenicno smenjuju na zaletistu (jedan skakac u dalj, pa jedan bacac koplja i tako redom).
	
	Skok u dalj za jednog takmicara traje 1 sekundu. Bacanje koplja 2 sekunde.
	Metodu skaci poziva skakac u dalj. Metoda vraca duzinu u metrima koliko je takmicar skocio 
	(izmedju 0 i 9 metara moze skociti) i koliko je ukupno trebalo vremena da zavrsi skok 
	(koliko je zajedno trajalo cekanje i skakanje).
	Metodu baciKoplje poziva bacac koplja. Metoda vraca duzinu u metrima koliko je takmicar bacio koplje 
	(izmedju 0 i 100 metara moze baciti) i koliko je ukupno trebalo vremena da zavrsi bacanje koplja
	(koliko je zajedno trajalo cekanje i bacanje koplja).
*/

struct povratna_vrednost {
    int duzina;
    duration<double, milli> trajanje;
};

class AtletskaStaza {
    public:
		povratna_vrednost skaci();
		povratna_vrednost baciKoplje();
};

void skakac(AtletskaStaza& staza, int rbr) {
	povratna_vrednost rez = staza.skaci();
	cout << "Takmicar sa brojem " << rbr << " skocio " << rez.duzina << " metara."
         << ", a cekao " << rez.trajanje.count() << " milisekundi. " << endl;
}

void bacac(AtletskaStaza& staza, int rbr) {
	povratna_vrednost rez = staza.baciKoplje();
	cout << "Takmicar sa brojem " << rbr << " bacio koplje " << rez.duzina << " metara."
         << ", a cekao " << rez.trajanje.count() << " milisekundi. " << endl;
}