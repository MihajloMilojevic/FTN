package behavioral.obsever;

public class Test {

	public static void main(String[] args) {
		Timer timer = new Timer();
		Clock clock1 = new Clock();
		EvenClock clock2 = new EvenClock();
		timer.register(clock1);
		timer.register(clock2);
		timer.start();
	}

}
