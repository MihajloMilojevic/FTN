package behavioral.state;

public abstract class SemaforState {

	/** Kada se aktivira tajmer, vraća novo stanje. */
	public abstract SemaforState tajmerSeAktivirao();

	/**
	 * Ako se uključio u ovom stanju, vraća novo stanje.
	 */
	public abstract SemaforState ukljucio();

	/**
	 * Ako se u bilo kom stanju iskljuci, prelazi u trepcuce zuto.
	 */
	public SemaforState iskljucio() {
		return TrepcuceZuto.getInstance();
	}

	public abstract void ispisStanja();
}
