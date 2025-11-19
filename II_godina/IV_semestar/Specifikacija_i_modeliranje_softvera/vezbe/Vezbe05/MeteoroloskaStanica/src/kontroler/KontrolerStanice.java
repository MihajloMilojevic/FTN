package kontroler;

import model.DnevnaTemperatura;

/**
 * KontrolerStanice - klasa koja implementira kontroler deo MVC paterna
 */
public class KontrolerStanice {
	private DnevnaTemperatura dnevnaTemperatuera;   // model
	
	public KontrolerStanice(DnevnaTemperatura dnevnaTemperatura) {
		this.dnevnaTemperatuera = dnevnaTemperatura;
	}
	
	/**
	 * unosNoveTemperature - prima ulaz od prozora (sadržaj unetog stringa), vrši provere, prevodi ga u broj  
	 * i poziva metodu iz modela
	 */
	public void unosNoveTemperature(String unetaTemperatura) {
		if (unetaTemperatura == null)
			throw new NullPointerException();
		float temperatura =  Float.parseFloat(unetaTemperatura);  //potencijalno baca NumberFormatException			
		dnevnaTemperatuera.dodajTemperaturu(temperatura);
	}	
}


