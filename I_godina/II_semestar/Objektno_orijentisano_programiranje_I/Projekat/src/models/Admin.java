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
public class Admin extends Employee {
	public static final UserRole ROLE = UserRole.ADMIN;
	
	/* ******************************  CONSTRUCTORS  *************************************** */

 	public Admin() {
		super(ROLE);
	}
 	public Admin(String id) {
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
	public Admin(String name, String surname, String gender, LocalDate birthdate, String phone, String address,
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
	public Admin(String id, String name, String surname, String gender, LocalDate birthdate, String phone, String address,
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
	public Admin(String name, String surname, Gender gender, LocalDate birthdate, String phone, String address,
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
	public Admin(String id, String name, String surname, Gender gender, LocalDate birthdate, String phone, String address,
			String username, String password, EducationLevel levelOfProfessionalEducation, int yearsOfWorkExperience,
			double salary) {
		super(ROLE, id, name, surname, gender, birthdate, phone, address, username, password, levelOfProfessionalEducation,
				yearsOfWorkExperience, salary);
		// TODO Auto-generated constructor stub
	}

	/* ******************************  METHODS  *************************************** */
	@Override
	public Object clone() throws CloneNotSupportedException{
        Admin a = new Admin(
        		this.getId(),
        		this.getName(), 
        		this.getSurname(), 
        		this.getGender(),
            	getBirthdate() != null ? LocalDate.from(getBirthdate()) : null,
        		this.getPhone(), 
        		this.getAddress(), 
        		this.getUsername(), 
        		this.getPassword(), 
        		this.getLevelOfProfessionalEducation(), 
        		this.getYearsOfWorkExperience(), 
        		this.getSalary()
        	);
			if (this.isDeleted()) a.delete();
			return a;
    }
}
