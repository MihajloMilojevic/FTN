package voznje;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import com.fasterxml.jackson.databind.ObjectMapper;

import voznje.Z1JSONResult.PolazakRedukovano;

public class Test {

	public static void main(String[] args) {
		ObjectMapper mapper = new ObjectMapper();
		try {
			//Podaci p = mapper.readValue(new File("resources/test.json"), Podaci.class);
			//List<Data> lista = mapper.readValue(new File("resources/relacije.json"), new TypeReference<List<Data>>(){});
			@SuppressWarnings("unchecked")
			List<Map<String, Object>> lista = mapper.readValue(new File("resources/relacije.json"), ArrayList.class);
			for (Map<String, Object> m : lista) {
				//Data d = new Data((LinkedHashMap<String, Object>) o);
                System.out.println(m.get("sifra"));
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public static class Podaci {
		public ArrayList<Data> podaci;
	}
	public static class Data {
		public String sifra;
		public String polaziste;
		public String odrediste;
		public List<PolazakRedukovano> polasci;
		public Data(LinkedHashMap<String, Object> hm) {
			sifra = (String) hm.get("sifra");
			polaziste = (String) hm.get("polaziste");
			odrediste = (String) hm.get("odrediste");
			polasci = new ArrayList<PolazakRedukovano>();
			@SuppressWarnings("unchecked")
			ArrayList<LinkedHashMap<String, Object>> polasciHM = (ArrayList<LinkedHashMap<String, Object>>) hm.get("polasci");
		}
		public String getSifra() {
			return sifra;
		}
		public void setSifra(String sifra) {
			this.sifra = sifra;
		}
		public String getPolaziste() {
			return polaziste;
		}
		public void setPolaziste(String polaziste) {
			this.polaziste = polaziste;
		}
		public String getOdrediste() {
			return odrediste;
		}
		public void setOdrediste(String odrediste) {
			this.odrediste = odrediste;
		}
		public List<PolazakRedukovano> getPolasci() {
			return polasci;
		}
		public void setPolasci(List<PolazakRedukovano> polasci) {
			this.polasci = polasci;
		}
		public Data() {
			super();
		}
		public Data(String sifra, String polaziste, String odrediste, List<PolazakRedukovano> polasci) {
			super();
			this.sifra = sifra;
			this.polaziste = polaziste;
			this.odrediste = odrediste;
			this.polasci = polasci;
		}
	}
}
