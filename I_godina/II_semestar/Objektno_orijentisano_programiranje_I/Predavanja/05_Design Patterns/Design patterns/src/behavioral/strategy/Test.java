package behavioral.strategy;

public class Test {

	public static void main(String[] args) {
		String text = "danas sam naucio Javu";
		String key = "0";
		EncryptStrategy caesar = new CaesarStrategy();
		char[]  encrypted = caesar.encrypt(text, key);
		System.out.print("Caesar kriptovano:");
		printCharArray(encrypted);
		String decrypted = caesar.decrypt(encrypted, key);
		System.out.println("Caesar dekrtiptovano: " + decrypted);
		
		EncryptStrategy xor = new XorStrategy();
		encrypted = xor.encrypt(text, key);
		System.out.print("Xor kriptovano:");
		printCharArray(encrypted);
		decrypted = xor.decrypt(encrypted, key);
		System.out.println("Xor dekriptovano: " + decrypted);
	}
	
	private static void printCharArray(char[] array) {
		for (char c : array)
			System.out.print(c);
		System.out.println();
	}

}
