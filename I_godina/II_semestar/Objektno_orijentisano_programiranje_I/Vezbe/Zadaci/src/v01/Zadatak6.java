package v01;

public class Zadatak6 {

	public static void main(String[] args) {
		double r = 6;
		double H = 4;

		double s = Math.sqrt(Math.pow(H, 2) + Math.pow(r / 2, 2));
		double povrsina = r * Math.PI * (s + r);
		System.out.printf("Kupa poluprecnika %.2f i visine %.2f im povrsinu %.2f", r, H, povrsina);
	}

}
