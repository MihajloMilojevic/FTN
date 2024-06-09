package behavioral.templatemethod;

public class SalterUBanci extends PodizanjeNovcaTemplate {

	@Override
	protected void identifikujSe() {
		System.out.println("Dajemo ličnu kartu na uvid.");
	}

	@Override
	protected void zadajIznos() {
		System.out.println("Izgovaramo iznos službeniku.");
	}

	@Override
	protected void podigniNovac() {
		System.out.println("Podižemo novac sa saltera.");
	}

}
