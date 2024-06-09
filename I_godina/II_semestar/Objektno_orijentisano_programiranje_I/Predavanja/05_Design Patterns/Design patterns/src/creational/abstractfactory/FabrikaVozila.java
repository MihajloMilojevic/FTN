package creational.abstractfactory;

public abstract class FabrikaVozila {
	public static final int FABRIKA_AUTOMOBILA = 0;
	public static final int FABRIKA_KAMIONA    = 1;
	
	public abstract Vozilo kreirajVozilo();

	public static FabrikaVozila getFabrika(int tip) {
		switch (tip) {
		case FabrikaVozila.FABRIKA_AUTOMOBILA: return new FabrikaAutomobila();
		case FabrikaVozila.FABRIKA_KAMIONA: return new FabrikaKamiona();
		default: return null;
		}
	}
}
