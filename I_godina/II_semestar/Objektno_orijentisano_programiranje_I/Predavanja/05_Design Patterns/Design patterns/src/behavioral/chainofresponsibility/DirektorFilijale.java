package behavioral.chainofresponsibility;

public class DirektorFilijale implements MozeDaPotpise {

	MozeDaPotpise sef;
	String potpis;
	
	public DirektorFilijale(MozeDaPotpise sef) {
		this.sef = sef;
		this.potpis = "Direktor filijale";
	}

	@Override
	public void potpisi(Zahtev z) {
		z.potpisi(potpis);
	}

}
