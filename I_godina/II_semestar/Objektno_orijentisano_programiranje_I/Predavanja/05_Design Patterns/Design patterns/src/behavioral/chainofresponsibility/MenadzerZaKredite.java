package behavioral.chainofresponsibility;

public class MenadzerZaKredite implements MozeDaPotpise {
	MozeDaPotpise sef;
	String potpis;
	
	public MenadzerZaKredite(MozeDaPotpise sef) {
		this.sef = sef;
		this.potpis = "Menadzer za kredite";
	}

	@Override
	public void potpisi(Zahtev z) {
		z.potpisi(potpis);
		sef.potpisi(z);
	}
	
	
}
