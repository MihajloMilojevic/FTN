package dogadjaj;

/**
 * Publisher interfejs treba da implementiraju svi koji zele da omoguće 
 * drugima praćenje promena koje se dešavaju nad njihovim podacima ili stanjem
 */
public interface Publisher {			
	//Metoda za dodavanje posmatrača (pretplata na praćenje promena) 
	public void addObserver(Observer observer);
	//Metoda za uklanjanje posmatrača  
	public void removeObserver(Observer observer);
	//Metoda za obaveštavanje svih koji posmatrača da je došlo do promene
	public void notifyObservers();
}
