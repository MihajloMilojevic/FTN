package rs.ac.uns.ftn.siit.op.csv.example01;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;

import com.opencsv.CSVReader;

public class E4_CSVReaderExample01 {

	static final String CSV_FILE_NAME = "resources/drzave_gradovi.csv";

	public static void main(String[] args) {

		readNextExample();

		System.out.println("\n\n########################################\n\n");

		readAllExample();
	}

	private static void readNextExample() {
		try (CSVReader csvReader = new CSVReader(new FileReader(CSV_FILE_NAME))) {
			String[] row = null;

			while ((row = csvReader.readNext()) != null) {
				StringBuilder rowDataBuilder = new StringBuilder();

				for (int i = 0; i < row.length; i++) {
					rowDataBuilder.append(row[i]);

					if (i != row.length - 1) {
						rowDataBuilder.append("|");

					}
				}

				System.out.println(rowDataBuilder);
			}
		} catch (FileNotFoundException e) {
			System.out.println("Could not open file");

		} catch (IOException e) {
			System.out.println("I/O error occured");

		}
	}

	private static void readAllExample() {
		try (CSVReader csvReader = new CSVReader(new FileReader(CSV_FILE_NAME))) {
			String[] row = null;

			List<String[]> content = csvReader.readAll();

			for (Object object : content) {
				row = (String[]) object;
				StringBuilder rowDataBuilder = new StringBuilder();

				for (int i = 0; i < row.length; i++) {
					rowDataBuilder.append(row[i]);

					if (i != row.length - 1)
						rowDataBuilder.append("|");
				}
				System.out.println(rowDataBuilder);
			}

		} catch (FileNotFoundException e) {
			System.out.println("Could not open file");

		} catch (IOException e) {
			System.out.println("I/O error occured");

		}
	}

}
