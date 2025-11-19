package model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Date;
import java.util.List;

import dogadjaj.Observer;
import dogadjaj.Publisher;
import dogadjaj.UpdateEvent;

/**
 * DnevnaTemperatura - Klasa koja čuva izmerene dnevne temeraturu na jednom mernom mestu u jednom danu
 */
public class DnevnaTemperatura implements Publisher {
	public static final float MAX_TEMP = 50;
	public static final float MIN_TEMP = -50;
	
	private Date datum;
	private List<Float> izmereneVrednosti = null;
	private float minVrednost = MAX_TEMP;
	private float maxVrednost = MIN_TEMP;	
	
	public DnevnaTemperatura() {
		datum = new Date();  // današnji datum
	}
	
	public Date getDatum() {
		return datum;
	}

	/**
	 * getIzmereneVrednosti - vraća listu koja se ne može modifikovati
	 */
	public List<Float> getIzmereneVrednosti() {
		if (null == izmereneVrednosti) 
			return null;
		return Collections.unmodifiableList(izmereneVrednosti);
	}

	public float getMinVrednost() {
		return minVrednost;
	}

	public float getMaxVrednost() {
		return maxVrednost;
	}			
	
	/**
	 * dodajTemperaturu - metoda za dodavanje temperature u listu temperatura, uz različite provere	 
	 */
	public void dodajTemperaturu(float temperatura) {		
		if (null == izmereneVrednosti) {
			izmereneVrednosti = new ArrayList<Float>(); // lazy inicijalizacija - kreiramo listu samo kada za njom postoji potreba
		}
		if (temperatura > MAX_TEMP || temperatura < MIN_TEMP)
			throw new IllegalArgumentException(String.format("Temperatura mora biti u opsegu [%f, %f]", MIN_TEMP, MAX_TEMP));						
		
		if (temperatura < minVrednost)
			minVrednost = temperatura;
		if (temperatura > maxVrednost)
			maxVrednost = temperatura;
		izmereneVrednosti.add(temperatura);		
		
		//Obaveštavanje da je došlo do promena
		notifyObservers();
	}
	
	/**
	 * srednjaVrednost - metoda za računanje srednje vrednosti	 
	 */
	public float srednjaVrednost() {		
		if (null == izmereneVrednosti) 
			throw new NullPointerException();
		
		int brojElemenata = izmereneVrednosti.size();		
		float suma = 0;
		for (int i = 0; i < brojElemenata; i++) {
			suma += izmereneVrednosti.get(i);
		}
		return suma / brojElemenata;
	}
		
	/**
	 * List<Observer> observers - lista onih koji "osluskuju" odnosno posmatraju promenu podataka  (Observer pattern)	
	 * Više razlicitih elemenata korisnickog interfejsa (cak i oni koji nisu poznati u trenutku inicijalnog dizajna aplikacije) 
	 * se mogu registrovati da slusaju promene 
	 */
	private List<Observer> observers; 
		
	/**
	 * addObserver - metoda za dodavanje observera (pretplata na slusanje)   
	 */ 
	@Override
	public void addObserver(Observer observer) {
		if (null == observers)
			observers = new ArrayList<Observer>();
		observers.add(observer);
	}
		
	/**
	 * removeObserver - Metoda za uklanjanje obzervera   
	 */
	@Override
	public void removeObserver(Observer observer) {
		if (null == observers)
			return;
		observers.remove(observer);
	}	
	
	/**
	 * notifyObservers - Metoda za slanje dogadjaja da se desila promena svima koji su se registrovali za pracenje promena  
	 */
	@Override
	public void notifyObservers() {
		//Kreiranje događaja koji opisuje promenu
		//Trenutno je to samo generički događaj
		UpdateEvent e = new UpdateEvent(this);
		for (Observer observer : observers) {
			observer.updatePerformed(e);
		}			
	}
}
