package vezbe_03_yaml.zadaci;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import vezbe_03_yaml.example03.Invoice;
import vezbe_03_yaml.example03.Product;

public class Zadatak2 {

	@SuppressWarnings("unchecked")
	public static void main(String[] args) throws IOException {
		Yaml yaml = new Yaml();
		Map<String, Double> mapa = new HashMap<>();
		Invoice invoice = null;
		try (InputStream input = new FileInputStream(new File("resources/vezbe_03_yaml/exchange.yaml"));) {
			mapa = (Map<String, Double>) yaml.load(input);
		} catch(Exception e) {
			e.printStackTrace();
		}
		System.out.println("Moguce valute i kurs: ");
		for (String string : mapa.keySet()) {
			System.out.println(string + " " + mapa.get(string));
		}
		Scanner sc = new Scanner(System.in);
		String val = "";
		while(true) {
			System.out.println("Izaberite valutu (izlaz za izlaz): ");
			val = sc.nextLine();
			if(val.equals("izlaz"))
				break;
			if(!mapa.containsKey(val)) {
				System.out.println("Ne postoji ta valuta! ");
				continue;
			}
			break;
		}
		
		yaml = new Yaml(new Constructor(Invoice.class));
		try (InputStream input = new FileInputStream(new File("resources/vezbe_03_yaml/invoice.yaml"));) {
			invoice = (Invoice) yaml.load(input);
		} catch(Exception e) {
			e.printStackTrace();
		}
		if(!val.equals("izlaz")) {
			Float k = (mapa.get(val)).floatValue();
			invoice.total *= k;
			for(Product p : invoice.product) {
				p.price *= k;
			}
			invoice.tax *= k;
			yaml = new Yaml();
			FileWriter writer = new FileWriter("resources/vezbe_03_yaml/invoice_" + val + ".yaml");
			yaml.dump(invoice, writer);
			sc.close();
		}
		System.out.println(invoice);
		
		
	}

}
