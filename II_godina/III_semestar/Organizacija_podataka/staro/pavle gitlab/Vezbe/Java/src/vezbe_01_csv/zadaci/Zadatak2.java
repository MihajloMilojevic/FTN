package vezbe_01_csv.zadaci;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

import com.opencsv.CSVWriter;
import com.opencsv.CSVWriterBuilder;
import com.opencsv.ICSVWriter;
import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;

public class Zadatak2 {

	static final String CSV_FILE_NAME = "resources/vezbe_01_csv/studenti.csv";
	static List<StudentOcena> studentiOcene;
	static HashMap<String, ArrayList<String>> evaluirani;
	public static void main(String[] args) {
		studentiOcene = new ArrayList<StudentOcena>();
		evaluirani = new HashMap<String, ArrayList<String>>();
		readData();
		writeStudents();
		writeGrades();
	}
	private static void writeStudents() {
		for(int i = 5; i <= 10; i++) {
			
			HashMap<String, Integer> mapa = count(i);
			String filename = "resources/vezbe_01_csv/"+ String.valueOf(i) + ".csv";
			try(CSVWriter csvWriter = (CSVWriter) new CSVWriterBuilder(new FileWriter(filename))
				    .withSeparator(',')
				    .withQuoteChar(ICSVWriter.NO_QUOTE_CHARACTER)
				    .withEscapeChar(ICSVWriter.DEFAULT_ESCAPE_CHARACTER)
				    .withLineEnd(ICSVWriter.DEFAULT_LINE_END)
				    .build()) {
				
				for (String student : mapa.keySet()) {
					ArrayList<String> s = new ArrayList<>();
					
					s.addAll(Arrays.asList(student.split("\\s+")));
					s.add(String.valueOf(mapa.get(student)));
					csvWriter.writeNext(s.toArray(new String[0]));
				}

			} catch (IOException e) {
				e.printStackTrace();
			} 
		}
		
	}
	private static HashMap<String, Integer> count(int ocena) {
		HashMap<String, Integer> mapica = new HashMap<String, Integer>();
		
		for(StudentOcena s : studentiOcene) {
			mapica.putIfAbsent(s.id(), 0);
			if(s.getOcena() != ocena)
				continue;
			int old = mapica.get(s.id());
			mapica.replace(s.id(), old + 1);
			
			if(!evaluirani.containsKey(s.id())) {
				ArrayList<String> a = new ArrayList<String>();
				a.add("0");
				a.add("0");
				evaluirani.put(s.id(), a);
			}
			int polozeni = Integer.parseInt(evaluirani.get(s.id()).get(0));
			double prosek = Double.parseDouble(evaluirani.get(s.id()).get(1));
			if(ocena != 5) {
				prosek = (prosek*polozeni + ocena)/(polozeni + 1);
				polozeni += 1;
			}
			ArrayList<String> lista = new ArrayList<String>();
			lista.add(String.format("%d", polozeni));
			lista.add(String.format("%.2f", prosek));
			evaluirani.replace(s.id(), lista);
		}
		return mapica;
	}

	private static void writeGrades() {
		String filename = "resources/vezbe_01_csv/eval_studenti.csv";
		try(CSVWriter csvWriter = (CSVWriter) new CSVWriterBuilder(new FileWriter(filename))
			    .withSeparator(',')
			    .withQuoteChar(ICSVWriter.NO_QUOTE_CHARACTER)
			    .withEscapeChar(ICSVWriter.DEFAULT_ESCAPE_CHARACTER)
			    .withLineEnd(ICSVWriter.DEFAULT_LINE_END)
			    .build()) {
			
			for (String student : evaluirani.keySet()) {
				ArrayList<String> s = new ArrayList<>();
				
				s.addAll(Arrays.asList(student.split("\\s+")));
				s.addAll((evaluirani.get(student)));
				csvWriter.writeNext(s.toArray(new String[0]));
			}

		} catch (IOException e) {
			e.printStackTrace();
		} 
		
	}
	private static void readData() {
		try (Reader reader = new FileReader(CSV_FILE_NAME)) {
			CsvToBean<StudentOcena> csv = new CsvToBeanBuilder<StudentOcena>(reader)
					.withType(StudentOcena.class).withSkipLines(1).withSeparator(',').build();

			List<StudentOcena> procitane = csv.parse();

			for (StudentOcena studentOcena : procitane) {
				studentiOcene.add(studentOcena);
			}
			
		} catch (FileNotFoundException e) {
			System.out.println("Could not open file");

		} catch (IOException e) {
			System.out.println("I/O error occured");

		}
		
	}
	
}
