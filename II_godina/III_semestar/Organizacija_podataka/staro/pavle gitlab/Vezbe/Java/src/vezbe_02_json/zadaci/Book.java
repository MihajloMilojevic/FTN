package vezbe_02_json.zadaci;

import java.util.List;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.JsonAutoDetect.Visibility;

@JsonAutoDetect(fieldVisibility = Visibility.ANY)
public class Book {
	private String ISBN;
	private double Price;
	private int Edition;
	private String Title;
	private List<Author> Authors;
	private List<String> Tags;
	private String Remark;
	
	
	@Override
	public String toString() {
		return "Book [ISBN=" + ISBN + ", Price=" + Price + ", Edition=" + Edition + ", Title=" + Title + ", Authors="
				+ Authors + ", Tags=" + Tags + ", Remark=" + Remark + "]";
	}
	public String getRemark() {
		return Remark;
	}
	public void setRemark(String remark) {
		Remark = remark;
	}
	public List<String> getTags() {
		return Tags;
	}
	public void setTags(List<String> tags) {
		this.Tags = tags;
	}
	public String getISBN() {
		return ISBN;
	}
	public void setISBN(String iSBN) {
		ISBN = iSBN;
	}
	public double getPrice() {
		return Price;
	}
	public void setPrice(double price) {
		Price = price;
	}
	public int getEdition() {
		return Edition;
	}
	public void setEdition(int edition) {
		Edition = edition;
	}
	public String getTitle() {
		return Title;
	}
	public void setTitle(String title) {
		Title = title;
	}
	public List<Author> getAuthors() {
		return Authors;
	}
	public void setAuthors(List<Author> authors) {
		Authors = authors;
	}
	
}
