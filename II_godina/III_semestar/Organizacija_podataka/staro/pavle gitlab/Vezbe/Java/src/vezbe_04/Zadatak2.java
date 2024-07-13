package vezbe_04;

import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;

public class Zadatak2 {

	private static String CSV_PATH = "D:\\Fakultet\\SIIT\\Organizacija podataka\\Vezbe\\Java\\resources\\vezbe_04\\ulazna.csv";
	private static String JSON_PATH = "D:\\Fakultet\\SIIT\\Organizacija podataka\\Vezbe\\Java\\resources\\vezbe_04\\izlazna";
	private static List<Putanja> procitane;
	private static HashMap<String, Integer> maksi;
	private static HashMap<String, Integer> maksiTime;
	private static DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd.MM.yyyy.");
	private static DateTimeFormatter timeFormat = DateTimeFormatter.ofPattern("HH:mm");

	public static void main(String[] args) throws Exception, IOException {
		// najveci broj, ukupno najduze, najveca zarada
		try (Reader reader = new FileReader(CSV_PATH)) {
			CsvToBean<Putanja> csv = new CsvToBeanBuilder<Putanja>(reader).withType(Putanja.class).withSkipLines(1)
					.withSeparator(',').build();

			procitane = csv.parse();

			najveciBroj();
			najduze();
			zarada();
		}
	}


	private static void najveciBroj() {
		maksi = new HashMap<String, Integer>();
		for (Putanja p : procitane) {
			String s = p.getMestoPolaska() + "-" + p.getMestoDolaska();
			maksi.putIfAbsent(s, 0);
			maksi.replace(s, maksi.get(s) + 1);
		}

		int maks = -1;
		String maksiPath = "";
		for (String s : maksi.keySet()) {
			if (maksi.get(s) > maks) {
				maksiPath = s;
				maks = maksi.get(s);
			}
		}
		/*
		 * for (String putanja : maksi.keySet()) { System.out.println(putanja + " " +
		 * maksi.get(putanja)); }
		 */
		System.out.println("Najvise " + maksiPath + " sa " + maks);
	}

	private static void najduze() {
		maksiTime = new HashMap<String, Integer>();
		for (Putanja p : procitane) {
			String s = p.getMestoPolaska() + "-" + p.getMestoDolaska();
			maksiTime.putIfAbsent(s, 0);
			int val = (-1)*(int) ChronoUnit.HOURS.between(LocalTime.parse(p.getVremeDolaska(), timeFormat),
					LocalTime.parse(p.getVremePolaska(), timeFormat));
			maksiTime.replace(s, maksiTime.get(s) + val);
		}

		int maks = -1;
		String maksiPath = "";
		for (String s : maksiTime.keySet()) {
			if (maksiTime.get(s) > maks) {
				maksiPath = s;
				maks = maksiTime.get(s);
			}
		}
		/*
		 * for (String putanja : maksi.keySet()) { System.out.println(putanja + " " +
		 * maksi.get(putanja)); }
		 */
		System.out.println("Najduze " + maksiPath + " sa " + maks);
	}
	
	private static void zarada() {
		HashMap<String, Double> dinariPoSatu = new HashMap<String, Double>();
	}

}
