package voznje;

import java.util.ArrayList;

public class Z1JSONResult {
	public String sifra;
	public String polaziste;
	public String odrediste;
	public ArrayList<PolazakRedukovano> polasci;
	
	public Z1JSONResult(Relacija r) {
		sifra = r.sifra;
		polaziste = r.polaziste;
		odrediste = r.odrediste;
		polasci = new ArrayList<Z1JSONResult.PolazakRedukovano>();
	}
	
	public Z1JSONResult() {
		super();
		polasci = new ArrayList<Z1JSONResult.PolazakRedukovano>();
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

	public ArrayList<PolazakRedukovano> getPolasci() {
		return polasci;
	}

	public void setPolasci(ArrayList<PolazakRedukovano> polasci) {
		this.polasci = polasci;
	}

	public Z1JSONResult(String sifra, String polaziste, String odrediste, ArrayList<PolazakRedukovano> polasci) {
		super();
		this.sifra = sifra;
		this.polaziste = polaziste;
		this.odrediste = odrediste;
		this.polasci = polasci;
	}

	public static class PolazakRedukovano {
		public String datumPolaska;
		public String vremePolaska;
		public String vremeDolaska;
		public String peron;
		public double cenaKarte;
		public int brojPutnika;
		
		public PolazakRedukovano(Polazak p) {
			datumPolaska = p.datumPolaska;
			vremePolaska = p.vremePolaska;
			vremeDolaska = p.vremeDolaska;
			peron = p.peron;
			cenaKarte = p.cenaKarte;
			brojPutnika = p.brojPutnika;
		}
		
		public PolazakRedukovano() {
			super();
		}


		public PolazakRedukovano(String datum, String vremePolaska,
				String vremeDolaska, String peron, double cenaKarte, int brojPutnika) {
			super();
			this.datumPolaska = datum;
			this.vremePolaska = vremePolaska;
			this.vremeDolaska = vremeDolaska;
			this.peron = peron;
			this.cenaKarte = cenaKarte;
			this.brojPutnika = brojPutnika;
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
}
