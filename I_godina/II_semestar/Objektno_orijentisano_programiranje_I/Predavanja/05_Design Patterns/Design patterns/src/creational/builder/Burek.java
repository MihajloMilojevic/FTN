package creational.builder;

public class Burek {
	private String ime;
	private String testo;
	private String fil;
	
	public String getIme() {
		return ime;
	}
	public void setIme(String ime) {
		this.ime = ime;
	}
	public String getTesto() {
		return testo;
	}
	public void setTesto(String testo) {
		this.testo = testo;
	}
	public String getFil() {
		return fil;
	}
	public void setFil(String fil) {
		this.fil = fil;
	}
	public String toString() {
		return "Ime: " + ime + ", testo: " + testo + ", fil: " + fil; 
	}
}
