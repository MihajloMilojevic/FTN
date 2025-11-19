package rs.ac.uns.ftn.siit.op.csv.example02;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.opencsv.CSVWriter;

public class E1_CSVWriterExample01 {

	static final String outputFile_next = "resources/drzave_gradovi2_next.csv";
	static final String outputFile_all = "resources/drzave_gradovi2_all.csv";

	static final String header = "Coutry,City";
	static final String[] countries = { "Australia,Canberra", "Canada,Ottawa", "China,Beijing", "France,Paris" };

	public static void main(String[] args) {
		writeNextExample();
		writeAllExample();

	}

	static void writeNextExample() {
		try (CSVWriter writer = new CSVWriter(new FileWriter(outputFile_next))) {
			writer.writeNext(header.split(","));
			for (String country : countries) {
				String[] line = country.split(",");
				writer.writeNext(line);
			}
		} catch (IOException e) {
			System.out.println("I/O error occured");

		}
	}

	static void writeAllExample() {
		List<String[]> content = new ArrayList<String[]>();
		content.add(header.split(","));
		for (String country : countries) {
			String[] line = country.split(",");
			content.add(line);
		}

		try (CSVWriter writer = new CSVWriter(new FileWriter(outputFile_all))) {
			writer.writeAll(content);

		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}
