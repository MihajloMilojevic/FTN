package structural.decorator;

public class BorderDecorator extends GUIComponent {
	
	GUIComponent component;

	public BorderDecorator(GUIComponent component, String name) {
		this.component = component;
		this.name = name;
	}
	
	
	@Override
	public void draw() {
		System.out.println("BorderDecorator: Dodajem okvir oko " + component.getName() + " component");
		component.draw();
	}

}
