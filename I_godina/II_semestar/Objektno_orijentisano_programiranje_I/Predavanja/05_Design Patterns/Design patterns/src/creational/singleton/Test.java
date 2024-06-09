package creational.singleton;

public class Test {

	public static void main(String[] args) {
		Singleton s1 = Singleton.getInstance();
		s1.hello();
		
		Singleton s2 = Singleton.getInstance();
		s2.hello();
		
		//Singleton s = new Singleton();
		
		System.out.println(s1 == s2);
		
		class Pera {
			
		}
		Pera p1 = new Pera();
		System.out.println("pera1: " + p1);
		Pera p2 = new Pera();
		System.out.println("pera2: " + p2);
		System.out.println(p1 == p2);
	}

}

