package vezbe_02_json.zadaci;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import com.fasterxml.jackson.core.JsonGenerationException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.MapperFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;


public class Zadatak2 {
	
	private static String path_csv = "resources/vezbe_02_json/countries_cities.csv";
	private static String path_json = "resources/vezbe_02_json/";
	
	private static HashMap<String, ArrayList<Country>> continents;
	public static void main(String[] args) throws JsonGenerationException, JsonMappingException, IOException {
		continents = new HashMap<String, ArrayList<Country>>();
		read_csv();
		write_json();
	}

	private static void write_json() throws JsonGenerationException, JsonMappingException, IOException {
		ObjectMapper mapper = new ObjectMapper();
		mapper.configure(MapperFeature.ACCEPT_CASE_INSENSITIVE_PROPERTIES, true);
		mapper.enable(SerializationFeature.INDENT_OUTPUT);
		for (String cont : continents.keySet()) {
			String path = path_json + cont + ".json";
			mapper.writeValue(new File(path), continents.get(cont));
		}
	}

	private static void read_csv() {
		try (Reader reader = new FileReader(path_csv)) {
			CsvToBean<Country> csv = new CsvToBeanBuilder<Country>(reader)
					.withType(Country.class).withSkipLines(1).withSeparator(',').build();

			List<Country> countries = csv.parse();

			for (Country country : countries) {
				continents.putIfAbsent(country.getContinentName(), new ArrayList<Country>());
				continents.get(country.getContinentName()).add(country);
			}
			
			for (String cont : continents.keySet()) {
				System.out.println(cont);
				for (Country country : continents.get(cont)) {
					System.out.println(country);
				}
			}
			
		} catch (FileNotFoundException e) {
			System.out.println("Could not open file");

		} catch (IOException e) {
			System.out.println("I/O error occured");

		}
	}

}
