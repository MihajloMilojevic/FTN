package kt1;

import java.util.Scanner;

public class VezbaKT1 {
	
	static Scanner scanner = new Scanner(System.in);
	static String[][] artikli = new String[50][2];
	static int[][] kolicine = new int[50][3];
	static int brojArtikala = 0;

	static void unosArtikla() {
		System.out.println("unesi podatke o artiklu u formatu [šifra;naziv]: ");
		String unos = scanner.nextLine();
		String[] podaciOArtiklu = unos.split(";");
		artikli[brojArtikala] = podaciOArtiklu;
		brojArtikala++;
		System.out.printf("Uspesno dodat artikal %s %s\n", 
				podaciOArtiklu[0], podaciOArtiklu[1]);
		
	}
	
	static void dodavanjeKolicineUMagacin() {
		System.out.println("Unesite sifru artikla:");
		String sifra = scanner.nextLine();
		boolean pronadjeno = false;
		
		for (int i=0; i<brojArtikala; i++) {
			if (sifra.equals(artikli[i][0])) {
				System.out.println("Unesi količine artikla "
						+ "u magacinima u formatu [količina1 količina2 količina3]:");
				int kolicina1 = scanner.nextInt();
				int kolicina2 = scanner.nextInt();
				int kolicina3 = scanner.nextInt();
				scanner.nextLine();
				
				kolicine[i][0] = kolicina1;
				kolicine[i][1] = kolicina2;
				kolicine[i][2] = kolicina3;
				
				pronadjeno = true;
				break;		
			}
		}
			
		if (!pronadjeno) {
			System.out.println("Nema trazenog artikla");
		}
		
		
	}
	
	public static void main(String[] args) {
		
		String answer;
		
		do {
			System.out.println("=== Meni ===");
			System.out.println("1. Unos artikla");
			System.out.println("2. Dodavanje kolicine u magacin");
			System.out.println("x. Izlaz");
			System.out.println("Odaberite opciju:");
			
			answer = scanner.nextLine();
			
			switch (answer) {
				case "1": 
					unosArtikla();
					break;
				case "2": 
					dodavanjeKolicineUMagacin();
					break;				
				case "x": 
					System.out.println("Dovidjenja!");
					break;
				default:
					System.out.println("Uneli ste nepostojecu opciju.");
			}
			
			
		} while (!answer.equals("x"));
		
		scanner.close();
	}

}
