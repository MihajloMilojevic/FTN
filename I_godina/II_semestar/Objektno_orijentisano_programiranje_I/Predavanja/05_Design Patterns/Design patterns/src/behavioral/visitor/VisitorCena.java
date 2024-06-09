package behavioral.visitor;

public class VisitorCena implements Visitor {
	double total;
	
	public VisitorCena() {
		total = 0;
	}
	
	@Override
	public void visit(HardverskiElement e) {
		total += e.cena();
	}

	@Override
	public double getTotal() {
		return total;
	}
	
}
