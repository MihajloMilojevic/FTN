package vezbe_03_yaml.example03;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

public class Parser {

	public static void main(String args[]) throws IOException {
		/***********************************/
		/*** Convert YAML to Java Object ***/
		/***********************************/
		// One way of loading a custom type is by using the Constructor class
		// The root type for a YAML document must be specified
		Yaml yaml = new Yaml(new Constructor(Invoice.class));

		Invoice invoice = null;
		try (InputStream input = new FileInputStream(new File("resources/invoice.yaml"));) {
			invoice = (Invoice) yaml.load(input);
			System.out.println(invoice);
		}

		/***********************************/
		/*** Convert Java Object to YAML ***/
		/***********************************/
		yaml = new Yaml();

		// Dump an object into a YAML document
		// When used with custom Java type, adds the global explicit tag to the output
		// document
		String output = yaml.dump(invoice);
		System.out.println(output);
	}

}
