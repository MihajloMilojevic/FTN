package models;

import java.text.ParseException;

public class RoomType extends Model {

	/* ******************************  ATTRIBUTES  *************************************** */
	// Attributes in the database
	private String name;
	private int maxCapacity;
	
	public RoomType() {
		super();
		this.name = "";
		this.maxCapacity = 0;
	}

	public RoomType(String name, int maxCapacity) {
		super();
        this.name = name;
        this.maxCapacity = maxCapacity;
	}
	
	public RoomType(String id, String name, int maxCapacity) {
		super(id);
		this.name = name;
		this.maxCapacity = maxCapacity;
	}
	
	/* ******************************  METHODS  *************************************** */
	
	@Override
	public boolean isValid() {
		if (this.name == null || this.name.isBlank() || this.maxCapacity <= 0) return false;
		return super.isValid();
	}
	
	@Override
	public Object get(String key) throws IllegalArgumentException {
		switch (key) {
		case "name":
			return (Object) this.name;
		case "maxCapacity":
			return (Object) this.maxCapacity;
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
		case "maxCapacity":
			this.maxCapacity = (int) value;
			break;
		default:
			super.set(key, value);
		}
	}
	@Override
	public void update(Model newModel) throws IllegalArgumentException {
		super.update(newModel);
		if (!(newModel instanceof RoomType)) throw new IllegalArgumentException("Not  a RoomType object");
		this.name = (String) newModel.get("name");
		this.maxCapacity = (int) newModel.get("maxCapacity");
	}
	@Override
	public String toString() {
		return String.join(";", new String[] {super.toString(), this.name, String.valueOf(this.maxCapacity)});
	}
	@Override
	public boolean equals(Object obj) {
		if (obj == this) {
			return true;
		}
		if (obj == null || obj.getClass() != this.getClass()) {
			return false;
		}
		RoomType roomType = (RoomType) obj;
		return super.equals(obj) && this.name.equals(roomType.name) && this.maxCapacity == roomType.maxCapacity;
	}
	@Override
	public Object clone() throws CloneNotSupportedException {
		RoomType rt = new RoomType(this.getId(), this.name, this.maxCapacity);
		if (this.isDeleted()) rt.delete();
		return rt;
	}
	@Override
	public Model fromCSV(String csv) throws ParseException {
		super.fromCSV(csv);
		String[] values = csv.split(";");
		if (values.length < 4) throw new ParseException("Invalid RoomType string", 1);
		this.name = values[2];
		this.maxCapacity = Integer.parseInt(values[3]);
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

	/**
	 * @return the maxCapacity
	 */
	public int getMaxCapacity() {
		return maxCapacity;
	}

	/**
	 * @param maxCapacity the maxCapacity to set
	 */
	public void setMaxCapacity(int maxCapacity) {
		this.maxCapacity = maxCapacity;
	}
}
