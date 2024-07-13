package vezbe_04;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.JsonAutoDetect.Visibility;
import com.opencsv.bean.CsvBindByPosition;

@JsonAutoDetect(fieldVisibility = Visibility.ANY)
public class Putanja {
	@CsvBindByPosition(position = 0, required = true)
	private String id;
	@CsvBindByPosition(position = 1, required = true)
	private String mestoPolaska;
	@CsvBindByPosition(position = 2, required = true)
	private String mestoDolaska;
	@CsvBindByPosition(position = 3, required = true)
	private String datumPolaska;
	@CsvBindByPosition(position = 4, required = true)
	private String datumDolaska;
	@CsvBindByPosition(position = 5, required = true)
	private String vremeDolaska;
	@CsvBindByPosition(position = 6, required = true)
	private String vremePolaska;
	@CsvBindByPosition(position = 7, required = true)
	private String stanicniPeron;
	@CsvBindByPosition(position = 8, required = true)
	private Double cenaKarte;
	@CsvBindByPosition(position = 9, required = true)
	private Integer prodateKarte;
	
	
	
	public Putanja(){
		
	}
	
	public Putanja(String id, String mestoPolaska, String mestoDolaska, String datumPolaska, String datumDolaska,
			String vremeDolaska, String vremePolaska, String stanicniPeron, Double cenaKarte, Integer prodateKarte) {
		super();
		this.id = id;
		this.mestoPolaska = mestoPolaska;
		this.mestoDolaska = mestoDolaska;
		this.datumPolaska = datumPolaska;
		this.datumDolaska = datumDolaska;
		this.vremeDolaska = vremeDolaska;
		this.vremePolaska = vremePolaska;
		this.stanicniPeron = stanicniPeron;
		this.cenaKarte = cenaKarte;
		this.prodateKarte = prodateKarte;
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getMestoPolaska() {
		return mestoPolaska;
	}
	public void setMestoPolaska(String mestoPolaska) {
		this.mestoPolaska = mestoPolaska;
	}
	public String getMestoDolaska() {
		return mestoDolaska;
	}
	public void setMestoDolaska(String mestoDolaska) {
		this.mestoDolaska = mestoDolaska;
	}
	public String getDatumPolaska() {
		return datumPolaska;
	}
	public void setDatumPolaska(String datumPolaska) {
		this.datumPolaska = datumPolaska;
	}
	public String getDatumDolaska() {
		return datumDolaska;
	}
	public void setDatumDolaska(String datumDolaska) {
		this.datumDolaska = datumDolaska;
	}
	public String getVremeDolaska() {
		return vremeDolaska;
	}
	public void setVremeDolaska(String vremeDolaska) {
		this.vremeDolaska = vremeDolaska;
	}
	public String getVremePolaska() {
		return vremePolaska;
	}
	public void setVremePolaska(String vremePolaska) {
		this.vremePolaska = vremePolaska;
	}
	public String getStanicniPeron() {
		return stanicniPeron;
	}
	public void setStanicniPeron(String stanicniPeron) {
		this.stanicniPeron = stanicniPeron;
	}
	public Double getCenaKarte() {
		return cenaKarte;
	}
	public void setCenaKarte(Double cenaKarte) {
		this.cenaKarte = cenaKarte;
	}
	public Integer getProdateKarte() {
		return prodateKarte;
	}
	public void setProdateKarte(Integer prodateKarte) {
		this.prodateKarte = prodateKarte;
	}

	@Override
	public String toString() {
		return "Putanja [id=" + id + ", mestoPolaska=" + mestoPolaska + ", mestoDolaska=" + mestoDolaska
				+ ", datumPolaska=" + datumPolaska + ", datumDolaska=" + datumDolaska + ", vremeDolaska=" + vremeDolaska
				+ ", vremePolaska=" + vremePolaska + ", stanicniPeron=" + stanicniPeron + ", cenaKarte=" + cenaKarte
				+ ", prodateKarte=" + prodateKarte + "]";
	}
	
	
	
}
