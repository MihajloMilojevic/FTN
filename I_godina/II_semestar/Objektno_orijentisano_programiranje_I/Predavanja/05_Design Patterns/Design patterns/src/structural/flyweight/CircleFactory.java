package structural.flyweight;

import java.util.HashMap;
import java.util.Map;

public class CircleFactory {
	Map<String, Circle> circleMap; 
	
	public CircleFactory() {
		circleMap = new HashMap<String, Circle>();
	}
	public Circle getCircle(String color) {
		Circle circle = circleMap.get(color);
		if (circle == null) {
			circle = new Circle(color);
			circleMap.put(color, circle);
		}
		return circle;
	}
}
