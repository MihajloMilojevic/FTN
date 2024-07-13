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

import vezbe_03_yaml.example03.Address;
import vezbe_03_yaml.example03.Invoice;

public class Zadatak1 {

	public static void main(String args[]) throws IOException {

		Yaml yaml = new Yaml(new Constructor(Invoice.class));
		Map<String, Invoice> mapa = new HashMap<>();
		Invoice invoice = null;
		try (InputStream input = new FileInputStream(new File("resources/vezbe_03_yaml/invoice.yaml"));) {
			invoice = (Invoice) yaml.load(input);
			mapa.put(invoice.billTo.given + " " + invoice.billTo.family, invoice);
		} catch(Exception e) {
			e.printStackTrace();
		}
		
		Scanner sc = new Scanner(System.in);
		String ime;
	
		while(true) {
			System.out.println("Unesite ime i prezime ili izlaz za izlaz: ");
			ime = sc.nextLine();
			if(ime.equals("izlaz"))
				break;
			if(mapa.containsKey(ime)) {
				int o = 0;
				Address adr = mapa.get(ime).billTo.address;
				System.out.println("Da li zelite da promenite grad? 0 - ne; 1 - da; ");
				o = sc.nextInt();
				sc.nextLine();
				if(o == 1) {
					String s = sc.nextLine();
					adr.city = s;
				}
				
				System.out.println("Da li zelite da promenite drzavu? 0 - ne; 1 - da; ");
				o = sc.nextInt();
				sc.nextLine();
				if(o == 1) {
					String s = sc.nextLine();
					adr.state = s;
				}
				
				System.out.println("Da li zelite da promenite ulicu i broj? 0 - ne; 1 - da; ");
				o = sc.nextInt();
				sc.nextLine();
				if(o == 1) {
					String s = "";
					while (sc.hasNextLine()){
					    String citan = sc.nextLine();
					    if(citan == null || citan.isEmpty()){
					        break;
					    }
					    s += citan + '\n';
					}
					adr.lines = s;
				}
				
				System.out.println("Da li zelite da promenite postal code? 0 - ne; 1 - da; ");
				o = sc.nextInt();
				sc.nextLine();
				if(o == 1) {
					String s = sc.nextLine();
					adr.postal = s;
				}
			} else {
				System.out.println("Ne postoji takav korisnik!");
			}
		}
		
		yaml = new Yaml();
		FileWriter writer = new FileWriter("resources/vezbe_03_yaml/invoice_mod.yaml");
		yaml.dump(invoice, writer);
		sc.close();
	}

}
