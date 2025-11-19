package zadatak1;

public class Person {
	private String given;
	private String family;
	private Address address;

	public Person() {
		super();
	}

	public Person(String given, String family, Address address) {
		super();
		this.given = given;
		this.family = family;
		this.address = address;
	}

	public Person(Person person) {
		this.given = person.getGiven();
		this.family = person.getFamily();
		this.address = new Address(person.getAddress());
	}

	public String getGiven() {
		return given;
	}

	public void setGiven(String given) {
		this.given = given;
	}

	public String getFamily() {
		return family;
	}

	public void setFamily(String family) {
		this.family = family;
	}

	public Address getAddress() {
		return address;
	}

	public void setAddress(Address address) {
		this.address = address;
	}

	@Override
	public String toString() {
		return "Person [given=" + given + ", family=" + family + ", address=" + address + "]";
	}

}
