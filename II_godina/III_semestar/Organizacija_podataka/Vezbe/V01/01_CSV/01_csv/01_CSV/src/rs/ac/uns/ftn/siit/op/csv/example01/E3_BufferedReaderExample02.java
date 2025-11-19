package rs.ac.uns.ftn.siit.op.csv.example01;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class E3_BufferedReaderExample02 {
	static final String CSV_FILE_NAME = "resources/drzave_gradovi.csv";
	static final String DELIMITER = ",";

	public static void main(String[] args) {

		// The try-with-resources Statement:
		// https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html
		try (BufferedReader fileReader = new BufferedReader(new FileReader(CSV_FILE_NAME))) {
			String line = "";

			while ((line = fileReader.readLine()) != null) {
				String[] tokens = line.split(DELIMITER);
				for (String token : tokens) {
					System.out.print(token + " | ");
				}
				System.out.println("");
			}
		} catch (FileNotFoundException e) {
			System.out.println("Could not open file");

		} catch (IOException e) {
			System.out.println("I/O error occured");

		}
	}
}
