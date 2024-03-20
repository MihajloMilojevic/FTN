package v01;

import java.util.Scanner;

public class Zadatak4 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Unesite duzinu u centimetrima: ");
		int unosCM = sc.nextInt();
		
		sc.close();
		int metri = unosCM / 100;
		int decimetri = (unosCM % 100) / 10;
		int centimetri = unosCM % 10;
		System.out.printf("Duzina od %dcm je %dm %ddm %dcm", unosCM, metri, decimetri, centimetri);
	}

}
