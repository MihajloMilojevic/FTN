package rs.ac.uns.ftn.siit.op.json.examples_additional;

import java.io.File;
import java.io.IOException;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

public class E3_JSONTreeStream {

	public static void main(String[] args) throws JsonProcessingException, IOException {
		ObjectMapper objectMapper = new ObjectMapper();
		E2_AuthorsBook authorsBook = new E2_AuthorsBook();

		// create root JSON node from a file
		JsonNode rootNode = objectMapper.readTree(new File("resources/Example1_Book.json"));

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
		objectMapper.writeValue(new File("resources/Example3_Book_changed.json"), rootNode);

	}

}
