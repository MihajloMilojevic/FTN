package trgovinska_radnja;

import java.util.Scanner;

public class App {

	static Scanner scanner = new Scanner(System.in);
    static int brojArtikala = 0;
    static String[][] artikli;
    static int[][] kolicine;
    
	public static void main(String[] args) {
        System.out.println("Aplikacija za evidentiranje artikala u trgovinskoj radnji");
        boolean exit = false;
        artikli = new String[50][2];
        kolicine = new int[50][3];
        
        do {
        	
        	System.out.println("=============== Meni ===============");
        	System.out.println("0. Izlazak");
        	System.out.println("1. Unos artikla");
        	System.out.println("2. Unos kolicina u magacine");
        	System.out.println("3. Ispis kolicina iz magacina");
        	System.out.println("4. Prosecne kolicine iz magacina");
        	System.out.println("====================================");
        	
        	int odabraniBroj = scanner.nextInt();
        	scanner.nextLine();
        	
        	switch (odabraniBroj) {
        		case 0:
        			exit = true;
        			System.out.println("Izlazak iz aplikacije");
        			break;
        		case 1:
        			dodajArtikal();
        			break;
        		case 2:
        			dodajKolicinuUMagacine();
        			break;
        		case 3:
        			ispisKolicinaIzMagacina();
        			break;
        		case 4:
        			ispisProsecneKolicine();
        			break;
        		default:
        			System.out.println("Odabrali ste nepostojecu opciju. Pokusajte ponovo.");
        		
        	}
        	
        } while (!exit);
        
        scanner.close();
        
	}
	
	static void dodajArtikal() {
		System.out.println("Unesi podatke o artiklu u formatu [šifra;naziv]: ");
		String[] podaci = scanner.nextLine().split(";");
		
		artikli[brojArtikala++] = podaci;
		
		System.out.printf("Uspesno dodat artikal %s %s.\n", podaci[0], podaci[1]);
	}
	
	static void dodajKolicinuUMagacine() {
		System.out.println("Unesi sifru artikla: ");
		String sifra = scanner.nextLine();
		int index = -1;
		
		for (int i=0; i<brojArtikala; i++) {
			if (artikli[i][0].equals(sifra)) {
				index = i;
				break;
			}
		}
		
		if (index != -1) {
			
			System.out.println("Unesite kolicine za svaki od magacina odvojene razmakom:");
			int kolicina1 = scanner.nextInt();
			int kolicina2 = scanner.nextInt();
			int kolicina3 = scanner.nextInt();
		
			int[] kolicineArtikla = {kolicina1, kolicina2, kolicina3};
			kolicine[index] = kolicineArtikla;
		} else {
			System.out.println("Trazeni artikal ne postoji");
		}
	}
	
	static void ispisKolicinaIzMagacina() {
		System.out.println("Unesi sifru artikla: ");
		String sifra = scanner.nextLine();
		int index = -1;
		
		for (int i=0; i<brojArtikala; i++) {
			if (artikli[i][0].equals(sifra)) {
				index = i;
				break;
			}
		}
		
		if (index != -1) {
			int[] kolicineArtikla = kolicine[index];
			String[] podaciOArtiklu = artikli[index];
			System.out.printf("Artikal %s %s se u magacinima nalazi u količinama %d, %d i %d.\n", podaciOArtiklu[0], podaciOArtiklu[1], 
						kolicineArtikla[0], kolicineArtikla[1], kolicineArtikla[2]);
		} else {
			System.out.println("Trazeni artikal ne postoji");
		}
	}
	
	static void ispisProsecneKolicine() {

		for (int i=0; i<brojArtikala; i++) {
			String[] podaciOArtiklu = artikli[i];
			int[] kolicineArtikla = kolicine[i];
			double prosek = ((double)kolicineArtikla[0] + kolicineArtikla[1] + kolicineArtikla[2])/3;
			
			System.out.printf("Artikal %s %s se u magacinima nalazi u prosečnoj količini %.2f.\n", podaciOArtiklu[0], podaciOArtiklu[1], 
					prosek);
		}
	}
	
	
	
}
