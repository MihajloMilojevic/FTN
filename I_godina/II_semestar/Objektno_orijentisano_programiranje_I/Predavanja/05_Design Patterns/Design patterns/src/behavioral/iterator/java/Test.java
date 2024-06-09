package behavioral.iterator.java;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class Test {
	public static void main(String[] args) {
		Automobil[] niz = new Automobil[] { new Automobil("Audi", "A8"),
				new Automobil("Renault", "Laguna"),
				new Automobil("Fiat", "Punto") };

		for (Automobil a : niz)
			System.out.println(a);
		
		System.out.println("=====================================");
		
		Collection<Automobil> kolekcija = new ArrayList<Automobil>();
		kolekcija.add(new Automobil("Audi", "A8"));
		kolekcija.add(new Automobil("Renault", "Laguna"));
		kolekcija.add(new Automobil("Fiat", "Punto"));

		Iterator<Automobil> iterator = kolekcija.iterator();
		while (iterator.hasNext())
			System.out.println(iterator.next());

		System.out.println("=====================================");
		kolekcija.add(new Automobil("VolksWagen", "Passat"));

		for (Automobil a : kolekcija)
			System.out.println(a);
		System.out.println("=====================================");
		
		iterator = kolekcija.iterator();
		while (iterator.hasNext())
			System.out.println(iterator.next());

		System.out.println("=====================================");

	}
}
