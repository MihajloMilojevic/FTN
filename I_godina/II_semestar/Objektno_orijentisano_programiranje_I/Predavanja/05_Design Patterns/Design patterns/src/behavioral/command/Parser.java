package behavioral.command;

public class Parser {
	public Command parse(String s) {
		String commandStr = getCommand(s.trim());
		String param = getParams(s.trim());
		if (commandStr.equalsIgnoreCase("dir"))
			return new DirCommand();
		else if (commandStr.equalsIgnoreCase("exit"))
			return new ExitCommand();
		else if (commandStr.equalsIgnoreCase("cd")) {
			return new CdCommand(param);
		}
		else if (commandStr.equals(""))
			return new BlankCommand();
		else 
			return null;
	}
	
	/** Izvlači komandu iz komandne linije.
	 * Primer: <code>cd pera</code> <br />
	 * Komanda je <b>cd</b>, a paramatar je <b>pera</b>
	 */
	private String getCommand(String s) {
		int index = s.indexOf(' ');
		if (index != -1) {
			return s.substring(0, index);
		} else {
			return s;
		}
	}
	
	/** Izvlači komandu iz komandne linije.
	 * Primer: <code>cd pera</code> <br />
	 * Komanda je <b>cd</b>, a paramatar je <b>pera</b>
	 */
	private String getParams(String s) {
		int index = s.indexOf(' ');
		if (index != -1) {
			return s.substring(index + 1);
		} else {
			return "";
		}
	}
}
