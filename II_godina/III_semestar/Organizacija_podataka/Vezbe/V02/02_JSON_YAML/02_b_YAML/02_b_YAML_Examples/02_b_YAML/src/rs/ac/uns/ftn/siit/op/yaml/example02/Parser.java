package rs.ac.uns.ftn.siit.op.yaml.example02;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.Writer;

import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

public class Parser {

	public static void main(String args[]) throws IOException {
		Invoice invoice = yamlToBean();		
		beanToYaml(invoice);
	}

	private static Invoice yamlToBean() throws IOException, FileNotFoundException {
		// One way of loading a custom type is by using the Constructor class
		// The root type for a YAML document must be specified
		Yaml yaml = new Yaml(new Constructor(Invoice.class));

		Invoice invoice = null;
		try (InputStream input = new FileInputStream(new File("resources/invoice.yaml"));) {
			invoice = (Invoice) yaml.load(input);		
		}
		return invoice;
	}
	
	private static void beanToYaml(Invoice invoice) {
		DumperOptions opts = new DumperOptions();
		opts.setWidth(50);
		opts.setIndent(4);
		opts.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);  // BLOCK, FLOW, AUTO

		Yaml yaml = new Yaml(opts);
		System.out.println("PRE");
		System.out.println(invoice);
		Address a = new Address("Dositeja Obradovica 3","Novi Sad", "Serbia", "21000");
		invoice.getBillTo().setAddress(a);
		System.out.println("{POSLE");
		System.out.println(invoice);
		try(Writer w = new FileWriter("resources/invoice_mod.yaml")) {
			yaml.dump(invoice, w);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
	}

}
