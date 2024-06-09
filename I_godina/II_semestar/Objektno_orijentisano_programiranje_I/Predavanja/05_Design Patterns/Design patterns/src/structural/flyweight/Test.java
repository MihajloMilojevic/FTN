package structural.flyweight;

public class Test {

	public static void main(String[] args) {
		String[] circleColors = {"Red", "Green", "Blue", "White", "Black", "Yellow"};
		System.out.println("Bez flyweight šablona");
		for (int i = 0; i < 1000; i++) {
			Circle c = new Circle(circleColors[(int)(Math.random()*5)]);
			c.draw();
		}

		System.out.println("Sa flyweight šablonom");
		CircleFactory circleFactory = new CircleFactory();
		for (int i = 0; i < 1000; i++) {
			Circle c = circleFactory.getCircle(circleColors[(int)(Math.random()*5)]);
			c.draw();
		}
	
	}

}
