package rs.ac.uns.ftn.siit.op.csv.example01;

import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class E1_ScannerExample {
	static final String CSV_FILE_NAME = "resources/drzave_gradovi.csv";
	static final String DELIMITER = ",";

	public static void main(String[] args) {
		Scanner scanner = null;
		try {
			scanner = new Scanner(new File(CSV_FILE_NAME));
			scanner.useDelimiter(DELIMITER);

			while (scanner.hasNext()) {
				System.out.print(scanner.next() + "|");
			}

		} catch (FileNotFoundException e) {
			e.printStackTrace();

		} finally {
			if (scanner != null) {
				scanner.close();
			}
		}
	}

}
