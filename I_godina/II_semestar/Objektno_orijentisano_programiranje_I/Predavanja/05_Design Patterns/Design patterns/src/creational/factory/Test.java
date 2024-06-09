package creational.factory;

public class Test {

	public static void main(String[] args) {
		Vozilo auto = FabrikaVozila.kreirajVozilo(FabrikaVozila.AUTOMOBIL);
		auto.vozi();
		Vozilo kamion = FabrikaVozila.kreirajVozilo(FabrikaVozila.KAMION);
		kamion.vozi();
		
		if (auto instanceof Automobil) {
			System.out.println("auto je objekat klase Automobil.");
		}
	}

}
