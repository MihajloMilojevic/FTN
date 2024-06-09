package structural.facade;

public class Test {
	Racunar racunar;
	public Test() {
		racunar = new Racunar();
		racunar.start();
	}
	
	public static void main(String args[]) {
		new Test();
	}
}
