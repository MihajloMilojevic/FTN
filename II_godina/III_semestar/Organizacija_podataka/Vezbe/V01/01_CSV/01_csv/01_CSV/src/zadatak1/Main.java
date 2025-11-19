package zadatak1;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Comparator;

import com.opencsv.CSVParser;
import com.opencsv.CSVParserBuilder;
import com.opencsv.CSVReader;
import com.opencsv.CSVReaderBuilder;
import com.opencsv.CSVWriter;
import com.opencsv.CSVWriterBuilder;

public class Main {

	public static String INPUT_FILE = "resources/tacke.csv";
	public static String OUTPUT_FILE = "resources/tacke_out.csv";
	public static void main(String[] args) {
		CSVParser parser = new CSVParserBuilder().withSeparator('#').build();
		ArrayList<Double[]> points = new ArrayList<>();
		String[] line;
		try (CSVReader reader = new CSVReaderBuilder(new FileReader(INPUT_FILE)).withCSVParser(parser).build()) {
			while ((line = reader.readNext()) != null) {
				Double[] point = new Double[3];
				point[0] = Double.parseDouble(line[0]);
				point[1] = Double.parseDouble(line[1]);
				point[2] = Math.sqrt(Math.pow(point[0], 2) + Math.pow(point[1], 2));
				points.add(point);
			}
			points.sort(new Comparator<Double[]>() {
				@Override
				public int compare(Double[] a, Double[] b) {
					return Double.compare(a[2], b[2]);
				}
			});
		}
		catch (FileNotFoundException e) {
			System.out.println("Could not open file");
		}
		catch (IOException e) {
			System.out.println("I/O error occured");
		}
		catch (Exception e) {
			System.out.println("An error occured");
		}
		try (CSVWriter writer = (CSVWriter) new CSVWriterBuilder(new FileWriter(OUTPUT_FILE)).withSeparator('#').build()) {
			for (Double[] point : points) {
				writer.writeNext(new String[] { point[0].toString(), point[1].toString(), point[2].toString() });
			}
			System.out.println("Done");
		} catch (FileNotFoundException e) {
			System.out.println("Could not open file");
		} catch (IOException e) {
			System.out.println("I/O error occured");
		} catch (Exception e) {
			System.out.println("An error occured");
		}
	}

}
