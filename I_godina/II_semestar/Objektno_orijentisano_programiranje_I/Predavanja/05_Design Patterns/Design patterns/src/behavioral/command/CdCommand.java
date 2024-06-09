package behavioral.command;

import java.io.File;
import java.io.IOException;

public class CdCommand extends Command {

	public CdCommand(String param) {
		this.parameters.add(param);
	}
	
	@Override
	public boolean execute() {
		String path = parameters.get(0);
		if (path.equals("")) {
			try {
				System.out.println(currentDir.getCanonicalPath());
			} catch (IOException e) {
				e.printStackTrace();
			}
			return true;
		}
		File f = new File(currentDir, path);
		if (f.exists()) {
			if (f.isDirectory()) {
				currentDir = f;
			} else {
				System.out.println("This is not a folder: " + path);
			}
		} else {
			System.out.println("Folder " + path + " does not exist!");
		}
		return true;
	}


}
