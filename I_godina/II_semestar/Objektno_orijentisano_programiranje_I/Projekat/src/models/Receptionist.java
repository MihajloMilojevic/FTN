/**
 * 
 */
package models;

import java.time.LocalDate;

import models.enums.EducationLevel;
import models.enums.Gender;
import models.enums.UserRole;

/**
 * 
 */
public class Receptionist extends Employee {
	public static final UserRole ROLE = UserRole.RECEPTIONIST;

	/* ******************************  CONSTRUCTORS  *************************************** */
	
	public Receptionist() {
		super(ROLE);
	}
	public Receptionist(String id) {
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
	 * @param levelOfProfessionalEducation
	 * @param yearsOfWorkExperience
	 * @param salary
	 */
	public Receptionist(String name, String surname, String gender, LocalDate birthdate, String phone,
			String address, String username, String password, EducationLevel levelOfProfessionalEducation,
			int yearsOfWorkExperience, double salary) {
		super(ROLE, name, surname, gender, birthdate, phone, address, username, password, levelOfProfessionalEducation,
				yearsOfWorkExperience, salary);

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
	 * @param levelOfProfessionalEducation
	 * @param yearsOfWorkExperience
	 * @param salary
	 */
	public Receptionist(String id, String name, String surname, String gender, LocalDate birthdate, String phone,
			String address, String username, String password, EducationLevel levelOfProfessionalEducation,
			int yearsOfWorkExperience, double salary) {
		super(ROLE, id, name, surname, gender, birthdate, phone, address, username, password, levelOfProfessionalEducation,
				yearsOfWorkExperience, salary);

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
	 * @param levelOfProfessionalEducation
	 * @param yearsOfWorkExperience
	 * @param salary
	 */
	public Receptionist(String name, String surname, Gender gender, LocalDate birthdate, String phone,
			String address, String username, String password, EducationLevel levelOfProfessionalEducation,
			int yearsOfWorkExperience, double salary) {
		super(ROLE, name, surname, gender, birthdate, phone, address, username, password, levelOfProfessionalEducation,
				yearsOfWorkExperience, salary);

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
	 * @param levelOfProfessionalEducation
	 * @param yearsOfWorkExperience
	 * @param salary
	 */
	public Receptionist(String id, String name, String surname, Gender gender, LocalDate birthdate, String phone,
			String address, String username, String password, EducationLevel levelOfProfessionalEducation,
			int yearsOfWorkExperience, double salary) {
		super(ROLE, id, name, surname, gender, birthdate, phone, address, username, password, levelOfProfessionalEducation,
				yearsOfWorkExperience, salary);

	}
	@Override
	public Object clone() throws CloneNotSupportedException {
		Receptionist r = new Receptionist(getId(), getName(), getSurname(), getGender(), 
	        	getBirthdate() != null ? LocalDate.from(getBirthdate()) : null, getPhone(), getAddress(),
				getUsername(), getPassword(), getLevelOfProfessionalEducation(), getYearsOfWorkExperience(),
				getSalary());
		if (this.isDeleted()) r.delete();
		return r;
	}
}
