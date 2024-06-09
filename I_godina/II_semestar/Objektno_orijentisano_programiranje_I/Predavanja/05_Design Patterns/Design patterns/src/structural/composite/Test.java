package structural.composite;

public class Test {

	/**
	 * TEST:
	 * dir1  
	 *       --> abc.txt
	 *       --> dir2
	 *       		  --> abc.txt
	 *                --> abcd.txt
	 *                --> dir3
	 *       		  		  --> abc.txt
	 *                        --> abcd.txt
	 *                        --> abcdef.txt     
	 */
	public static void main(String[] args) {
		FileSystemItem abc    = new FileItem("abc.txt");
		FileSystemItem abcd   = new FileItem("abcd.txt");
		FileSystemItem abcdef = new FileItem("abcdef.txt");
		
		FileSystemItem dir1 = new DirectoryItem("dir1");
		FileSystemItem dir2 = new DirectoryItem("dir2");
		FileSystemItem dir3 = new DirectoryItem("dir3");
		
		dir1.add(abc);
		dir1.add(dir2);
		dir2.add(abc);
		dir2.add(dir3);
		dir2.add(abcd);
		dir3.add(abc);
		dir3.add(abcd);
		dir3.add(abcdef);
		
		printComposite(dir1);
		
	}
	
	private static String indent = "";
	
	private static void printComposite(FileSystemItem item) {
		if (item.isFile()) {
			// file
			System.out.println(indent + item.getName());
		} else {
			// folder (directory)
			System.out.println(indent + "<" + item.getName() + ">");
			increaseIndent();
			/*
			for (FileSystemItem i : item.getList()) {
				printComposite(i);
			}
			*/
			for (FileSystemItem i : item.getList()) {
				if (i.isFile())
					printComposite(i);
			}
			for (FileSystemItem i : item.getList()) {
				if (!i.isFile())
					printComposite(i);
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
