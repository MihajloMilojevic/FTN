package aplikacija;

import kontroler.KontrolerStanice;
import model.DnevnaTemperatura;
import pogled.ProzorMeteoroloskeStanice;

public class Aplikacija {

	public static void main(String[] args) {
		DnevnaTemperatura dnevnaTemperatura = new DnevnaTemperatura();
		KontrolerStanice kontroler = new KontrolerStanice(dnevnaTemperatura);
		ProzorMeteoroloskeStanice prozor = new ProzorMeteoroloskeStanice(dnevnaTemperatura, kontroler);	
		prozor.setVisible(true);				
	}
}
