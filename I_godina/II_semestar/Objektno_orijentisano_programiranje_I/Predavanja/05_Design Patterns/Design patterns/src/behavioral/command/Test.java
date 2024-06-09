package behavioral.command;

import java.io.IOException;
import java.util.Scanner;

public class Test {

	public static void main(String[] args) {
		Parser parser = new Parser();
		Scanner sc = new Scanner(System.in);
		while (true) {
			try {
				System.out.print(Command.currentDir.getCanonicalPath() + ">");
			} catch (IOException e) {
				e.printStackTrace();
			}
			String line = sc.nextLine();
			Command cmd = parser.parse(line);
			if (cmd != null) { 
				if (cmd.execute() == false)
					break;
			} else
				System.out.println("Unknown command.");
		}
		sc.close();
	}

}
