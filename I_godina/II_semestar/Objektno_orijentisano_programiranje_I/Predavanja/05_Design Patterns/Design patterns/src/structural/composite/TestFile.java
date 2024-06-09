package structural.composite;

import java.io.File;

public class TestFile {

	public static void main(String[] args) {
		printFile(new File("C:/Temp"));
	}

	private static String indent = "";

	private static void printFile(File file) {
		if (file.isFile())
			System.out.println(indent + file.getName());
		else {
			System.out.println(indent + "<" + file.getName() + ">");
			increaseIndent();
//			for (File f : file.listFiles()) {
//				printFile(f);
//			}
			for (File f : file.listFiles()) {
				if (f.isFile())
					printFile(f);
			}
			for (File f : file.listFiles()) {
				if (f.isDirectory())
					printFile(f);
			}
			decreaseIndent();
		}
	}

	private static void increaseIndent() {
		indent += "  ";
	}
	private static void decreaseIndent() {
		indent = indent.substring(0, indent.length() - 2);
	}
}
