package vezbe_04;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

import com.fasterxml.jackson.core.JsonGenerationException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.opencsv.bean.StatefulBeanToCsv;
import com.opencsv.bean.StatefulBeanToCsvBuilder;

public class Zadatak1 {

	private static String CSV_PATH = "D:\\Fakultet\\SIIT\\Organizacija podataka\\Vezbe\\Java\\resources\\vezbe_04\\ulazna.csv";
	private static String JSON_PATH = "D:\\Fakultet\\SIIT\\Organizacija podataka\\Vezbe\\Java\\resources\\vezbe_04\\izlazna";
	private static DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd.MM.yyyy.");
	private static DateTimeFormatter timeFormat = DateTimeFormatter.ofPattern("HH:mm");
	private static ArrayList<Putanja> putanje;
	private static HashMap<String, ArrayList<Putanja>> mapa;

	public static void main(String[] args) throws Exception {
		mapa = new HashMap<String, ArrayList<Putanja>>();
		formirajUlaznu();
		ispisiIzlaznu();
	}

	private static void formirajUlaznu() throws Exception {
		String mesta[] = { "Zrenjanin", "Novi Sad", "Beograd", "Valjevo", "Kragujevac" };
		int id = 1;
		LocalDate startDate = LocalDate.now();
		LocalTime startTime = LocalTime.of(6, 0, 0);
		Random random = new Random();
		putanje = new ArrayList<>();

		for (String from : mesta) {
			for (String to : mesta) {
				if (!from.equals(to)) {
					int up = random.nextInt(4) + 1;
					for (int i = 1; i < up; i++) {
						int up2 = random.nextInt(8) + 1;
						LocalDate generatedDate = startDate.plusDays(i);
						
						for (int j = 1; j < up2; j++) {
							int generatedSales = random.nextInt(60);
							int generatedPeron = random.nextInt(20);
							double generatedCeona = random.nextDouble() * 1000;
							LocalTime generatedTime = startTime.plusHours(j);
							Putanja p = new Putanja();
							p.setId(String.valueOf(id));

							p.setDatumPolaska(dtf.format(generatedDate));
							p.setDatumDolaska(dtf.format(generatedDate));

							p.setMestoPolaska(from);
							p.setMestoDolaska(to);

							p.setVremePolaska(timeFormat.format(generatedTime));
							p.setVremeDolaska(timeFormat.format(generatedTime.plusHours(random.nextInt(3) + 1)));

							p.setProdateKarte(generatedSales);
							p.setStanicniPeron(String.valueOf(generatedPeron));
							p.setCenaKarte(generatedCeona);

							putanje.add(p);

							mapa.putIfAbsent(from + "_" + to, new ArrayList<>());
							mapa.get(from + "_" + to).add(p);
							id++;
						}

					}
				}
			}
		}

		writeCsv();
	}

	private static void writeCsv() throws Exception {
		for (Putanja putanja : putanje) {
			System.out.println(putanja);
		}
		try (Writer writer = new FileWriter(CSV_PATH)) {
			StatefulBeanToCsv<Putanja> beanToCsv = new StatefulBeanToCsvBuilder<Putanja>(writer)
					.withApplyQuotesToAll(false).build();

			beanToCsv.write(putanje);
		}
	}

	private static void ispisiIzlaznu() throws Exception {
		ObjectMapper mapper = new ObjectMapper();

		mapper.enable(SerializationFeature.INDENT_OUTPUT);
		File fajl;

		for (String s : mapa.keySet()) {
			fajl = new File(JSON_PATH + s + ".json");
			mapper.writeValue(fajl, mapa.get(s));
		}

	}

}
