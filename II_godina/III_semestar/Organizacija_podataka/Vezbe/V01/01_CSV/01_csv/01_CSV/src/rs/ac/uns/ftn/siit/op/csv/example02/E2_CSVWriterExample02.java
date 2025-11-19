package rs.ac.uns.ftn.siit.op.csv.example02;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.opencsv.CSVWriter;
import com.opencsv.CSVWriterBuilder;
import com.opencsv.ICSVWriter;

public class E2_CSVWriterExample02 {

	static final String outputFile_all = "resources/drzave_gradovi2_configured.csv";

	static final String header = "Coutry,City";
	static final String[] countries = { "Australia,Canberra", "Canada,Ottawa", "China,Beijing", "France,Paris" };
	
	public static void main(String[] args) throws IOException {

		List<String[]> content = new ArrayList<String[]>();
		content.add(header.split(","));
		for (String country : countries) {
			String[] line = country.split(",");
			content.add(line);
		}

		try(CSVWriter csvWriter = (CSVWriter) new CSVWriterBuilder(new FileWriter(outputFile_all))
			    .withSeparator('#')
			    .withQuoteChar(ICSVWriter.DEFAULT_QUOTE_CHARACTER)	// obratiti paznju na klasu iz kojih dolaze konstante... 
			    .withEscapeChar(ICSVWriter.DEFAULT_ESCAPE_CHARACTER)
			    .withLineEnd(ICSVWriter.DEFAULT_LINE_END)
			    .build()) {
			csvWriter.writeAll(content);
		}
		
		
//		try (CSVWriter writer = new CSVWriter(new FileWriter(outputFile_all), '#', isto to na malo drugaciji nacin; stariji nacin rada;
//				CSVWriter.NO_QUOTE_CHARACTER,
//				CSVWriter.DEFAULT_ESCAPE_CHARACTER,
//				CSVWriter.DEFAULT_LINE_END)) {
//			writer.writeAll(content);
//
//		} catch (IOException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
		
		
	}

}
