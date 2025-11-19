package voznje;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.util.ArrayList;
import java.util.HashMap;

import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import com.opencsv.CSVReader;


public class Zadatak2 {
	static String INPUT_FILE_NAME = "resources/voznje.csv";
	static String OUTPUT_FILE_NAME = "resources/voznje_out_2.yaml";
	public static void main(String[] args) {
		ArrayList<Polazak> polasci = new ArrayList<>();
		try (CSVReader reader = new CSVReader(new FileReader(INPUT_FILE_NAME))) {
			for (String[] linija : reader.readAll()) {
				polasci.add(new Polazak(linija));
			}
		} catch (Exception e) {
			e.printStackTrace();
			return;
		}
		HashMap<String, Integer> relacije = new HashMap<>();
		for (Polazak pol : polasci) {
			if (!relacije.containsKey(pol.relacija)) {
				relacije.put(pol.relacija.sifra, 0);
			}
			relacije.put(pol.relacija.sifra, relacije.get(pol.relacija.sifra) + 1);
		}
		String maxRelacija = null;
		for (String relacija : relacije.keySet()) {
			if (maxRelacija == null || relacije.get(relacija) > relacije.get(maxRelacija)) {
				maxRelacija = relacija;
			}
		}
		
		Polazak najduzaRelacija = null;
		int maxTrajanje = 0;
		
		Polazak najIsplativijaRelacija = null;
		double maxProfit = 0;
		
		for (Polazak pol : polasci) {
			
			if (najduzaRelacija == null || pol.getTrajanje() > maxTrajanje) {
				najduzaRelacija = pol;
				maxTrajanje = pol.getTrajanje();
			}
			if (najIsplativijaRelacija == null || pol.getProfit() > maxProfit) {
				najIsplativijaRelacija = pol;
				maxProfit = pol.getProfit();
			}
		}
		Rezultat rezultat = new Rezultat(maxRelacija, najduzaRelacija, najIsplativijaRelacija);
		try (Writer w = new FileWriter(OUTPUT_FILE_NAME)) {
			(new Yaml(new Constructor(Rezultat.class))).dump(rezultat, w);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static class Rezultat {
		public String relacija_najvise_polazaka;
		public Polazak najduzi_polazak;
		public Polazak najisplativiji_polazak;

		public Rezultat(String maxRelacija, Polazak najduzaRelacija, Polazak najIsplativijaRelacija) {
			this.relacija_najvise_polazaka = maxRelacija;
			this.najduzi_polazak = najduzaRelacija;
			this.najisplativiji_polazak = najIsplativijaRelacija;
		}

		public Rezultat() {
			super();
		}

		public String getRelacija_najvise_polazaka() {
			return relacija_najvise_polazaka;
		}

		public void setRelacija_najvise_polazaka(String relacija_najvise_polazaka) {
			this.relacija_najvise_polazaka = relacija_najvise_polazaka;
		}

		public Polazak getNajduzi_polazak() {
			return najduzi_polazak;
		}

		public void setNajduzi_polazak(Polazak najduzi_polazak) {
			this.najduzi_polazak = najduzi_polazak;
		}

		public Polazak getNajisplativiji_polazak() {
			return najisplativiji_polazak;
		}

		public void setNajisplativiji_polazak(Polazak najisplativiji_polazak) {
			this.najisplativiji_polazak = najisplativiji_polazak;
		}
	}
}
