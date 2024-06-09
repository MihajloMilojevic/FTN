package behavioral.state;

public class Semafor {
	SemaforState tekuceStanje;
	public Semafor() {
		tekuceStanje = TrepcuceZuto.getInstance();
	}
	
	public void ukljuci() {
		sleep();
		tekuceStanje = tekuceStanje.ukljucio();
		sleep();
		for (int i = 0; i < 10; i++) {
			tekuceStanje = tekuceStanje.tajmerSeAktivirao();
			sleep();
		}
		tekuceStanje = tekuceStanje.iskljucio();
		sleep();
	}

	@SuppressWarnings("static-access")
	private void sleep() {
		tekuceStanje.ispisStanja();
		try {
			Thread.currentThread().sleep(1000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
	}
}
