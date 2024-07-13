package vezbe_02_json.zadaci;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.JsonAutoDetect.Visibility;
import com.opencsv.bean.CsvBindByPosition;

@JsonAutoDetect(fieldVisibility = Visibility.ANY)
public class Country {
	@CsvBindByPosition(position = 0, required = true)
	private String CountryName;
	@CsvBindByPosition(position = 1, required = true)
	private String CapitalName;
	@CsvBindByPosition(position = 2, required = true)
	private double CapitalLatitude;
	@CsvBindByPosition(position = 3, required = true)
	private double CapitalLongitude;
	@CsvBindByPosition(position = 4, required = true)
	private String CountryCode;
	@CsvBindByPosition(position = 5, required = true)
	private String ContinentName;
	
	public Country() {
		
	}
	public Country(String countryName, String capitalName, double capitalLatitude, double capitalLongitude,
			String countryCode, String continentName) {
		super();
		CountryName = countryName;
		CapitalName = capitalName;
		CapitalLatitude = capitalLatitude;
		CapitalLongitude = capitalLongitude;
		CountryCode = countryCode;
		ContinentName = continentName;
	}
	public String getCountryName() {
		return CountryName;
	}
	public void setCountryName(String countryName) {
		CountryName = countryName;
	}
	public String getCapitalName() {
		return CapitalName;
	}
	public void setCapitalName(String capitalName) {
		CapitalName = capitalName;
	}
	public double getCapitalLatitude() {
		return CapitalLatitude;
	}
	public void setCapitalLatitude(double capitalLatitude) {
		CapitalLatitude = capitalLatitude;
	}
	public double getCapitalLongitude() {
		return CapitalLongitude;
	}
	public void setCapitalLongitude(double capitalLongitude) {
		CapitalLongitude = capitalLongitude;
	}
	public String getCountryCode() {
		return CountryCode;
	}
	public void setCountryCode(String countryCode) {
		CountryCode = countryCode;
	}
	public String getContinentName() {
		return ContinentName;
	}
	public void setContinentName(String continentName) {
		ContinentName = continentName;
	}
	@Override
	public String toString() {
		return "Country [CountryName=" + CountryName + ", CapitalName=" + CapitalName + ", CapitalLatitude="
				+ CapitalLatitude + ", CapitalLongitude=" + CapitalLongitude + ", CountryCode=" + CountryCode
				+ ", ContinentName=" + ContinentName + "]";
	}
	
	
}
