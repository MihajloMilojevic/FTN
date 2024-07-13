package vezbe_02_json.zadaci;

import java.io.File;
import java.io.IOException;

import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.MapperFeature;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Zadatak1 {

	static String path = "resources/vezbe_02_json/Bookstore.json";

	public static void main(String[] args) throws Throwable {
		read1();
	}

	private static void read1() throws JsonParseException, JsonMappingException, IOException {
		ObjectMapper mapper = new ObjectMapper();
		mapper.configure(MapperFeature.ACCEPT_CASE_INSENSITIVE_PROPERTIES, true);
		PaperStorage books = mapper.readValue(new File(path), PaperStorage.class);
		for (Book book : books.getBooks()) {
			System.out.println(book);
		}
		for (Magazine mag : books.getMagazines()) {
			System.out.println(mag);
		}

	}

}
