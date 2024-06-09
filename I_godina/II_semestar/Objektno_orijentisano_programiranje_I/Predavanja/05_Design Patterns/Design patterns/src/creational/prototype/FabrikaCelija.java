package creational.prototype;

public class FabrikaCelija {
	private Celija original;
	
	public FabrikaCelija() {
		original = new Celija();
		System.out.println("Fabrika celija, original: " + original);
	}
	public Celija napraviCelijuShallow() {
		return (Celija)original.clone();
	}

	public Celija napraviCelijuDeep() {
		return original.deepClone();
	}
	public void promeniVelicinuJezgra(int velicina) {
		original.jezgro.velicina = velicina;
	}
	
	public Celija getOriginal() {
		return original;
	}
}
