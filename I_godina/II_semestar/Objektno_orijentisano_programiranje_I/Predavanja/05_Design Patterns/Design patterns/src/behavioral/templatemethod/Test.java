package behavioral.templatemethod;

public class Test {

	public static void main(String[] args) {
		PodizanjeNovcaTemplate bankomat = new Bankomat();
		bankomat.operacijaPodizanjaNovca();
		System.out.println("============================================");
		PodizanjeNovcaTemplate salter = new SalterUBanci();
		salter.operacijaPodizanjaNovca();
	}

}
