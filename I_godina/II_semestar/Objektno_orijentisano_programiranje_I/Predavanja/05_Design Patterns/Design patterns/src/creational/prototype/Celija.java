package creational.prototype;

public class Celija implements Cloneable {
	Jezgro jezgro;
	
	public Celija() {
		jezgro = new Jezgro();
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
	
	public Celija deepClone() {
		Celija kopija = (Celija)clone();
		kopija.jezgro = (Jezgro)jezgro.clone();
		return kopija;
	}
	
	@Override
	public String toString() {
		return "Celija (" + this.hashCode() + "), sa jezgrom velicine: " + jezgro.velicina + ", hashCode jezgra: " + jezgro.hashCode();
	}
}
