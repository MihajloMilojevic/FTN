package utils;

import java.io.File;
import java.io.IOException;


public class FileChecker {

	public static File getFile(String path) {
		File f = new File(path);
		if (!f.exists()) {
			try {
				File parent = f.getParentFile();
				if(parent != null && !parent.exists()) {
					parent.mkdirs();
				}
				f.createNewFile();
			} catch (IOException e) {
				System.err.println(e.getMessage());
				e.printStackTrace();
			}
		}
		return f;
	}

}
