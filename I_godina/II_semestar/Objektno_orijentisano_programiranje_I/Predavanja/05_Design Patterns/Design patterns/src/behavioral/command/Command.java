package behavioral.command;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public abstract class Command {

	public static File currentDir = new File(".");
	
	public List<String> parameters;

	public Command() {
		parameters = new ArrayList<String>();
	}
	
	/** Izvršava komandu. 
	 * Ako vrati <b>false</b>, program će završiti sa radom.
	 * @return da li da ostane u programu ili ne
	 */
	public abstract boolean execute();
}
