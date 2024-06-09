package creational.factory;

public class FabrikaVozila {
	public static final int AUTOMOBIL = 0;
	public static final int KAMION    = 1;
	
	public static Vozilo kreirajVozilo(int tip) {
		switch (tip) {
		case AUTOMOBIL: return new Automobil();
		case KAMION:    return new Kamion();
		default:		return null;
		}
	}
}
