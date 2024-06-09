package behavioral.templatemethod;

public abstract class PodizanjeNovcaTemplate {
	protected abstract void identifikujSe();
	protected abstract void zadajIznos();
	protected abstract void podigniNovac();
	
	public void operacijaPodizanjaNovca() {
		identifikujSe();
		zadajIznos();
		podigniNovac();
	}
}
