package vezbe_01_csv.zadaci;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;

public class Zadatak3 {
	
	public static void main(String[] args) {
		read();
	}
	private static void read() {
		for(int i = 0; i < 3; i++) {
			String CSV_FILE_NAME = "resources/vezbe_01_csv/input3_" + i +".csv";
			try (BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(new File(CSV_FILE_NAME)))) ) {
				
				String linija;
				while((linija = reader.readLine()) != null) {
					String tokens[] = linija.split(",");
					if(tokens.length == 5 && tokens[0].startsWith("sw")) {
						for (String string : tokens) {
							System.out.printf("%s \t", string);
						}
						System.out.println();
					}
				}
							
			} catch (FileNotFoundException e) {
				System.out.println("Could not open file");
	
			} catch (IOException e) {
				System.out.println("I/O error occured");
	
			}
		}
	}

}
