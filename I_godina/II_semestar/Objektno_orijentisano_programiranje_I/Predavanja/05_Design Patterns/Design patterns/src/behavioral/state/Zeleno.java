package behavioral.state;

public class Zeleno extends SemaforState {

	private static Zeleno instance = null;

	public static Zeleno getInstance() {
		if (instance == null)
			instance = new Zeleno();
		return instance;
	}

	private Zeleno() {
	}

	@Override
	public SemaforState tajmerSeAktivirao() {
		// sledece stanje je trepćuće zeleno
		return TrepcuceZeleno.getInstance();
	}

	@Override
	public SemaforState ukljucio() {
		return this;
	}


	@Override
	public void ispisStanja() {
		System.out.println("ZELENO");
	}

}
