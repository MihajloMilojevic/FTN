package behavioral.iterator;

public class Test {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		NizAutomobila niz = new NizAutomobila();
		niz.dodaj(new Automobil("Audi", "A8"));
		niz.dodaj(new Automobil("Renault", "Laguna"));
		niz.dodaj(new Automobil("Fiat", "Punto"));
		
		IteratorAutomobila iterator = niz.vratiIterator();
		for (iterator.first(); !iterator.isDone(); iterator.next()) 
			System.out.println(iterator.current());
		
		System.out.println("=====================================");
		niz.dodaj(new Automobil("VolksWagen", "Passat"));

		for (iterator.first(); !iterator.isDone(); iterator.next()) 
			System.out.println(iterator.current());
		System.out.println("=====================================");
		
	}

}
