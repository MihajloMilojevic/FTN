package voznje;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.opencsv.CSVReader;

public class Zadatak4 {
	
	public static String DATA_FILE = "resources/voznje.csv";
	public static String OUT_FILE = "resources/zadatak4.json";
	public static String CONFIG_FILE = "resources/zadatak4_pretraga.yaml";

	public static void main(String[] args) {
		writeConfig();
		List<Polazak> polasci = readCSV();
		ArrayList<Polazak> polasciFiltered = new ArrayList<>();
		HashMap<String, String> config = readConfig();	
		String polaziste = config.get("polaziste");
		String odrediste = config.get("odrediste");
		String vreme = config.get("vreme");
		System.out.println("Polaziste: " + polaziste + ", Odrediste: " + odrediste + ", Vreme: " + vreme);
		for (Polazak p : polasci) {
			if (p.relacija.getPolaziste().equals(polaziste) && p.relacija.getOdrediste().equals(odrediste)
					&& p.vremePolaska.equals(vreme)) {
				polasciFiltered.add(p);
			}
		}
		writeJSON(polasciFiltered);
	}
	
	public static void writeJSON(ArrayList<Polazak> polasci) {
		ObjectMapper mapper = new ObjectMapper();
		mapper.enable(SerializationFeature.INDENT_OUTPUT);
		try {
			mapper.writeValue(new FileWriter(OUT_FILE), polasci);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	@SuppressWarnings("unchecked")
	public static HashMap<String, String> readConfig() {
        try (FileReader fr = new FileReader(CONFIG_FILE)) {
            Yaml yaml = new Yaml(new Constructor(HashMap.class));
            return (HashMap<String, String>)yaml.load(fr);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
	}
	
	public static List<Polazak> readCSV() {
		try (CSVReader csvReader = new CSVReader(new FileReader(DATA_FILE))) {
			String[] nextRecord;
			ArrayList<Polazak> polasci = new ArrayList<>();
			while ((nextRecord = csvReader.readNext()) != null) {
				polasci.add(new Polazak(nextRecord));
			}
			return polasci;
		} catch (IOException e) {
			e.printStackTrace();
		}
		return null;
	}

	public static void writeConfig() {
		try (FileWriter wr = new FileWriter(CONFIG_FILE)) {
			DumperOptions options = new DumperOptions();
			options.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);
			Yaml yaml = new Yaml(options);
			HashMap<String, String> config = new HashMap<>();
			config.put("polaziste", "Beograd");
			config.put("odrediste", "Novi Sad");
			config.put("vreme", "12:00");
			yaml.dump(config, wr);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
