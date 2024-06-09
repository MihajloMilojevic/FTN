package creational.builder;

public class BurekSaSiromBuilder extends BurekBuilder {
	
	@Override
	public void postaviIme() {
		burek.setIme("Burek sa sirom");
	}
	
	@Override
	public void napraviTesto() {
		burek.setTesto("normalno");
	}

	@Override
	public void napraviFil() {
		burek.setFil("sir");
	}
}
