package creational.abstractfactory;

public class FabrikaAutomobila extends FabrikaVozila {

	@Override
	public Vozilo kreirajVozilo() {
		return new Automobil();
	}

}
