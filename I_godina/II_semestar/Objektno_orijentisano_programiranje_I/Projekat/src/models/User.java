/**
 * 
 */
package models;

import java.text.ParseException;
import java.time.LocalDate;

import models.enums.Gender;
import models.enums.UserRole;
import utils.CSVDateParser;

public abstract class User extends Model {

	/* ******************************  PROPERTIES  *************************************** */

	protected String name;
	protected String surname;
	protected Gender gender;
	protected LocalDate birthdate;
	protected String phone;
	protected String address;
	protected String username;
	protected String password;
	protected UserRole role;
	
	/* ******************************  CONSTRUCTORS  *************************************** */

	public User(UserRole role) {
		super();
		this.role = role;
		this.name = "";
		this.surname = "";
		this.gender = Gender.MALE;
		this.birthdate = LocalDate.now();
		this.phone = "";
		this.address = "";
		this.username = "";
		this.password = "";
	}
	/**
	 * @param role
	 * @param name
	 * @param surname
	 * @param gender
	 * @param birthdate
	 * @param phone
	 * @param address
	 * @param username
	 * @param password
	 */
	public User(UserRole role, String name, String surname, String gender, LocalDate birthdate, String phone, String address,
			String username, String password) {
		super();
		this.role = role;
		this.name = name;
		this.surname = surname;
		this.gender = Gender.valueOf(gender);
		this.birthdate = birthdate;
		this.phone = phone;
		this.address = address;
		this.username = username;
		this.password = password;
	}
	/**
	 * @param role
	 * @param name
	 * @param surname
	 * @param gender
	 * @param birthdate
	 * @param phone
	 * @param address
	 * @param username
	 * @param password
	 */
	public User(UserRole role, String name, String surname, Gender gender, LocalDate birthdate, String phone, String address,
			String username, String password) {
		super();
		this.role = role;
		this.name = name;
		this.surname = surname;
		this.gender = gender;
		this.birthdate = birthdate;
		this.phone = phone;
		this.address = address;
		this.username = username;
		this.password = password;
	}

	public User(UserRole role, String id) {
		super(id);
		this.role = role;
		this.name = "";
		this.surname = "";
		this.gender = Gender.MALE;
		this.birthdate = null;
		this.phone = "";
		this.address = "";
		this.username = "";
		this.password = "";
	}
	/**
	 * @param role
	 * @param id
	 * @param name
	 * @param surname
	 * @param gender
	 * @param birthdate
	 * @param phone
	 * @param address
	 * @param username
	 * @param password
	 */
	public User(UserRole role, String id, String name, String surname, String gender, LocalDate birthdate, String phone, String address,
			String username, String password) {
		super(id);
		this.role = role;
		this.name = name;
		this.surname = surname;
		this.gender = Gender.valueOf(gender);
		this.birthdate = birthdate;
		this.phone = phone;
		this.address = address;
		this.username = username;
		this.password = password;
	}

	/**
	 * @param role
	 * @param id
	 * @param name
	 * @param surname
	 * @param gender
	 * @param birthdate
	 * @param phone
	 * @param address
	 * @param username
	 * @param password
	 */
	public User(UserRole role, String id, String name, String surname, Gender gender, LocalDate birthdate, String phone, String address,
			String username, String password) {
		super(id);
		this.role = role;
		this.name = name;
		this.surname = surname;
		this.gender = gender;
		this.birthdate = birthdate;
		this.phone = phone;
		this.address = address;
		this.username = username;
		this.password = password;
	}
	
	/* ******************************  METHODS  *************************************** */
	
	@Override
	public boolean isValid() {
		if (this.name == null || this.name.isBlank()) return false;
		if (this.surname == null || this.surname.isBlank()) return false;
		if (this.username == null || this.username.isBlank()) return false;
		if (this.password == null || this.password.isBlank()) return false;
		if (this.role == null) return false;
		if (this.phone == null || this.phone.isBlank()) return false;
		if (this.address == null || this.address.isBlank()) return false;
		if (this.birthdate == null || !this.birthdate.isBefore(LocalDate.now())) return false;
		return super.isValid();
	}
	
	@Override
	public Object get(String key) throws IllegalArgumentException {
		// TODO Auto-generated method stub
		switch (key) {
		case "name":
			return (Object) getName();
		case "surname":
			return (Object) getSurname();
		case "gender":
			return (Object) getGender();
		case "birthdate":
			return (Object) getBirthdate();
		case "phone":
			return (Object) getPhone();
		case "address":
			return (Object) getAddress();
		case "username":
			return (Object) getUsername();
		case "password":
			return (Object) getPassword();
		case "role":
			return (Object) getRole();
		default:
			return super.get(key);
		}
	}

