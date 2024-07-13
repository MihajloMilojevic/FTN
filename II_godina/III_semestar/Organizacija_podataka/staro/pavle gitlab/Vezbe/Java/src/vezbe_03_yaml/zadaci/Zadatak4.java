package vezbe_03_yaml.zadaci;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;

public class Zadatak4 {

	public static void main(String[] args) throws IOException {
		Yaml yaml = new Yaml();
		List<Map<String, String>> errors = new ArrayList<>();
		List<Map<String, String>> warnings = new ArrayList<>();
		try (InputStream input = new FileInputStream(new File("resources/vezbe_03_yaml/log.yaml"));) {
			for (Object o : yaml.loadAll(input)) {
				@SuppressWarnings("unchecked")
				Map<String, String> bean = (Map<String, String>)o;
				if(bean.containsKey("Warning"))
					warnings.add(bean);
				else
					errors.add(bean);
				
			}
		} catch(Exception e) {
			e.printStackTrace();
		}
		
		DumperOptions opts = new DumperOptions();
		opts.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK); 
		yaml = new Yaml(opts);
		FileWriter writer = new FileWriter("resources/vezbe_03_yaml/log_warnings.yaml");
		for (Map<String, String> map : warnings) {
			yaml.dump(map, writer);
		}
		writer = new FileWriter("resources/vezbe_03_yaml/log_errors.yaml");
		for (Map<String, String> map : errors) {
			yaml.dump(map, writer);
		}
		
	
	}

}
