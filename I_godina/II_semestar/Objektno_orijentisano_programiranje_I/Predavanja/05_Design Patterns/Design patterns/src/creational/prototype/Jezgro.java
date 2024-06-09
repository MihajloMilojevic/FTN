package creational.prototype;

public class Jezgro implements Cloneable {
	int velicina;
	
	public Jezgro() {
		velicina = 5;
	}
	
	@Override
	public Object clone() {
		try {
			return super.clone();
		} catch (CloneNotSupportedException e) {
			e.printStackTrace();
			throw new Error("Ovo ne bi smelo da se dogodi.");
		}
		
	}
}
