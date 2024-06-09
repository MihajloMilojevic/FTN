/**
 * 
 */
package models;

import java.time.LocalDate;

import models.enums.Gender;
import models.enums.UserRole;

/**
 * 
 */
public final class Guest extends User {
	public static final UserRole ROLE = UserRole.GUEST;

	/* ******************************  CONSTRUCTORS  *************************************** */

	public Guest() {
		super(ROLE);
	}

	public Guest(String id) {
		super(ROLE, id);
	}
	/**
	 * @param name
	 * @param surname
	 * @param gender
	 * @param birthdate
	 * @param phone
	 * @param address
	 * @param username
	 * @param password
	 */
	public Guest(String name, String surname, String gender, LocalDate birthdate, String phone, String address,
			String username, String password) {
		super(ROLE, name, surname, gender, birthdate, phone, address, username, password);
	}
	/**
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
	public Guest(String id, String name, String surname, String gender, LocalDate birthdate, String phone, String address,
			String username, String password) {
		super(ROLE, id, name, surname, gender, birthdate, phone, address, username, password);
	}

	/**
	 * @param name
	 * @param surname
	 * @param gender
	 * @param birthdate
	 * @param phone
	 * @param address
	 * @param username
	 * @param password
	 */
	public Guest(String name, String surname, Gender gender, LocalDate birthdate, String phone, String address,
			String username, String password) {
		super(ROLE, name, surname, gender, birthdate, phone, address, username, password);
	}

	/**
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
	public Guest(String id, String name, String surname, Gender gender, LocalDate birthdate, String phone, String address,
			String username, String password) {
		super(ROLE, id, name, surname, gender, birthdate, phone, address, username, password);
	}
	
	/* ******************************  METHODS  *************************************** */
	
	@Override
	public Object clone() throws CloneNotSupportedException {
        Guest g = new Guest(
        	getId(),
        	getName(),
        	getSurname(),
        	getGender(),
        	getBirthdate() != null ? LocalDate.from(getBirthdate()) : null,
        	getPhone(),
        	getAddress(),
        	getUsername(),
        	getPassword()
    	);
		if (this.isDeleted()) g.delete();
		return g;
	}
}
