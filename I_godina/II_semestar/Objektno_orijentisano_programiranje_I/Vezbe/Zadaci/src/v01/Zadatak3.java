package v01;

import java.util.Scanner;

public class Zadatak3 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Unesite godinu: ");
		int godina = sc.nextInt();
		sc.close();
		if(godina % 400 == 0 || (godina % 100 != 0 && godina % 4 == 0))
			System.out.printf("Godina %d jeste prestupna", godina);
		else
			System.out.printf("Godina %d nije prestupna", godina);
	}

}
