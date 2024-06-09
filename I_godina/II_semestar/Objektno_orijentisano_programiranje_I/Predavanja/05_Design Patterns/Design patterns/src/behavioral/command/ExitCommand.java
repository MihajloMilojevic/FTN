package behavioral.command;

public class ExitCommand extends Command {

	@Override
	public boolean execute() {
		//System.exit(0);
		return false;
	}

}
