package v01;

import java.util.Scanner;

public class Zadatak8 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Unesi koeficijente kvadratne jednacine ax\u00B2 + bx + c = 0");
		System.out.print("Unesite vrednost a: ");
		double a = scanner.nextDouble();
		System.out.print("Unesite vrednost b: ");
		double b = scanner.nextDouble();
		System.out.print("Unesite vrednost c: ");
		double c = scanner.nextDouble();
		scanner.close();

		System.out.print("Uneta je jednacina: ");
		if (a != 0) {
			System.out.printf("%.2fx\u00B2 ", a);
		}
		if (b != 0) {
			System.out.printf("%+.2fx ", b);
		}
		if (c != 0) {
			System.out.printf("%+.2f ", c);
		}

		if (a == 0 && b == 0 && c == 0) { // ako su svi nula treba da dobijemo 0 = 0
			System.out.print("0 ");
		}
		System.out.println("= 0");
		double det = Math.pow(b, 2) - 4 * a * c;
		if (a == 0 && b == 0 && c == 0) {
			System.out.printf("Jednacina ima beskonacno mnogo resenja (x\u2208\u211D)");
		} else if (a == 0 && b == 0) {
			System.out.printf("Jednacina uopste nema resenja (x\u2208\u2205)");
		} else if (a == 0) {
			System.out.printf("Jednacina ima jedno resenje (x = %.2f)", -c / b);
		} else if (det < 0) {
			System.out.printf("Jednacina nema realnih resenja (x\u2208\u2205)");
		} else if (det == 0) {
			System.out.printf("Jednacina ima jedno resenje (x = %.2f)", (-b) / (2 * a));
		} else {
			double x1 = (-b - Math.sqrt(det)) / (2 * a);
			double x2 = (-b + Math.sqrt(det)) / (2 * a);
			System.out.printf("Jednacina ima dva resenja (x\u2208{%.2f;%.2f})", x1, x2);
		}
	}

}
