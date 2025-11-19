/* Napraviti sekvencijalni program koji izračunava sumu svih elemenata vektora
 * sekvencijalno, koristeći funkciju f():
 *
 * f(ci begin, ci end, double& zbir);
 *
 * pri cemu je ci definisano kao
 *
 * typedef vector<double>::const_iterator ci;
 */
#include <iostream>
#include <vector>

using namespace std;

/*
Definicija tipa iteratora na elemente vektora. Korisno je definisati tip ci zbog koriscenja
krace notacije u kasnijem kodu. const_iterator se koristi zato sto necemo menjati vrednosti
u vektoru (samo ih citamo). Da su se vrednosti menjale koristio bi se:

typedef vector<double>::iterator it;

Efektivno iterator je pokazivac na elemente vector-a, dok je vector kontejner koji sadrzi u
nasem slucaju elemente tipa double. U opstem slucaju vector moze sadrzati bilo koji tip
(genericka klasa).
*/
typedef vector<double>::const_iterator ci;

/*
Funkcija sabiranja elemenata vektora. Prihvata 3 parametra. Iterator na pocetak vektora,
iterator na kraj vektora i referencu na zbir.
*/
void f(ci begin, ci end, double &zbir) {
  zbir = 0;

  for (; begin != end; ++begin) // Prolazak kroz ceo vektor. Iteratori se mogu koristiti kao brojaci u for petlji.
    zbir += *begin;             // Pristup elementu na koji pokazuje iterator begin, tj. dodavanje datog elementa na ukupan zbir.
}

int main() {
  vector<double> v = {1, 2, 3, 4, 5, 6, 7, 8, 9}; // Vektor brojeva. Moze se inicijalizovati brojevima kao obican c-ovski niz.
  double zbir;

  f(v.begin(), v.end(), zbir); // Poziv funkcije f. Prosledjivanje pocetka i kraja vektora kao i reference na zbir.

  cout << "Zbir=" << zbir << endl;

  return 0;
}