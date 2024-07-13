/*
Napisati program za unos reci sa tastature sa ukljucenom proverom ispravnosti unosa.
Dat je vektor recnik koji predstavlja reci koje sistem prepoznaje kao ispravne.
Funkcija proveri_ispravnost() utvrdjuje da li se prosledjena rec nalazi u recniku.

U glavnom programu korisnik unosi jednu po jednu rec. Nakon unosa reci, u posebnoj niti se vrsi provera ispravnosti reci.

Kada korisnik zavrsi unos svih reci, za svaku rec se ispisuje da li je ispravno unesena.
Primer ispisa:
Rec 1 ispravno napisana.
Rec 2 neispravno napisana.
Rec 3 ispravno napisana.
*/

vector<string> recnik{"black", "red", "blue", "yellow", "white"};

bool proveri_ispravnost(string rec);