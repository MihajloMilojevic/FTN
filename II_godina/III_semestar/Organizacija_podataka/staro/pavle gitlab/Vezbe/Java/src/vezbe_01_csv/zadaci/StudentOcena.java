package vezbe_01_csv.zadaci;

import com.opencsv.bean.CsvBindByPosition;

public class StudentOcena {
	@CsvBindByPosition(position = 0, required = true)
	private String index;
	@CsvBindByPosition(position = 1, required = true)
	private String ime;
	@CsvBindByPosition(position = 2, required = true)
	private String prezime;
	@CsvBindByPosition(position = 3, required = true)
	private String predmet;
	@CsvBindByPosition(position = 4, required = true)
	private int ocena;
	
	public StudentOcena() {
		
	}
	public StudentOcena(String index, String ime, String prezime, String predmet, int ocena) {
		super();
		this.index = index;
		this.ime = ime;
		this.prezime = prezime;
		this.predmet = predmet;
		this.ocena = ocena;
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
	public String getPrezime() {
		return prezime;
	}
	public void setPrezime(String prezime) {
		this.prezime = prezime;
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
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((ime == null) ? 0 : ime.hashCode());
		result = prime * result + ((index == null) ? 0 : index.hashCode());
		result = prime * result + ((prezime == null) ? 0 : prezime.hashCode());
		return result;
	}
	
	public String id() {
		return index + " " + ime + " " + prezime;
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		StudentOcena other = (StudentOcena) obj;
		if (ime == null) {
			if (other.ime != null)
				return false;
		} else if (!ime.equals(other.ime))
			return false;
		if (index == null) {
			if (other.index != null)
				return false;
		} else if (!index.equals(other.index))
			return false;
		if (prezime == null) {
			if (other.prezime != null)
				return false;
		} else if (!prezime.equals(other.prezime))
			return false;
		return true;
	}
	@Override
	public String toString() {
		return "Student [index=" + index + ", ime=" + ime + ", prezime=" + prezime + ", predmet=" + predmet + ", ocena="
				+ ocena + "]";
	}
	
	
	
	
}
