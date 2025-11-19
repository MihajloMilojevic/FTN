package voznje;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.opencsv.CSVReader;

public class Zadatak3 {
	
	public static String IN_FILE = "resources/voznje.csv";
	public static String OUT_RETURN = "resources/voznje_sa_povratkom.yaml";
	public static String OUT_NO_RETURN = "resources/voznje_bez_povratka.json";

	public static void main(String[] args) {
		Set<Relacija> relacije = readCSV();
		Set<Relacija> withoutReturn = new HashSet<Relacija>();
		Set<Relacija> withReturn = new HashSet<Relacija>();
		for(Relacija r : relacije) {
			boolean found = false;
			for (Relacija s: relacije) {
				if (r.povratak(s)) {
					withReturn.add(r);
					found = true;
				}
			}
			if (!found) {
				withoutReturn.add(r);
			}
		}
		printYAML(withReturn);
		printJSON(withoutReturn);
	}

	public static void printYAML(Set<Relacija> relacije) {
		DumperOptions opts = new DumperOptions();
		opts.setWidth(50);
		opts.setIndent(4);
		opts.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);  // BLOCK, FLOW, AUTO
		opts.setPrettyFlow(true);
		Yaml yaml = new Yaml(opts);
		
		try (FileWriter writer = new FileWriter(OUT_RETURN)) {
			yaml.dump(relacije, writer);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public static void printJSON(Set<Relacija> relacije) {
		ObjectMapper mapper = new ObjectMapper();
		mapper.enable(SerializationFeature.INDENT_OUTPUT);
		try {
			mapper.writeValue(new File(OUT_NO_RETURN), relacije);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public static Set<Relacija> readCSV() {
		try (CSVReader csv = new CSVReader(new FileReader(IN_FILE))) {
			HashSet<Relacija> relacije = new HashSet<Relacija>();
			String[] linija = null;
			while((linija = csv.readNext()) != null) {
				relacije.add(new Relacija(linija));
			}
			return relacije;
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return null;
	}
}
