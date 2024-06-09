package creational.abstractfactory;

public class Test {

	public static void main(String[] args) {
		FabrikaVozila fabrikaAutomobila = FabrikaVozila.getFabrika(FabrikaVozila.FABRIKA_AUTOMOBILA);
		
		Vozilo auto = fabrikaAutomobila.kreirajVozilo();
		auto.vozi();

		FabrikaVozila fabrikaKamiona = FabrikaVozila.getFabrika(FabrikaVozila.FABRIKA_KAMIONA);
		Vozilo kamion = fabrikaKamiona.kreirajVozilo();
		kamion.vozi();
		
//		if (auto instanceof Automobil) {
//			Automobil a = (Automobil)auto;
//			a.vozi();
//		}
		
	}
	

}
