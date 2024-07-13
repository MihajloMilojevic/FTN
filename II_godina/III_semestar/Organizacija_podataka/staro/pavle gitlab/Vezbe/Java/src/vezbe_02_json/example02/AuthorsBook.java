package vezbe_02_json.example02;

public class AuthorsBook {
	private String firstName;
	private String lastName;
	private String bookTitle;

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public String getBookTitle() {
		return bookTitle;
	}

	public void setBookTitle(String bookTitle) {
		this.bookTitle = bookTitle;
	}

	@Override
	public String toString() {
		return "AuthorsBook [firstName=" + firstName + ", lastName=" + lastName + ", bookTitle=" + bookTitle + "]";
	}

}
