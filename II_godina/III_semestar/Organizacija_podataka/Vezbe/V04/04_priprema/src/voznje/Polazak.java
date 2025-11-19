package voznje;

public class Polazak {
	public Relacija relacija;
	public String datumPolaska;
	public String vremePolaska;
	public String vremeDolaska;
	public String peron;
	public double cenaKarte;
	public int brojPutnika;
	
	public Polazak(String[] linija) {
		this.relacija = new Relacija(linija);
        this.datumPolaska = linija[3];
        this.vremePolaska = linija[4];
        this.vremeDolaska = linija[5];
        this.peron = linija[6];
        this.cenaKarte = Double.parseDouble(linija[7]);
        this.brojPutnika = Integer.parseInt(linija[8]);
	}
	
	public Polazak() {
		super();
	}

	public int getTrajanje() {
		int polazak = Integer.parseInt(vremePolaska.split(":")[0]) * 60 + Integer.parseInt(vremePolaska.split(":")[1]);
        int dolazak = Integer.parseInt(vremeDolaska.split(":")[0]) * 60 + Integer.parseInt(vremeDolaska.split(":")[1]);
        return dolazak - polazak;
	}

	public double getProfit() {
		return cenaKarte * brojPutnika;
	}

	public Polazak(String relacija, String polazak, String dolazak, String datum, String vremePolaska,
			String vremeDolaska, String peron, double cenaKarte, int brojPutnika) {
		super();
		this.relacija = new Relacija(relacija, polazak, dolazak);
		this.datumPolaska = datum;
		this.vremePolaska = vremePolaska;
		this.vremeDolaska = vremeDolaska;
		this.peron = peron;
		this.cenaKarte = cenaKarte;
		this.brojPutnika = brojPutnika;
	}

	public Relacija getRelacija() {
		return relacija;
	}

	public void setRelacija(Relacija relacija) {
		this.relacija = relacija;
	}

	
	public String getDatum() {
		return datumPolaska;
	}

	public void setDatum(String datum) {
		this.datumPolaska = datum;
	}

	public String getVremePolaska() {
		return vremePolaska;
	}

	public void setVremePolaska(String vremePolaska) {
		this.vremePolaska = vremePolaska;
	}

	public String getVremeDolaska() {
		return vremeDolaska;
	}

	public void setVremeDolaska(String vremeDolaska) {
		this.vremeDolaska = vremeDolaska;
	}

	public String getPeron() {
		return peron;
	}

	public void setPeron(String peron) {
		this.peron = peron;
	}

	public double getCenaKarte() {
		return cenaKarte;
	}

	public void setCenaKarte(double cenaKarte) {
		this.cenaKarte = cenaKarte;
	}

	public int getBrojPutnika() {
		return brojPutnika;
	}

	public void setBrojPutnika(int brojPutnika) {
		this.brojPutnika = brojPutnika;
	}
}
