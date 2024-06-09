package behavioral.memento;

import java.util.ArrayList;
import java.util.List;

public class Memento {

	List <String> state;

	public Memento(List <String> state) {
		this.state = new ArrayList<String>(state);
	}
	
	public void setState(List <String> state) {
		this.state = state;
		
	}
	
	public List<String> getState() {
		return state;
	}
	
	public String toString() {
		String retVal = "Size: " + state.size() + ", content: ";
		StringBuilder sb = new StringBuilder(retVal);
		for (String s : state) {
			sb.append(s);
			sb.append(" ");
		}
		return sb.toString();
	}
}
