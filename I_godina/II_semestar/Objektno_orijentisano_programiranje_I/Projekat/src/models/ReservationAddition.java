package models;

import java.text.ParseException;

public class ReservationAddition extends Model {

	/* ******************************  ATTRIBUTES  *************************************** */
	// Attributes in the database
	private String name;
	
	public ReservationAddition() {
		super();
		this.name = "";
	}

	public ReservationAddition(String name) {
		super();
        this.name = name;
	}
	
	public ReservationAddition(String id, String name) {
		super(id);
		this.name = name;
	}
	
	/* ******************************  METHODS  *************************************** */
	
	@Override
	public boolean isValid() {
		if (this.name == null || this.name.isEmpty()) return false;
		return super.isValid();
	}
	
	@Override
	public Object get(String key) throws IllegalArgumentException {
		switch (key) {
		case "name":
			return (Object) this.name;
		default:
			return super.get(key);
		}
	}
	@Override
	public void set(String key, Object value) throws IllegalArgumentException {
		switch (key) {
		case "name":
			this.name = (String) value;
			break;
		default:
			super.set(key, value);
		}
	}
	@Override
	public void update(Model newModel) throws IllegalArgumentException {
		super.update(newModel);
		if (!(newModel instanceof ReservationAddition)) throw new IllegalArgumentException("Not  a ReservationAddition object");
		this.name = (String) newModel.get("name");
	}
	@Override
	public String toString() {
		return String.join(";", new String[] {super.toString(), this.name});
	}
	@Override
	public boolean equals(Object obj) {
		if (obj == this) {
			return true;
		}
		if (obj == null || obj.getClass() != this.getClass()) {
			return false;
		}
		ReservationAddition ReservationAddition = (ReservationAddition) obj;
		return super.equals(obj) && this.name.equals(ReservationAddition.name);
	}
	@Override
	public Object clone() throws CloneNotSupportedException {
		ReservationAddition ra = new ReservationAddition(this.getId(), this.name);
		if (this.isDeleted()) ra.delete();
		return ra;
	}
	@Override
	public Model fromCSV(String csv) throws ParseException {
		super.fromCSV(csv);
		String[] values = csv.split(";");
		if (values.length < 3) throw new ParseException("Invalid RoomType string", 1);
		this.name = values[2];
		return this;
	}
	
	/* ******************************  GETTERS & SETTERS  *************************************** */
	/**
	 * @return the name
	 */
	public String getName() {
		return name;
	}

	/**
	 * @param name the name to set
	 */
	public void setName(String name) {
		this.name = name;
	}
}
