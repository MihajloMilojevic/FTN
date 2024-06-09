package models;

import java.text.ParseException;

public class RoomAddition extends Model {

	/* ******************************  ATTRIBUTES  *************************************** */
	// Attributes in the database
	private String name;
	
	public RoomAddition() {
		super();
		this.name = "";
	}

	public RoomAddition(String name) {
		super();
        this.name = name;
	}
	
	public RoomAddition(String id, String name) {
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
		if (!(newModel instanceof RoomAddition)) throw new IllegalArgumentException("Not  a RoomAddition object");
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
		RoomAddition RoomAddition = (RoomAddition) obj;
		return super.equals(obj) && this.name.equals(RoomAddition.name);
	}
	@Override
	public Object clone() throws CloneNotSupportedException {
		RoomAddition ra = new RoomAddition(this.getId(), this.name);
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
