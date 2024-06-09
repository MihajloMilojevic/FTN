package creational.builder;

public class BurekSaMesomBuilder extends BurekBuilder {

	@Override
	public void postaviIme() {
		burek.setIme("Burek sa mesom");
	}

	@Override
	public void napraviTesto() {
		burek.setTesto("normalno");
	}

	@Override
	public void napraviFil() {
		burek.setFil("meso");
	}

}
