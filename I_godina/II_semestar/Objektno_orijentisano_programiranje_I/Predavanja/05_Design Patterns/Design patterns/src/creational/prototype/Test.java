package creational.prototype;

public class Test {

	public static void main(String[] args) {
		FabrikaCelija fabrika = new FabrikaCelija();
		Celija celijaShallow  = fabrika.napraviCelijuShallow();
		Celija celijaDeep     = fabrika.napraviCelijuDeep();  

		System.out.println("Original: " + fabrika.getOriginal());
		System.out.println("Shallow: " + celijaShallow);
		System.out.println("Deep: " + celijaDeep);

		// provera deep i shallow kopiranja
		fabrika.promeniVelicinuJezgra(10);
		
		System.out.println("Original: " + fabrika.getOriginal());
		System.out.println("Shallow: " + celijaShallow);
		System.out.println("Deep: " + celijaDeep);
	}

}
