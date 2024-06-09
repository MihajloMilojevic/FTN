package structural.decorator;

public abstract class GUIComponent {
	protected String name;
	public String getName() {
		return name;
	}
	public abstract void draw();
}
