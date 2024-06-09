package behavioral.templatemethod;

public class Bankomat extends PodizanjeNovcaTemplate {

	@Override
	protected void identifikujSe() {
		System.out.println("Ubacujemo karticu u bankomat i unosimo PIN kod.");
	}

	@Override
	protected void zadajIznos() {
		System.out.println("Unosimo iznos preko tastature.");
	}

	@Override
	protected void podigniNovac() {
		System.out.println("Podizemo novac sa bankomata.");
	}

}
