package rs.ac.uns.ftn.siit.op.csv.example03;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.List;

import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;

public class E1_CsvToBeanExample {

	static final String CSV_FILE_NAME = "resources/drzave_gradovi.csv";

	public static void main(String[] args) {
		exampleColumnPositions();

		System.out.println("\n\n########################################\n\n");

		exampleColumnNames();

	}

	static void exampleColumnPositions() {
		try (Reader reader = new FileReader(CSV_FILE_NAME)) {
			CsvToBean<E1_Country_ColumnPositions> csv = new CsvToBeanBuilder<E1_Country_ColumnPositions>(reader)
					.withType(E1_Country_ColumnPositions.class).withSkipLines(1).withSeparator(',').build();

			List<E1_Country_ColumnPositions> countries = csv.parse();

			for (E1_Country_ColumnPositions country : countries) {
				System.out.println(country);
			}
			

		} catch (FileNotFoundException e) {
			System.out.println("Could not open file");

		} catch (IOException e) {
			System.out.println("I/O error occured");

		}
	}

	static void exampleColumnNames() {
		try (Reader reader = new FileReader(CSV_FILE_NAME)) {

			CsvToBean<E1_Country_ColumnNames> csv = new CsvToBeanBuilder<E1_Country_ColumnNames>(reader)
					.withType(E1_Country_ColumnNames.class).withSeparator(',').build(); // ne sme se odraditi skipLine jer mu trebaju nazivi kolona, automatski ce odraditi skip

			List<E1_Country_ColumnNames> countries = csv.parse();

			for (E1_Country_ColumnNames country : countries) {
				System.out.println(country);
			}

		} catch (FileNotFoundException e) {
			System.out.println("Could not open file");

		} catch (IOException e) {
			System.out.println("I/O error occured");

		}

	}

}
