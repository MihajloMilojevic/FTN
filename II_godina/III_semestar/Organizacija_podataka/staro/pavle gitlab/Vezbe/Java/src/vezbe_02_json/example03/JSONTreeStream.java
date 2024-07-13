package vezbe_02_json.example03;

import java.io.File;
import java.io.IOException;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

import vezbe_02_json.example02.AuthorsBook;

public class JSONTreeStream {

	public static void main(String[] args) throws JsonProcessingException, IOException {
		ObjectMapper objectMapper = new ObjectMapper();
		AuthorsBook authorsBook = new AuthorsBook();

		// create root JSON node from a file
		JsonNode rootNode = objectMapper.readTree(new File("resources/vezbe_02_json/Book.json"));

		// find required attributes and read their values
		authorsBook.setBookTitle(rootNode.path("Title").textValue());

		authorsBook.setFirstName(rootNode.at("/Author/First_Name").textValue());
		
		JsonNode nameNode = rootNode.path("Author");
		authorsBook.setLastName(nameNode.path("Last_Name").textValue());
		// alternative solution
		// authorsBook.setLastName(rootNode.path("Author").path("Last_Name").textValue());
		
		System.out.println(authorsBook);

		// change title of the book in the tree model
		((ObjectNode) rootNode).put("Title", "ChangedBookTitle");
		objectMapper.writeValue(new File("resources/vezbe_02_json/Book_changed.json"), rootNode);

	}

}
