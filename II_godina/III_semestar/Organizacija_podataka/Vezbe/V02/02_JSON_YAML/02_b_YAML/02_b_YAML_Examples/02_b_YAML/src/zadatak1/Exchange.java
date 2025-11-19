package zadatak1;

public class Exchange {
	private String name;
	private double value;
	
	public Exchange() {
		super();
	}
	public Exchange(String name, double value) {
		super();
		this.name = name;
		this.value = value;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public double getValue() {
		return value;
	}
	public void setValue(double value) {
		this.value = value;
	}
}