	@Override
	public void set(String key, Object value) throws IllegalArgumentException {
		switch (key) {
		case "name":
			setName((String) value);
			break;
		case "surname":
			setSurname((String) value);
			break;
		case "gender":
			setGender((Gender) value);
			break;
		case "birthdate":
			setBirthdate((LocalDate) value);
			break;
		case "phone":
			setPhone((String) value);
			break;
		case "address":
			setAddress((String) value);
			break;
		case "username":
			setUsername((String) value);
			break;
		case "password":
			setPassword((String) value);
			break;
		default:
			super.set(key, value);
		}
	}

	@Override
	public String toString() {
		return String.join(";", new String[] { super.toString(), getRole().toString(), getName(), getSurname(), getGender().toString(),
				CSVDateParser.formatDate(getBirthdate()), getPhone(), getAddress(), getUsername(), getPassword() });
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}
		if (obj == null || obj.getClass() != this.getClass()) {
			return false;
		}
		User user = (User) obj;
		return (
				super.equals(user) &&
				this.getRole().equals(user.getRole()) &&
				this.getName().equals(user.getName()) &&
				this.getSurname().equals(user.getSurname()) &&
				this.getGender().equals(user.getGender()) &&
				this.getBirthdate().equals(user.getBirthdate()) &&
				this.getPhone().equals(user.getPhone()) &&
				this.getAddress().equals(user.getAddress())  &&
				this.getUsername().equals(user.getUsername()) &&
				this.getPassword().equals(user.getPassword())
			);
	}
	
	@Override
	public void update(Model newModel) throws IllegalArgumentException {
        super.update(newModel);
        if (!(newModel instanceof User)) throw new IllegalArgumentException("Not a User");
        User user = (User) newModel;
        this.role = user.role;
        this.name = user.name;
        this.surname = user.surname;
        this.gender = user.gender;
        this.birthdate = user.birthdate;
        this.phone = user.phone;
        this.address = user.address;
        this.username = user.username;
        this.password = user.password;
	}
	
	@Override
	public Model fromCSV(String csv) throws ParseException {
		super.fromCSV(csv);
        String[] values = csv.split(";");
        if (values.length < 11) throw new ParseException("Invalid CSV record", 1);
        try {
        	this.role = UserRole.valueOf(values[2]);
            this.name = values[3];
            this.surname = values[4];
            this.gender = Gender.valueOf(values[5]);
            this.birthdate = CSVDateParser.parseString(values[6]);
            this.phone = values[7];
            this.address = values[8];
            this.username = values[9];
            this.password = values[10];
            return this;
        }
		catch (Exception e) {
			throw new ParseException("Invalid CSV record", 1);
		}
	}

	/* ******************************  GETTERS AND SETTERS  *************************************** */
	
	/**
	 * @return the role
	 */
	public UserRole getRole() {
		return role;
	}

	/**
	 * @param role the role to set
	 */
	public void setRole(UserRole role) {
		this.role = role;
	}
	
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
	 * @return the surname
	 */
	public String getSurname() {
		return surname;
	}

	/**
	 * @param surname the surname to set
	 */
	public void setSurname(String surname) {
		this.surname = surname;
	}

	/**
	 * @return the gender
	 */
	public Gender getGender() {
		return gender;
	}

	/**
	 * @param gender the gender to set
	 */
	public void setGender(Gender gender) {
		this.gender = gender;
	}

	/**
	 * @return the birthdate
	 */
	public LocalDate getBirthdate() {
		return birthdate;
	}

	/**
	 * @param birthdate the birthdate to set
	 */
	public void setBirthdate(LocalDate birthdate) {
		this.birthdate = birthdate;
	}

	/**
	 * @return the phone
	 */
	public String getPhone() {
		return phone;
	}

	/**
	 * @param phone the phone to set
	 */
	public void setPhone(String phone) {
		this.phone = phone;
	}

	/**
	 * @return the address
	 */
	public String getAddress() {
		return address;
	}

	/**
	 * @param address the address to set
	 */
	public void setAddress(String address) {
		this.address = address;
	}

	/**
	 * @return the username
	 */
	public String getUsername() {
		return username;
	}

	/**
	 * @param username the username to set
	 */
	public void setUsername(String username) {
		this.username = username;
	}

	/**
	 * @return the password
	 */
	public String getPassword() {
		return password;
	}

	/**
	 * @param password the password to set
	 */
	public void setPassword(String password) {
		this.password = password;
	}
}
