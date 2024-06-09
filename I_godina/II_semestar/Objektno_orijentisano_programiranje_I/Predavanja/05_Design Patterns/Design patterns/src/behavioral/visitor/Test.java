package behavioral.visitor;


public class Test {

	public static void main(String[] args) {
		HardverskiElement ploca    = new MaticnaPloca();
		HardverskiElement procesor = new Procesor();
		
		Visitor vCena           = new VisitorCena();
		Visitor vPotrosnje      = new VisitorPotrosnje();
		
		ploca.accept(vPotrosnje);
		procesor.accept(vPotrosnje);
		System.out.println("Ukupna potrosnja: " + vPotrosnje.getTotal());
		
		ploca.accept(vCena);
		procesor.accept(vCena);
		System.out.println("Ukupna cena: " + vCena.getTotal());
	}

}
