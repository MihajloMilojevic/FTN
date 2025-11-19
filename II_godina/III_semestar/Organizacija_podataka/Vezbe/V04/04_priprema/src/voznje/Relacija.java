package voznje;

import java.util.Objects;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.JsonAutoDetect.Visibility;

@JsonAutoDetect(fieldVisibility = Visibility.ANY)
public class Relacija {
	public String sifra;
	public String polaziste;
	public String odrediste;
	public Relacija(String sifra, String polaziste, String odrediste) {
		super();
		this.sifra = sifra;
		this.polaziste = polaziste;
		this.odrediste = odrediste;
	}
	public Relacija() {
		super();
	}
	public Relacija(String[] linija) {
		sifra = linija[0];
		polaziste = linija[1];
		odrediste = linija[2];
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
	@Override
	public int hashCode() {
		return Objects.hash(odrediste, polaziste, sifra);
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Relacija other = (Relacija) obj;
		return Objects.equals(odrediste, other.odrediste) && Objects.equals(polaziste, other.polaziste)
				&& Objects.equals(sifra, other.sifra);
	}
	public boolean povratak(Relacija s) {
		return polaziste.equalsIgnoreCase(s.odrediste) && odrediste.equalsIgnoreCase(s.polaziste);
	}
	
}
