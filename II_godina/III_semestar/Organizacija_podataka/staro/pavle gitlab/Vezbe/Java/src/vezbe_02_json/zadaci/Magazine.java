package vezbe_02_json.zadaci;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.JsonAutoDetect.Visibility;

@JsonAutoDetect(fieldVisibility = Visibility.ANY)
public class Magazine {
	private String Title;
	private String Month;
	private int Year;
	public String getTitle() {
		return Title;
	}
	
	
	@Override
	public String toString() {
		return "Magazine [Title=" + Title + ", Month=" + Month + ", Year=" + Year + "]";
	}


	public void setTitle(String title) {
		Title = title;
	}
	public String getMonth() {
		return Month;
	}
	public void setMonth(String month) {
		Month = month;
	}
	public int getYear() {
		return Year;
	}
	public void setYear(int year) {
		Year = year;
	}
	
	
}
