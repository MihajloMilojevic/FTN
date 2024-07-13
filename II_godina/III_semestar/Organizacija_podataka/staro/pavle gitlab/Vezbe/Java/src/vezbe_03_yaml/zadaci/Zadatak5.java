package vezbe_03_yaml.zadaci;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

import org.apache.commons.lang3.StringUtils;
import org.yaml.snakeyaml.Yaml;

public class Zadatak5 {


	public static void main(String[] args) throws UnsupportedEncodingException, FileNotFoundException, IOException {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		Yaml yaml = new Yaml();
		HashMap<String, String> mapa = new HashMap<>();
		ArrayList<String> keys = new ArrayList<String>();
		try (BufferedReader citac = new BufferedReader(
				new InputStreamReader(new FileInputStream(new File("resources/vezbe_03_yaml/en.yml")), "utf-8"))) {
			String linija = "";
			System.out.println("Ponudjena podesavanja: ");
			while ((linija = citac.readLine()) != null) {
				@SuppressWarnings("unchecked")
				Map<String, String> items = (Map<String, String>) yaml.load(linija);
				for (Map.Entry<String, String> item : items.entrySet()) {
					if (item.getValue() != null) {
						System.out.println(item);
						mapa.put(item.getKey(), item.getValue());
						keys.add(item.getKey());
					}
				}

			}
			
			while(true) {
				System.out.println("Izaberite opciju koju zelite da menjate ili unesite quit za izlaz");
				linija = sc.nextLine();
				if(linija.equals("quit"))
					break;
				if(!mapa.containsKey(linija)) {
					System.out.println("Ne postoji ta opcija! ");
					continue;
				}
				System.out.println("Unesite vrednost: ");
				mapa.replace(linija, sc.nextLine());
			}
			citac.close();
			BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(new File("resources/vezbe_03_yaml/en.yml")), "utf-8"));
			PrintWriter writer = new PrintWriter(new OutputStreamWriter(new FileOutputStream(new File("resources/vezbe_03_yaml/en_changed.yaml"))));
			linija = "";
			int indent = 0;
			while((linija = reader.readLine()) != null) {
				@SuppressWarnings("unchecked")
				Map<String, String> items = (Map<String, String>) yaml.load(linija);
				for (Map.Entry<String, String> item : items.entrySet()) {
					if (item.getValue() == null) {
						writer.printf("%s\n", linija);
						indent = StringUtils.countMatches(linija, " ");
					}else {
						String spaces = new String(new char[indent + 2]).replace('\0', ' ');
						writer.printf("%s%s: %s\n", spaces, item.getKey(), mapa.get(item.getKey()));
					}
				}	
			}
			writer.close();
			reader.close();
		}
		sc.close();

	}

}
