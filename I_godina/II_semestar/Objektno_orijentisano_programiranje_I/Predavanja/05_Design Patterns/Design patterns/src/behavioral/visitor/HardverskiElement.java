package behavioral.visitor;

public abstract class HardverskiElement {
	public abstract double potrosnja();
	public abstract double cena();
	
	public void accept(Visitor visitor) {
		visitor.visit(this);
	}

}
