package rs.ac.uns.ftn.siit.op.json.example01;

import java.io.File;
import java.io.IOException;

import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.MapperFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

public class E2_JSONMapper {

	public static void main(String[] args) throws JsonParseException, JsonMappingException, IOException {
		/***********************************/
		/*** Convert JSON to Java Object ***/
		/***********************************/
		ObjectMapper mapper = new ObjectMapper();

		mapper.configure(MapperFeature.ACCEPT_CASE_INSENSITIVE_PROPERTIES, true);
		// As an alternative, configuration per class could be used:
		// mapper.configOverride(Book.class).setFormat(JsonFormat.Value.empty().withFeature(Feature.ACCEPT_CASE_INSENSITIVE_PROPERTIES));

		// Configure the Jackson parser to see private fields
		// This is a global configuration and it is an alternative to the
		// @JsonAutoDetect annotation
		// mapper.setVisibilityChecker(mapper.getSerializationConfig().getDefaultVisibilityChecker()
		// .withFieldVisibility(Visibility.ANY));

		Book book = mapper.readValue(new File("resources/Example1_Book.json"), Book.class);

		System.out.println(book);

		/***********************************/
		/*** Convert Java Object to JSON ***/
		/***********************************/
		book.setTitle("Changed book title");

		mapper.enable(SerializationFeature.INDENT_OUTPUT);

		mapper.writeValue(new File("resources/Example1_Book_changed.json"), book);
	}

}
