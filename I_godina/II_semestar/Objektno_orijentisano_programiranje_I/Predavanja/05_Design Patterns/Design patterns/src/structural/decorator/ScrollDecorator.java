package structural.decorator;

public class ScrollDecorator extends GUIComponent {

	GUIComponent component;

	public ScrollDecorator(GUIComponent component, String name) {
		this.component = component;
		this.name = name;
	}
	
	@Override
	public void draw() {
		System.out.println("ScrollDecorator: Crtam scroll bar oko " + component.getName() + " komponente.");
		component.draw();
	}

}
