package structural.decorator;

public class ListBox extends GUIComponent {
	
	public ListBox(String name) {
		this.name = name;
	}
	@Override
	public void draw() {
		System.out.println("ListBox draw()");
	}

}
