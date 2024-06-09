package behavioral.visitor;

public class VisitorPotrosnje implements Visitor {
	double total;
	
	public VisitorPotrosnje() {
		total = 0;
	}
	
	@Override
	public void visit(HardverskiElement e) {
		total += e.potrosnja();
	}

	@Override
	public double getTotal() {
		return total;
	}

}
