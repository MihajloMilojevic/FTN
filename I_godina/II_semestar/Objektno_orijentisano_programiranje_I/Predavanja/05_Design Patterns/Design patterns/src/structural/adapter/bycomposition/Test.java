package structural.adapter.bycomposition;

public class Test {

	public static void main(String[] args) {
		Racunar racunar = new Racunar();
		PS2Tastatura ps2tastatura = new PS2Tastatura();
		
		racunar.tastatura = new PS2ToUsbAdapter(ps2tastatura);

		racunar.testTastature();
		
	}

}
