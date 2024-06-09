package creational.abstractfactory;

public class FabrikaKamiona extends FabrikaVozila {
	
	@Override
	public Vozilo kreirajVozilo() {
		return new Kamion();
	}
}
