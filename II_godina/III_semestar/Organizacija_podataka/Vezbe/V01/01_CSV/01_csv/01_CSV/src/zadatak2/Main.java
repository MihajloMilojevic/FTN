package zadatak2;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Objects;

import com.opencsv.CSVWriter;
import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;

public class Main {
	public static final String INPUT_FILE = "resources/studenti.csv";
	public static void main(String[] args) {
		try (Reader reader = new FileReader(INPUT_FILE)) {
			CsvToBean<Student> csv = new CsvToBeanBuilder<Student>(reader)
					.withType(Student.class).withSeparator(',').build();

			List<Student> students = csv.parse();
			Student s1 = new Student("a", "b", "c", 5);
			Student s2 = new Student("a", "b", "c", 5);
			System.out.println(s1.hashCode() == s2.hashCode());
			ArrayList<HashMap<StudentData, Integer> > ocene = new ArrayList<>();
			for(int i = 5; i <= 10; i++) {
				ocene.add(new HashMap<StudentData, Integer>());
			}
			HashMap<StudentData, ArrayList<Integer>> zb = new HashMap<>();
			for (Student s: students) {
				HashMap<StudentData, Integer> hm = ocene.get(s.ocena - 5);
				StudentData sd = new StudentData(s.index, s.ime);
				hm.put(sd, hm.getOrDefault(sd, 0) + 1);
				if (!zb.containsKey(sd)) {
					zb.put(sd, new ArrayList<Integer>());
				}
				if (s.ocena > 5) {
					zb.get(sd).add(s.ocena);
				}
			}
			
			for(Integer i = 5; i <= 10; i++) {
				printOcena("resources/ocena_" + i.toString() + ".csv", ocene.get(i-5));
			}
			
			printProsek("resources/prosek.csv", zb);
			

		} catch (FileNotFoundException e) {
			System.out.println("Could not open file");

		} catch (IOException e) {
			System.out.println("I/O error occured");

		}
	}
	static void printOcena(String fileName, HashMap<StudentData, Integer> hm) {
		try (FileWriter writer = new FileWriter(fileName)) {
			String[] data = new String[]{"index", "ime", "broj_ocena"};
			CSVWriter csv = new CSVWriter(writer);
			csv.writeNext(data);
			for (StudentData s: hm.keySet()) {
				data[0] = s.index;
				data[1] = s.ime;
				data[2] = hm.get(s).toString();
				csv.writeNext(data);
			}
			csv.close();
		}
		catch (Exception e) {
			System.out.println("Greska prilikom upisa u fajl " + fileName);
		}
	}
	static void printProsek(String fileName, HashMap<StudentData, ArrayList<Integer>> hm) {
		try (CSVWriter csv = new CSVWriter(new FileWriter(fileName)) ) {
			String[] data = new String[]{"index", "ime", "broj_ocena", "prosek"};
			csv.writeNext(data);
			for (StudentData s: hm.keySet()) {
				data[0] = s.index;
				data[1] = s.ime;
				ArrayList<Integer> ls = hm.get(s);
				double prosek = 0;
				for(int i: ls) prosek += i;
				if (ls.size() > 0) {
					prosek /= ls.size();
				}
				data[2] = Integer.toString(ls.size());
				data[3] = Double.toString(prosek);
				csv.writeNext(data);
			}
		}
		catch (Exception e) {
			System.out.println("Greska prilikom upisa u fajl " + fileName);
			System.err.println(e);
		}
	}
	private static class StudentData {
		public String index, ime;

		public StudentData(String index, String ime) {
			super();
			this.index = index;
			this.ime = ime;
		}

		@Override
		public int hashCode() {
			return Objects.hash(ime, index);
		}

		@Override
		public boolean equals(Object obj) {
			if (this == obj)
				return true;
			if (obj == null)
				return false;
			if (getClass() != obj.getClass())
				return false;
			StudentData other = (StudentData) obj;
			return Objects.equals(ime, other.ime) && Objects.equals(index, other.index);
		}
		
	}
}
