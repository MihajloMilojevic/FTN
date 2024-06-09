package structural.adapter.byinheritance;

public class Test {

	public static void main(String[] args) {
		Racunar racunar = new Racunar();

		racunar.tastatura = new PS2ToUsbAdapter();

		racunar.testTastature();
		
	}

}
