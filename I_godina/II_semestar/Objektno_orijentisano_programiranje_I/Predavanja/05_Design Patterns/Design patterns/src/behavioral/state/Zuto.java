package behavioral.state;

public class Zuto extends SemaforState {

	private static Zuto instance = null;
	public static Zuto getInstance() {
		if (instance == null) 
			instance = new Zuto();
		return instance;
	}
	
	private Zuto() {
	}
	
	@Override
	public SemaforState tajmerSeAktivirao() {
		// sledece stanje je crveno 
		return Crveno.getInstance();
	}

	@Override
	public SemaforState ukljucio() {
		return this;
	}

	@Override
	public void ispisStanja() {
		System.out.println("ZUTO");
	}

}
