package v01;

public class Zadatak2 {

	public static void main(String[] args) {
		double povrsinaKvadrata = 16;
		double osnovicaTrougla = 4;
		double krakTrougla = 6;
		
		
		double stranicaKvadrata = Math.sqrt(povrsinaKvadrata);
		double visinaTrouglaA = Math.sqrt(Math.pow(krakTrougla, 2) + (Math.pow(osnovicaTrougla, 2)/4));
		double povrsinaTrougla = osnovicaTrougla / 2 * visinaTrouglaA;
		
		System.out.printf("Stranica kvadrata: %.2f\n", stranicaKvadrata);
		System.out.printf("Povrsina trougla: %.2f\n", povrsinaTrougla);
	}

}
