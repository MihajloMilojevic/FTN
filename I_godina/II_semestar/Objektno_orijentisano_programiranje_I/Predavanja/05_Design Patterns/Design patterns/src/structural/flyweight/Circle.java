package structural.flyweight;

public class Circle {
	String color;
	
	public Circle(String color) {
		this.color = color;
		System.out.println("Napravili krug sa bojom: " + color);
	}
	public void draw() {
	}
}
