/*
Simulirati rad Operativnog sistema koji ima sledece funkcionalnosti.
1. Pokretanje i zaustavljanje servisa. Programski kod koji servisi izvrsavaju dat je u obliku slobodnih funkcija.
Za potrebe testiranja, date su dve funkcije serviceA i serviceB. Svaki servis predstavljen je posebnom klasom, kojoj se .
pri instanciranju definise programski kod koji ce izvrsavati po startovanju. Proces se izvrsava u posebnoj niti.

2. Rad sa fajlovima. Omoguciti kreiranje, brisanje i preimenovanje fajlova i direktorijuma u operativnom sistemu 
	(fajlovi i direktorijumi su hijerarhijski organizovani) 

3. Rad sa korisnicima. Omoguciti administraciju (unos, izmena, brisanje) korisnika u sistemu. Omoguciti organizovanje korisnika u grupe.
	
4. Napraviti podrsku za prava pristupa fajlovima. Svaki korisnik nad fajlom ima pravo citanja, pisanja ili i jedno i drugo.

Implementirati Shell koji omogucuje koriscenje navedenih funkcionalnosti.

*/

void serviceA() {
	cout << "Process f1 started." << endl;
	for (int i =0; i < 1000000; i++) {
	}
	cout << "Process f1 finished." << endl;
}

void serviceB() {
	while (true) {
		cout << "f2 hello" << endl;
	}
}
