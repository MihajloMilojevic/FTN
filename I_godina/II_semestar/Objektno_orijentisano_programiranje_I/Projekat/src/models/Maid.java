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
public class Maid extends Employee {
	public static final UserRole ROLE = UserRole.MAID;

	/* ******************************  CONSTRUCTORS  *************************************** */
	
	public Maid() {
		super(ROLE);
	}
	public Maid(String id) {
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
	public Maid(String name, String surname, String gender, LocalDate birthdate, String phone, String address,
			String username, String password, EducationLevel levelOfProfessionalEducation, int yearsOfWorkExperience,
			double salary) {
		super(ROLE, name, surname, gender, birthdate, phone, address, username, password, levelOfProfessionalEducation,
				yearsOfWorkExperience, salary);
		// TODO Auto-generated constructor stub
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
	public Maid(String id, String name, String surname, String gender, LocalDate birthdate, String phone, String address,
			String username, String password, EducationLevel levelOfProfessionalEducation, int yearsOfWorkExperience,
			double salary) {
		super(ROLE, id, name, surname, gender, birthdate, phone, address, username, password, levelOfProfessionalEducation,
				yearsOfWorkExperience, salary);
		// TODO Auto-generated constructor stub
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
	public Maid(String name, String surname, Gender gender, LocalDate birthdate, String phone, String address,
			String username, String password, EducationLevel levelOfProfessionalEducation, int yearsOfWorkExperience,
			double salary) {
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
	public Maid(String id, String name, String surname, Gender gender, LocalDate birthdate, String phone, String address,
			String username, String password, EducationLevel levelOfProfessionalEducation, int yearsOfWorkExperience,
			double salary) {
		super(ROLE, id, name, surname, gender, birthdate, phone, address, username, password, levelOfProfessionalEducation,
				yearsOfWorkExperience, salary);
	}
	/* ******************************  METHODS  *************************************** */
	@Override
	public Object clone() throws CloneNotSupportedException {
		Maid m = new Maid(
				getId(),
				getName(), 
				getSurname(), 
				getGender(), 
	        	getBirthdate() != null ? LocalDate.from(getBirthdate()) : null,
				getPhone(), 
				getAddress(), 
				getUsername(),
				getPassword(), 
				getLevelOfProfessionalEducation(), 
				getYearsOfWorkExperience(), 
				getSalary()
			);
		if (this.isDeleted()) m.delete();
	    return m;
	}
}
