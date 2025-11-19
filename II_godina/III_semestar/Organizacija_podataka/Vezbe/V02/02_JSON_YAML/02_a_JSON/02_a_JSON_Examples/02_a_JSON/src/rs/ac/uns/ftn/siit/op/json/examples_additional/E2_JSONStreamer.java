package rs.ac.uns.ftn.siit.op.json.examples_additional;

import java.io.File;
import java.io.IOException;

import com.fasterxml.jackson.core.JsonEncoding;
import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonToken;

public class E2_JSONStreamer {

	static final String JSON_FILE_NAME = "resources/Example2_Book_generated.json";

	public static void main(String[] args) throws IOException {
		generateJSON();

		E2_AuthorsBook authorsBook = new E2_AuthorsBook();
//		parseJSON(authorsBook, JSON_FILE_NAME);
//		System.out.println(authorsBook);

		parseJSON(authorsBook, "resources/Example2_Book.json");
		System.out.println(authorsBook);
	}

	public static void generateJSON() throws IOException {
		JsonFactory jsonFactory = new JsonFactory();
		JsonGenerator jsonGenerator = jsonFactory.createGenerator(new File(JSON_FILE_NAME), JsonEncoding.UTF8);

		jsonGenerator.writeStartObject();
		jsonGenerator.writeObjectFieldStart("Author");
		jsonGenerator.writeStringField("First_Name", "Stephen");
		jsonGenerator.writeStringField("Last_Name", "King");
		jsonGenerator.writeEndObject(); // for field 'Author'
		jsonGenerator.writeStringField("Title", "The Green Mile");
		jsonGenerator.writeEndObject();

		// it is important to close the generator
		// it will force flushing of the output and close underlying output stream
		jsonGenerator.close();

	}

	public static void parseJSON(E2_AuthorsBook authorsBook, String bookName) throws JsonParseException, IOException {
		JsonFactory jsonFactory = new JsonFactory();
		JsonParser jsonParser = jsonFactory.createParser(new File(bookName));

		// the following line will return JsonToken.Start_OBJECT (first curly bracket)
		jsonParser.nextToken();

		// parse JSON file for needed tokens
		while (jsonParser.nextToken() != JsonToken.END_OBJECT) {
			String fieldName = jsonParser.getCurrentName();
			jsonParser.nextToken(); // move to value, or START_OBJECT/START_ARRAY

			if ("Author".equals(fieldName)) { // field value contains an object

				// parse this object in the same way the whole JSON is parsed
				while (jsonParser.nextToken() != JsonToken.END_OBJECT) {
					String nameField = jsonParser.getCurrentName();
					jsonParser.nextToken(); // move to value

					if ("First_Name".equals(nameField)) {
						authorsBook.setFirstName(jsonParser.getText());

					} else if ("Last_Name".equals(nameField)) {
						authorsBook.setLastName(jsonParser.getText());
					}
				}
			} else if ("Title".equals(fieldName)) {
				authorsBook.setBookTitle(jsonParser.getText());

			} else {
				// is it OK to have additional fields? if no: 
				// throw new IllegalStateException("Unrecognized field '" + fieldName + "'!");
			}
		}

		jsonParser.close();

	}

}
