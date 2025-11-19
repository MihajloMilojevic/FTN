package rs.ac.uns.ftn.siit.op.json.example01;

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

		Map<String, Object> book = mapper.readValue(new File("resources/Example1_Book.json"), Map.class);

		System.out.println(book);

		/***********************************/
		/*** Convert Java Object to JSON ***/
		/***********************************/

		book.put("newAttribute", "newValue");

		mapper.enable(SerializationFeature.INDENT_OUTPUT);

		mapper.writeValue(new File("resources/Example1_Book_changed.json"), book);

	}

}
