package zadatak1;

public class Address {
	private String lines;
	private String city;
	private String state;
	private String postal;

	public Address() {
		super();
	}

	public Address(String lines, String city, String state, String postal) {
		super();
		this.lines = lines;
		this.city = city;
		this.state = state;
		this.postal = postal;
	}

	public Address(Address address) {
		this.lines = address.getLines();
		this.city = address.getCity();
		this.state = address.getState();
		this.postal = address.getPostal();
	}

	public String getLines() {
		return lines;
	}

	public void setLines(String lines) {
		this.lines = lines;
	}

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public String getState() {
		return state;
	}

	public void setState(String state) {
		this.state = state;
	}

	public String getPostal() {
		return postal;
	}

	public void setPostal(String postal) {
		this.postal = postal;
	}

	@Override
	public String toString() {
		return "Address [lines=" + lines + ", city=" + city + ", state=" + state + ", postal=" + postal + "]";
	}

}
