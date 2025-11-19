package rs.ac.uns.ftn.siit.op.csv.example01;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import com.opencsv.CSVParser;
import com.opencsv.CSVParserBuilder;
import com.opencsv.CSVReader;
import com.opencsv.CSVReaderBuilder;

// Primer u kom se obradjuje fajl ciji sadrzaj odstupa od 'standardnog'
// Zaglavlje se neretko preskace kada je potrebno obraditi podatke 
public class E5_CSVReaderExample02 {

	static final String CSV_FILE_NAME = "resources/indijska_hrana.csv";

	public static void main(String[] args) {

		CSVParser parser = new CSVParserBuilder().withSeparator(';').withQuoteChar('\'').build();

		try (CSVReader csvReader = new CSVReaderBuilder(new FileReader(CSV_FILE_NAME)).withCSVParser(parser)
				.withSkipLines(1).build()) {
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
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
	}

}
