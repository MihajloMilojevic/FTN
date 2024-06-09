package behavioral.obsever;

public class EvenClock implements Observer {

	@Override
	public void update(int newState) {
		if (newState % 2 == 0) {
			System.out.println("EvenClock: " + newState);
		}

	}

}
