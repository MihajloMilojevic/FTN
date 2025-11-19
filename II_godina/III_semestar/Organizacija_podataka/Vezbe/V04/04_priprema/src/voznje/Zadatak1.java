package voznje;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.opencsv.CSVReader;
import com.opencsv.CSVWriter;

public class Zadatak1 {
	static String FILE_NAME = "resources/voznje.csv";
	static String JSON_FILE = "resources/relacije.json";
	public static void main(String[] args) {
		printToCSV();
		ArrayList<Polazak> polasci = readFromCSV();
		HashMap<String, Z1JSONResult> result = new HashMap<String, Z1JSONResult>();
		for (Polazak p: polasci) {
			if (!result.containsKey(p.relacija.sifra)) {
				result.put(p.relacija.sifra, new Z1JSONResult(p.relacija));
			}
			result.get(p.relacija.sifra).polasci.add(new Z1JSONResult.PolazakRedukovano(p));
		}
		printToJSON(result);
	}
	private static void printToJSON(HashMap<String, Z1JSONResult> result) {
		ObjectMapper mapper = new ObjectMapper();
		mapper.enable(SerializationFeature.INDENT_OUTPUT);
		ArrayList<Z1JSONResult> list = new ArrayList<Z1JSONResult>();
		for (Z1JSONResult r: result.values()) {
            list.add(r);
        }
		try {
			mapper.writeValue(new File(JSON_FILE), list);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	static void printToCSV() {
		ArrayList<String[]> lista = new ArrayList<>();
		lista.add(new String[] { "001", "Novi Sad", "Beograd", "31-10-2024", "10:00", "11:00", "1", "300", "25" });
		lista.add(new String[] { "001", "Novi Sad", "Beograd", "31-10-2024", "15:00", "16:00", "1", "300", "30" });
		lista.add(new String[] { "001", "Novi Sad", "Beograd", "31-10-2024", "20:00", "21:00", "1", "300", "18" });

		lista.add(new String[] { "002", "Beograd", "Kraljevo", "31-10-2024", "11:00", "16:00", "7", "1300", "15" });
		lista.add(new String[] { "002", "Beograd", "Kraljevo", "01-11-2024", "11:00", "16:00", "7", "1300", "30" });
		
		lista.add(new String[] { "003", "Kraljevo", "Nis", "01-11-2024", "11:00", "14:00", "7", "1300", "15" });
		lista.add(new String[] { "003", "Kraljevo", "Nis", "02-11-2024", "11:00", "14:00", "7", "1300", "30" });
		
		lista.add(new String[] { "004", "Beograd", "Novi Sad", "31-10-2024", "10:00", "11:00", "1", "300", "25" });
		lista.add(new String[] { "004", "Beograd", "Novi Sad", "31-10-2024", "15:00", "16:00", "1", "300", "30" });
		lista.add(new String[] { "004", "Beograd", "Novi Sad", "31-10-2024", "20:00", "21:00", "1", "300", "18" });
		
		try (CSVWriter writer = new CSVWriter(new FileWriter(FILE_NAME))) {
			writer.writeAll(lista);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	static ArrayList<Polazak> readFromCSV() {
		try (CSVReader csv = new CSVReader(new FileReader(FILE_NAME))) {
			String[] row = null;
			ArrayList<Polazak> polasci = new ArrayList<Polazak>();
			while ((row = csv.readNext()) != null) {
				polasci.add(new Polazak(row));
			}
			return polasci;
		}
		catch (Exception e) {
			return null;
		}
	}
}
