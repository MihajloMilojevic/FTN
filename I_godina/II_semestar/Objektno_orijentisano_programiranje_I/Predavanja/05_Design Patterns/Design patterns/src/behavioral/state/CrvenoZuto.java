package behavioral.state;

public class CrvenoZuto extends SemaforState {

	private static CrvenoZuto instance = null;

	public static CrvenoZuto getInstance() {
		if (instance == null)
			instance = new CrvenoZuto();
		return instance;
	}

	private CrvenoZuto() {
	}

	@Override
	public SemaforState  tajmerSeAktivirao() {
		// sledece stanje je zeleno
		return Zeleno.getInstance();
	}

	@Override
	public SemaforState ukljucio() {
		return this;
	}

	@Override
	public void ispisStanja() {
		System.out.println("CRVENO I ZUTO");
	}

}
