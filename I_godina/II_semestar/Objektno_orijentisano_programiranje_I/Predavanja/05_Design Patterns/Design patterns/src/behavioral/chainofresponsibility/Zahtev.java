package behavioral.chainofresponsibility;

import java.util.ArrayList;
import java.util.List;

public class Zahtev {

	List<String> potpisi;
	
	public Zahtev() {
		potpisi = new ArrayList<String>();
	}
	
	public void potpisi(String potpis) {
		potpisi.add(potpis);
	}
	
	public String toString() {
		StringBuilder sb = new StringBuilder(10000);
		sb.append("Zahtev potpisali: ");
		for (String s : potpisi) {
			sb.append(s);
			sb.append("\n");
		}
		return sb.toString();
	}
}
