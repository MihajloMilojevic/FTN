package vezbe_03_yaml.example01;

import java.util.List;
import java.util.Map;

import org.yaml.snakeyaml.Yaml;

public class LoadExample {

	@SuppressWarnings("unchecked")
	public static void main(String[] args) {
		// The Yaml class is the entry point for the API
		// .load(document) method returns an object of class Object
		Yaml yaml = new Yaml();

		String documentContainingList = "\n- A\n- B\n- C";
		List<String> list = (List<String>) yaml.load(documentContainingList);
		System.out.println(list);

		String documentContainingMap = "Manufacturer: Toyota\nModel: Yaris\nYear: 2018";
		Map<String, Object> map = (Map<String, Object>) yaml.load(documentContainingMap);
		System.out.println(map);
		System.out.println(map.get("Model"));

	}

}
