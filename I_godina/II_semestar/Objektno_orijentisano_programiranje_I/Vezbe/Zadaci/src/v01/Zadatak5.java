package v01;

import java.util.Scanner;

public class Zadatak5 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Unesite duzinu: ");
		int a = sc.nextInt();
		System.out.print("Unesite sirinu: ");
		int b = sc.nextInt();
		System.out.print("Unesite visinu: ");
		int c = sc.nextInt();
		sc.close();
		int povrsina = 2 * (a * b + a * c + b * c);
		int zapremina = a * b *c;
		System.out.printf(
				"Kvadar duzine %d, sirine %d i visine %d ima povrsinu %d i zapreminu %d", 
				a, b, c, povrsina, zapremina
			);
	}

}
