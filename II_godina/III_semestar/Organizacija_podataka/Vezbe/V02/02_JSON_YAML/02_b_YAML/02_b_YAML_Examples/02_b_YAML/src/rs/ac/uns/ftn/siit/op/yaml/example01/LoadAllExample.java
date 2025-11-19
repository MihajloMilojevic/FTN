package rs.ac.uns.ftn.siit.op.yaml.example01;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.List;
import java.util.Map;

import org.yaml.snakeyaml.Yaml;

public class LoadAllExample {

	@SuppressWarnings("unchecked")
	public static void main(String[] args) throws FileNotFoundException {
		loadFromString();
		
		loadAllFromFile();
	}

	@SuppressWarnings("unchecked")
	private static void loadFromString() {
		Yaml yaml = new Yaml();

		// Loading a list
		String documentContainingList = "\n- A\n- B\n- C";
		List<String> list = (List<String>) yaml.load(documentContainingList);
		System.out.println(list);

		// Loading a map
		String documentContainingMap = "Manufacturer: Toyota\nModel: Yaris\nYear: 2018";
		Map<String, Object> map = (Map<String, Object>) yaml.load(documentContainingMap);
		System.out.println(map);
		System.out.println(map.get("Model"));
	}
	
	private static void loadAllFromFile() {
		try (InputStream input = new FileInputStream(new File("resources/log.yaml"));) {

			Yaml yaml = new Yaml();
			int counter = 0;

			// The .loadAll(input) method returns an instance of Iterable<Object>,
			// where each object is of type Map<String, Object>
			for (Object data : yaml.loadAll(input)) {
				System.out.println("Data " + data);

				Map<String, Object> dataMap = (Map<String, Object>) data;
				System.out.println("Time: " + dataMap.get("Time"));

				counter++;
			}

			System.out.println("No. of documents: " + counter);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
