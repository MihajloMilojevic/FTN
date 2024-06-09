package creational.singleton;

public class Singleton {
	private Singleton() {
		
	}
	
	private static Singleton instance = null;
	
	public static Singleton getInstance() {
		if (instance == null) {
			instance = new Singleton();
		}
		return instance;
	}

	public void hello() {
		System.out.println("Hello from singleton! " + this);
	}
}
