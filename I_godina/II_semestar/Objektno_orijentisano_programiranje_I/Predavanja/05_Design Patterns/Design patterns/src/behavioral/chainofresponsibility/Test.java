package behavioral.chainofresponsibility;

public class Test {

	public static void main(String[] args) {
		DirektorFilijale direktor = new DirektorFilijale(null);
		MenadzerZaKredite menadzer = new MenadzerZaKredite(direktor);
		Zahtev zahtev = new Zahtev();
		
		menadzer.potpisi(zahtev);
		
		System.out.println(zahtev);
	}
}
