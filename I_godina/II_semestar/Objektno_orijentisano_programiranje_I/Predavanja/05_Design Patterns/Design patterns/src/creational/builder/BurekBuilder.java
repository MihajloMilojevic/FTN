package creational.builder;

public abstract class BurekBuilder {
	protected Burek burek;

	public Burek napraviBurek() {
		burek = new Burek();
		napraviTesto();
		napraviFil();
		postaviIme();
		return burek;
	}
	public abstract void postaviIme();
	
	public abstract void napraviTesto();

	public abstract void napraviFil();
}
