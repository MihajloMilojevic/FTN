package vezbe_01_csv.zadaci;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Reader;
import java.io.Writer;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;
import com.opencsv.bean.StatefulBeanToCsv;
import com.opencsv.bean.StatefulBeanToCsvBuilder;
import com.opencsv.exceptions.CsvDataTypeMismatchException;
import com.opencsv.exceptions.CsvRequiredFieldEmptyException;

public class Zadatak1 {
	static final String CSV_FILE_NAME = "resources/vezbe_01_csv/tacke.csv";
	static List<Tacka> tacke;
	
	public static void main(String[] args) {
		tacke = new ArrayList<Tacka>();
		readPoints();
		sortPoints();
		writePoints();
	}

	private static void writePoints() {
		try (Writer writer = new FileWriter("resources/vezbe_01_csv/tacke2.csv")) {
			StatefulBeanToCsv<Tacka> beanToCsv = new StatefulBeanToCsvBuilder<Tacka>(writer)
					.withApplyQuotesToAll(false).withSeparator('#').build();
			writer.write("x#y#z#d\n");
			beanToCsv.write(tacke);

		} catch (IOException e) {
			e.printStackTrace();
		} catch (CsvDataTypeMismatchException e) {
			e.printStackTrace();
		} catch (CsvRequiredFieldEmptyException e) {
			e.printStackTrace();
		}
		
	}

	private static void sortPoints() {
		Collections.sort(tacke, new Comparator<Tacka>() {
			@Override
			public int compare(Tacka t1, Tacka t2) {
				if(t1.getDist() < t2.getDist())
					return 1;
				return -1;
			}
		});
		
	}

	private static void readPoints() {
		try (Reader reader = new FileReader(CSV_FILE_NAME)) {
			CsvToBean<Tacka> csv = new CsvToBeanBuilder<Tacka>(reader)
					.withType(Tacka.class).withSkipLines(1).withSeparator(',').build();

			List<Tacka> procitane = csv.parse();

			for (Tacka tacka : procitane) {
				tacka.calculateDistance();
				tacke.add(tacka);
			}
			
		} catch (FileNotFoundException e) {
			System.out.println("Could not open file");

		} catch (IOException e) {
			System.out.println("I/O error occured");

		}
		
	}

}
