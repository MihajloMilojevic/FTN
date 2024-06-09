package structural.composite;

import java.io.File;

public class CountFiles {

	public static void main(String[] args) {
		int c = count(new File("C:\\Temp"));
		System.out.println("Broj fajlova je: " + c);
	}

	private static int count(File file) {
		if (file.isFile()) 
			return 1;
		File[] files = file.listFiles();
		int ret = 0;
		for(File f : files) {
			ret += count(f);
		}
 		return ret;
	}

}
