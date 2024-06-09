package behavioral.state;

public class TrepcuceZeleno extends SemaforState {

	private static TrepcuceZeleno instance = null;

	public static TrepcuceZeleno getInstance() {
		if (instance == null)
			instance = new TrepcuceZeleno();
		return instance;
	}

	private TrepcuceZeleno() {
	}

	@Override
	public SemaforState tajmerSeAktivirao() {
		// sledece stanje je žuto
		return Zuto.getInstance();
	}

	@Override
	public SemaforState ukljucio() {
		return this;
	}

	@Override
	public void ispisStanja() {
		System.out.println("TREPCUCE ZELENO");
	}

}
