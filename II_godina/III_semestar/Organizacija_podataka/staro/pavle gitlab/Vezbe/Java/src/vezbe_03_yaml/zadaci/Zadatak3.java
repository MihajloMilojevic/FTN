package vezbe_03_yaml.zadaci;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.constructor.Constructor;

import vezbe_03_yaml.example03.Invoice;
import vezbe_03_yaml.example03.Product;

public class Zadatak3 {

	public static void main(String[] args) throws IOException {
		Yaml yaml = new Yaml(new Constructor(Invoice.class));
		Invoice invoice = null;
		List<Product> lista = new ArrayList<Product>();
		try (InputStream input = new FileInputStream(new File("resources/vezbe_03_yaml/invoice.yaml"));) {
			invoice = (Invoice) yaml.load(input);
			lista = new ArrayList<>(invoice.product);
		} catch(Exception e) {
			e.printStackTrace();
		}
		Float t = invoice.tax;
		Float total = invoice.total;
		Float p = t / total;
		for(int i = 1; i <= lista.size(); i++)
		{
			FileWriter writer = new FileWriter("resources/vezbe_03_yaml/invoice_" + String.valueOf(i) + ".yaml");
			Product pr = lista.get(i - 1);
			invoice.tax = p * pr.price;
			invoice.total = pr.price;
			invoice.product = new ArrayList<>();
			invoice.product.add(pr);
			yaml.dump(invoice, writer);
		}
		

	}

}
