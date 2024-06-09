package behavioral.memento.inverzno;


public class Memento {

	int state;

	public Memento(int state) {
		this.state = state;
	}
	
	public void setState(int state) {
		this.state = state;
		
	}
	
	public int getState() {
		return state;
	}
	
	public String toString() {
		return "Dodat red broj: " + state ;
	}
}
