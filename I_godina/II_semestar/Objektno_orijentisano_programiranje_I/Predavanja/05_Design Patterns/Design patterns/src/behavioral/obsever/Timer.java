package behavioral.obsever;

import java.util.ArrayList;
import java.util.List;

public class Timer implements Observable {
	
	List <Observer> observers;
	
	public Timer() {
		observers = new ArrayList<Observer>();
	}
	
	@Override
	public void register(Observer observer) {
		observers.add(observer);
	}

	@Override
	public void unregister(Observer observer) {
		observers.remove(observer);
	}


	@SuppressWarnings("static-access")
	public void start() {
		int seconds = 0;
		while(true) {
			try {
				Thread.currentThread().sleep(1000);
				seconds++;
				for (Observer o : observers) 
					o.update(seconds);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}
