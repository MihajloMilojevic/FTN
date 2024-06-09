package behavioral.state;

public class Crveno extends SemaforState {

	private static Crveno instance = null;
	public static Crveno getInstance() {
		if (instance == null) 
			instance = new Crveno();
		return instance;
	}
	
	private Crveno() {
	}
	
	@Override
	public SemaforState tajmerSeAktivirao() {
		// sledece stanje je crveno i zuto
		return CrvenoZuto.getInstance();
	}

	@Override
	public SemaforState  ukljucio() {
		return this;
	}

	@Override
	public void ispisStanja() {
		System.out.println("CRVENO");
	}
	

}
