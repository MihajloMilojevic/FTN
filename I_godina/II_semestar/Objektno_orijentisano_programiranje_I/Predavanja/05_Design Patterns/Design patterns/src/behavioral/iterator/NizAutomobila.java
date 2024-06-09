package behavioral.iterator;

public class NizAutomobila {
	int kapacitet;
	int trenutnoUnutra;
	Automobil[] niz;
	public NizAutomobila() {
		kapacitet = 3;
		niz = new Automobil[kapacitet];
		trenutnoUnutra = 0;
	}
	
	public void dodaj(Automobil auto) {
		if (trenutnoUnutra >= kapacitet) {
			int noviKapacitet = kapacitet * 2; 
			Automobil[] noviNiz = new Automobil[noviKapacitet];
			IteratorAutomobila iterator = vratiIterator();
			int j = 0;
			for (iterator.first(); !iterator.isDone(); iterator.next())
				noviNiz[j++] = iterator.current();

			kapacitet = noviKapacitet;
			niz = noviNiz;
		} 
		niz[trenutnoUnutra++] = auto;
	}
	
	IteratorAutomobila vratiIterator() {
		return new IteratorAutomobila(this);
	}
}
