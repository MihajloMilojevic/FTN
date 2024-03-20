package v01;

import java.util.Scanner;

public class Zadatak7 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Unesite vrednost x:");
		double x = scanner.nextDouble();
		System.out.print("Unesite vrednost y:");
		double y = scanner.nextDouble();
		scanner.close();
		double z = 0;
		if (x < y) {
			z = Math.max(x, y) / (1 + Math.abs(Math.min(x, y)));
		} else {
			z = Math.max(x, y) / (1 + Math.min(x, y));
		}
		System.out.printf("f(%.2f, %.2f) = %.2f", x, y, z);
	}

}
