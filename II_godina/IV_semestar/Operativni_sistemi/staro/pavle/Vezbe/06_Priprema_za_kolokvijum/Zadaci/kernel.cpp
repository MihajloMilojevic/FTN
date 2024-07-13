/* 
Napraviti konkurentni program koji simulira ponasanje kernela operativnog sistema pri dodelu 2-jezgarnog procesora nitima.

Niti pokusavaju da zauzmu jedno od jezgara procesora. Ukoliko je bar jedno jezgro slobodno, ono se dodeljuje niti na koriscenje odredjeni vremenski period delta koji iznosi 1 sekundu. Ukoliko su oba jezgra zauzeta nit ceka na jezgru na kome ceka manje niti (kako bi se raspodelilo opterecenje). 

Nakon koriscenja jezgra delta (1) sekundi nit prepusta jezgro nekoj drugoj niti koja ceka za njegovo koriscenje (bilo da je u pitanju nit koja je tek dosla na cekanje ili neka druga nit kojoj je bio istekao vremenski period delta) i ulazi u cooldown (cekanje pre ponovnog pokusaja zauzimanja procesora kako bi se dala sansa drugim nitima da koriste procesor).

Nakon cooldown perioda (10 ms) nit ponovo pokusava da zauzme procesor. Data sekvenca zauzimanje-otpustanje procesora se izvrsava minimalno jednom ili vise puta u zavisnosti koliko sekundi nit pokusava da koristi procesor.

Da bi se ispratio rad programa potrebno zabeleziti trenutak pocetka koriscenjas (nakon zauzimanja) procesora od strane niti kao i trenutak kraja koriscenja procesora. Dati trenuci se koriste u niti radi izracunavanja trajanja operacije koriscenja procesora.

Kreirati 1 procesor i 10 niti. Svaka nit treba da pokusava da zauzme procesor proizvoljan vremenski
period od 1-4 sekunde. 

Napomena: Obratiti paznju da nit u toku rada ne mora uvek zauzimati isto jezgro procesora.

Komentari su obavezni.
*/


struct vremena {
	monotonic_clock::time_point pocetak;
	monotonic_clock::time_point kraj;
};

class Procesor {
public:
	vremena zauzmi_procesor(int sekundi);
};

mutex term_mx;

void nit(Procesor & p, int rbr, int sekundi) {
	vremena vr = p.zauzmi_procesor(sekundi);
	double multiplier = 1;
	if (sekundi > 1)  multiplier = 1.01;
	duration<double> s = vr.kraj - vr.pocetak;

	unique_lock<mutex> l(term_mx);
	cout << "Nit broj: " << rbr << " provela u cekanju i koriscenju procesora: " 
		 << s.count() << " sekundi od planiranih: " << sekundi*multiplier << " sekundi." 
		 << endl;
}

