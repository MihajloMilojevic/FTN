package structural.decorator;

public class Test {

	public static void main(String[] args) {
		ListBox lb = new ListBox("ListBox");
		ScrollDecorator scrollDecorator = new ScrollDecorator(lb, "ScrollDecorator");
		BorderDecorator borderDecorator = new BorderDecorator(scrollDecorator, "BorderDecorator");
		
		borderDecorator.draw();
	}

}
