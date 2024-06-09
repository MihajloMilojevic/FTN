package behavioral.iterator;

public class IteratorAutomobila implements Iterator {
	
	private NizAutomobila nizAutomobila;
	private int trenutnaPozicija;

	public IteratorAutomobila(NizAutomobila niz) {
		this.nizAutomobila = niz;
		this.trenutnaPozicija = 0;
	}
	
	@Override
	public void first() {
		trenutnaPozicija = 0;
	}

	@Override
	public void next() {
		if (trenutnaPozicija < nizAutomobila.trenutnoUnutra)
			trenutnaPozicija++;
	}

	@Override
	public boolean isDone() {
		if (trenutnaPozicija < nizAutomobila.trenutnoUnutra)
			return false;
		else
			return true;
	}

	@Override
	public Automobil current() {
		return nizAutomobila.niz[trenutnaPozicija];
	}

}
