package vezbe_02_json.example01;

import java.io.File;
import java.io.IOException;
import java.util.Map;

import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

public class E1_JSONSimpleMapper {

	public static void main(String[] args) throws JsonParseException, JsonMappingException, IOException {
		/***********************************/
		/*** Convert JSON to Java Object ***/
		/***********************************/
		ObjectMapper mapper = new ObjectMapper();

		@SuppressWarnings("unchecked")
		Map<String, Object> book = mapper.readValue(new File("resources/vezbe_02_json/Book.json"), Map.class);

		System.out.println(book);

		/***********************************/
		/*** Convert Java Object to JSON ***/
		/***********************************/

		book.put("newattribute", "newValue");
		
		System.out.println(book);

		mapper.enable(SerializationFeature.INDENT_OUTPUT);

		mapper.writeValue(new File("resources/vezbe_02_json/Book_changed.json"), book);

	}

}
