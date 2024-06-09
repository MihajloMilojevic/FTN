package behavioral.iterator;

public class Automobil {
	public String marka;
	public String model;
	public Automobil(String marka, String model) {
		this.marka = marka;
		this.model = model;
	}
	
	public String toString() {
		return marka + " " + model;
	}
}
