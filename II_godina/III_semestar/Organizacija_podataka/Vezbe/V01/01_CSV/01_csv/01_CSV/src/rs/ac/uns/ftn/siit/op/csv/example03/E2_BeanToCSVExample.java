package rs.ac.uns.ftn.siit.op.csv.example03;

import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.util.ArrayList;
import java.util.List;

import com.opencsv.bean.StatefulBeanToCsv;
import com.opencsv.bean.StatefulBeanToCsvBuilder;
import com.opencsv.exceptions.CsvDataTypeMismatchException;
import com.opencsv.exceptions.CsvRequiredFieldEmptyException;

public class E2_BeanToCSVExample {
	static final String[] countries = { "Australia,Canberra", "Canada,Ottawa", "China,Beijing", "France,Paris" };

	public static void main(String[] args) {
		List<E2_CountrySimple> coutryBeans = new ArrayList<>();

		for (String country : countries) {
			String[] countryAttributes = country.split(",");
			coutryBeans.add(new E2_CountrySimple(countryAttributes[0], countryAttributes[1]));
		}

		try (Writer writer = new FileWriter("resources/drzave_gradovi_beans.csv")) {
			StatefulBeanToCsv<E2_CountrySimple> beanToCsv = new StatefulBeanToCsvBuilder<E2_CountrySimple>(writer)
					.withApplyQuotesToAll(false).build(); // withApplyQuotesToAll(false) - da ne bi svaku vrednost uokvirio navondnicima
			beanToCsv.write(coutryBeans);

		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (CsvDataTypeMismatchException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (CsvRequiredFieldEmptyException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}
