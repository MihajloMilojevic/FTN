package behavioral.state;

public class TrepcuceZuto extends SemaforState {

	private static TrepcuceZuto instance = null;

	public static TrepcuceZuto getInstance() {
		if (instance == null)
			instance = new TrepcuceZuto();
		return instance;
	}

	private TrepcuceZuto() {
	}

	@Override
	public SemaforState tajmerSeAktivirao() {
		// sledece stanje je zeleno
		return Zeleno.getInstance();
	}

	@Override
	public SemaforState ukljucio() {
		return Zeleno.getInstance();
	}

	@Override
	public void ispisStanja() {
		System.out.println("TREPCUCE ZUTO");
	}

}
