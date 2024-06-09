package structural.proxyoverkill;

import java.io.Serializable;

public class Auto implements Serializable {
	private static final long serialVersionUID = 1684788985105186719L;
	
	public boolean radi;

	@Override
	public String toString() {
		return "Auto [radi=" + radi + "]";
	}
	
	
}
