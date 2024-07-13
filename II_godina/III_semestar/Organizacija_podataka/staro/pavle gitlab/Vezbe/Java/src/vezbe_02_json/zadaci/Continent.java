package vezbe_02_json.zadaci;

import java.util.List;

public class Continent {
	private String ContinentName;
	private List<Country> Countries;
	public String getContinentName() {
		return ContinentName;
	}
	public void setContinentName(String continentName) {
		ContinentName = continentName;
	}
	public List<Country> getCountries() {
		return Countries;
	}
	public void setCountries(List<Country> countries) {
		this.Countries = countries;
	}
	
}
