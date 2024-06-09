package creational.builder;

public class Test {

	public static void main(String[] args) {
		BurekBuilder burekSaSiromBuilder = new BurekSaSiromBuilder();
		Burek burek = burekSaSiromBuilder.napraviBurek();
		System.out.println(burek);

		BurekBuilder burekSaMesomBuilder = new BurekSaMesomBuilder();
		burek = burekSaMesomBuilder.napraviBurek();
		System.out.println(burek);
	}

}
