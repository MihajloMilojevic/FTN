package zadatak2;

import java.util.Objects;

import com.opencsv.bean.CsvBindByName;

public class Student {
	@Override
	public int hashCode() {
		return index.hashCode();
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Student other = (Student) obj;
		return Objects.equals(ime, other.ime) && Objects.equals(index, other.index) && ocena == other.ocena
				&& Objects.equals(predmet, other.predmet);
	}
	@CsvBindByName(column = "index", required=true)
	public String index;
	@CsvBindByName(column = "ime", required=true)
	public String ime;
	@CsvBindByName(column = "predmet", required=true)
	public String predmet;
	@CsvBindByName(column = "ocena", required=true)
	public int ocena;
	public Student(String index, String ime, String predmet, int ocena) {
		super();
		this.index = index;
		this.ime = ime;
		this.predmet = predmet;
		this.ocena = ocena;
	}
	public Student() {
		super();
	}
	public String getIndex() {
		return index;
	}
	public void setIndex(String index) {
		this.index = index;
	}
	public String getIme() {
		return ime;
	}
	public void setIme(String ime) {
		this.ime = ime;
	}
	public String getPredmet() {
		return predmet;
	}
	public void setPredmet(String predmet) {
		this.predmet = predmet;
	}
	public int getOcena() {
		return ocena;
	}
	public void setOcena(int ocena) {
		this.ocena = ocena;
	}
}
