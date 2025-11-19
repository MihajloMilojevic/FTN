/*Modelovati koriscenje racunara u racunarskoj ucionici. Broj racunara u ucionici se prosledjuje pri inicijalizaciji.
Student pozivom operacije zauzmi() dolazi u ucionicu i zauzima prvi slobodan racunar, ukoliko takav racunar postoji.
Ukoliko su svi racunari zauzeti, student mora sacekati da se neki racunar oslobodi.
Operacija zauzmi() vraca redni broj racunara koji je student zauzeo.
Student koristi racunar neki slucajan broj sekundi.
Operacijom oslobodi(), student zavrsava rad u ucionici. Parametar metode je redni broj racunara koji student koristi i koji
treba da se oslobi.
*/

class RC {
	public:
		RC(int br);
		int zauzmi();
		void oslobodi(int id_racunara);
};

mutex term_mx;

void student(RC &rc, int br_indeksa) {
    {
        unique_lock<mutex> l(term_mx);
        cout << "Student " << br_indeksa << " zeli da koristi ucionicu. " << endl;
    }
    int id_racunara  = rc.zauzmi();
    {
        unique_lock<mutex> l(term_mx);
        cout << "Student " << br_indeksa << " seo za racunar " << id_racunara << endl;
    }
    this_thread::sleep_for(chrono::seconds(rand()%5 + 1));
    rc.oslobodi(id_racunara);
    {
        unique_lock<mutex> l(term_mx);
        cout << "Student " << br_indeksa << " zavrsio rad u ucionici." << endl;
    }
}