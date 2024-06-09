package behavioral.command;

import java.io.File;

public class DirCommand extends Command {

	@Override
	public boolean execute() {
		for(File f : currentDir.listFiles()) {
			if (f.isDirectory()) {
				System.out.println("<" + f.getName() + ">");
			} else
				System.out.println(f.getName());
		}
		return true;
	}
}
