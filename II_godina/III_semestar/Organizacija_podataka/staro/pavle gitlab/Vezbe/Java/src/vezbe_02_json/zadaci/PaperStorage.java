package vezbe_02_json.zadaci;

import java.util.List;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.JsonAutoDetect.Visibility;

@JsonAutoDetect(fieldVisibility = Visibility.ANY)
public class PaperStorage {
	List<Book> Books;
	List<Magazine> Magazines;
	
	public List<Book> getBooks() {
		return Books;
	}
	public void setBooks(List<Book> books) {
		Books = books;
	}
	public List<Magazine> getMagazines() {
		return Magazines;
	}
	public void setMagazines(List<Magazine> magazines) {
		Magazines = magazines;
	}

	
	
}
