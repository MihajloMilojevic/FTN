package zadatak1;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.Writer;
import java.util.ArrayList;
import java.util.LinkedHashMap;

import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import rs.ac.uns.ftn.siit.op.yaml.example02.Invoice;

public class main {

	public static void main(String args[]) throws IOException {
		Invoice invoice = (Invoice)yamlToBean(Invoice.class, "invoice");	
		ArrayList<Object> exchanges = (ArrayList<Object>)yamlToBean(ArrayList.class, "exchange");
		for (Object exchange : exchanges) {
			LinkedHashMap<String, Object> map = (LinkedHashMap<String, Object>) exchange;
			Exchange ex = new Exchange(map.get("name").toString(), (double)map.get("value"));
			
		}
		//beanToYaml(invoice);
	}

	private static Object yamlToBean(Class cls, String name) throws IOException, FileNotFoundException {
		// One way of loading a custom type is by using the Constructor class
		// The root type for a YAML document must be specified
		Yaml yaml = new Yaml(new Constructor(cls));

		Object obj = null;
		try (InputStream input = new FileInputStream(new File("resources/"+name+".yaml"));) {
			obj = yaml.load(input);		
		}
		return obj;
	}
	
	private static void beanToYaml(Invoice invoice, String name) {
		DumperOptions opts = new DumperOptions();
		opts.setWidth(50);
		opts.setIndent(4);
		opts.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);  // BLOCK, FLOW, AUTO

		Yaml yaml = new Yaml(opts);
		
		try(Writer w = new FileWriter("resources/" + name + ".yaml")) {
			yaml.dump(invoice, w);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
	}

}
