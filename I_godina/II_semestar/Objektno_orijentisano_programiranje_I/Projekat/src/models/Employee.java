/**
 * 
 */
package models;

import java.text.ParseException;
import java.time.LocalDate;

import models.enums.EducationLevel;
import models.enums.Gender;
import models.enums.UserRole;

/**
 * 
 */
public abstract class Employee extends User {

	/*
	 * ****************************** PROPERTIES
	 * ***************************************
	 */

	protected EducationLevel levelOfProfessionalEducation;
	protected int yearsOfWorkExperience;
	protected double salary;

	/*
	 * ****************************** CONSTRUCTORS
	 * ***************************************
	 */

	public Employee(UserRole role) {
		super(role);
		this.levelOfProfessionalEducation = EducationLevel.NO_EDUCATION;
		this.yearsOfWorkExperience = 0;
		this.salary = 0;
	}

	public Employee(UserRole role, String id) {
		super(role, id);
		this.levelOfProfessionalEducation = EducationLevel.NO_EDUCATION;
		this.yearsOfWorkExperience = 0;
		this.salary = 0;
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
	public Employee(UserRole role, String name, String surname, String gender, LocalDate birthdate, String phone,
			String address, String username, String password, EducationLevel levelOfProfessionalEducation,
			int yearsOfWorkExperience, double salary) {
		super(role, name, surname, gender, birthdate, phone, address, username, password);
		this.levelOfProfessionalEducation = levelOfProfessionalEducation;
		this.yearsOfWorkExperience = yearsOfWorkExperience;
		this.salary = salary;
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
	public Employee(UserRole role, String id, String name, String surname, String gender, LocalDate birthdate,
			String phone, String address, String username, String password, EducationLevel levelOfProfessionalEducation,
			int yearsOfWorkExperience, double salary) {
		super(role, id, name, surname, gender, birthdate, phone, address, username, password);
		this.levelOfProfessionalEducation = levelOfProfessionalEducation;
		this.yearsOfWorkExperience = yearsOfWorkExperience;
		this.salary = salary;
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
	public Employee(UserRole role, String name, String surname, Gender gender, LocalDate birthdate, String phone,
			String address, String username, String password, EducationLevel levelOfProfessionalEducation,
			int yearsOfWorkExperience, double salary) {
		super(role, name, surname, gender, birthdate, phone, address, username, password);
		this.levelOfProfessionalEducation = levelOfProfessionalEducation;
		this.yearsOfWorkExperience = yearsOfWorkExperience;
		this.salary = salary;
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
	public Employee(UserRole role, String id, String name, String surname, Gender gender, LocalDate birthdate,
			String phone, String address, String username, String password, EducationLevel levelOfProfessionalEducation,
			int yearsOfWorkExperience, double salary) {
		super(role, id, name, surname, gender, birthdate, phone, address, username, password);
		this.levelOfProfessionalEducation = levelOfProfessionalEducation;
		this.yearsOfWorkExperience = yearsOfWorkExperience;
		this.salary = salary;
	}

	/*
	 * ****************************** METHODS
	 * ***************************************
	 */

	@Override
	public boolean isValid() {
		if (levelOfProfessionalEducation == null)
			return false;
		if (yearsOfWorkExperience < 0)
			return false;
		if (salary < 0)
			return false;
		return super.isValid();
	}

	@Override
	public Object get(String key) throws IllegalArgumentException {
		switch (key) {
		case "levelOfProfessionalEducation":
			return getLevelOfProfessionalEducation();
		case "yearsOfWorkExperience":
			return getYearsOfWorkExperience();
		case "salary":
			return getSalary();
		default:
			return super.get(key);
		}
	}

	@Override
	public void set(String key, Object value) throws IllegalArgumentException {
		switch (key) {
		case "levelOfProfessionalEducation":
			setLevelOfProfessionalEducation((EducationLevel) value);
			break;
		case "yearsOfWorkExperience":
			setYearsOfWorkExperience((int) value);
			break;
		case "salary":
			setSalary((double) value);
			break;
		default:
			super.set(key, value);
			break;
		}
	}

	@Override
	public String toString() {
		return String.join(";", new String[] { super.toString(), getLevelOfProfessionalEducation().toString(),
				Integer.toString(getYearsOfWorkExperience()), Double.toString(getSalary()) });
	}

	@Override
	public boolean equals(Object obj) {
		if (obj == this) {
			return true;
		}
		if (obj == null || obj.getClass() != this.getClass()) {
			return false;
		}
		Employee employee = (Employee) obj;
		return super.equals(employee)
				&& getLevelOfProfessionalEducation().equals(employee.getLevelOfProfessionalEducation())
				&& getYearsOfWorkExperience() == employee.getYearsOfWorkExperience()
				&& getSalary() == employee.getSalary();
	}

	@Override
	public void update(Model newModel) throws IllegalArgumentException {
		super.update(newModel);
		if (!(newModel instanceof Employee))
			throw new IllegalArgumentException("Not an Employee");
		Employee employee = (Employee) newModel;
		setLevelOfProfessionalEducation(employee.getLevelOfProfessionalEducation());
		setYearsOfWorkExperience(employee.getYearsOfWorkExperience());
		setSalary(employee.getSalary());
	}

	@Override
	public Model fromCSV(String csv) throws ParseException {
		super.fromCSV(csv);
		String[] values = csv.split(";");
		if (values.length < 14)
			throw new ParseException("Invalid csv record", 2);
		try {
			setLevelOfProfessionalEducation(EducationLevel.valueOf(values[11]));
			setYearsOfWorkExperience(Integer.parseInt(values[12]));
			setSalary(Double.parseDouble(values[13]));
			return this;
		} catch (Exception e) {
			e.printStackTrace();
			throw new ParseException("Invalid csv record", 2);
		}
	}

	/*
	 * ****************************** GETTERS & SETTERS
	 * ***************************************
	 */

	/**
	 * @return the levelOfProfessionalEducation
	 */
	public EducationLevel getLevelOfProfessionalEducation() {
		return levelOfProfessionalEducation;
	}

	/**
	 * @param levelOfProfessionalEducation the levelOfProfessionalEducation to set
	 */
	public void setLevelOfProfessionalEducation(EducationLevel levelOfProfessionalEducation) {
		this.levelOfProfessionalEducation = levelOfProfessionalEducation;
	}

	/**
	 * @return the yearsOfWorkExperience
	 */
	public int getYearsOfWorkExperience() {
		return yearsOfWorkExperience;
	}

	/**
	 * @param yearsOfWorkExperience the yearsOfWorkExperience to set
	 */
	public void setYearsOfWorkExperience(int yearsOfWorkExperience) {
		this.yearsOfWorkExperience = yearsOfWorkExperience;
	}

	/**
	 * @return the salary
	 */
	public double getSalary() {
		return salary;
	}

	/**
	 * @param salary the salary to set
	 */
	public void setSalary(double salary) {
		this.salary = salary;
	}

}
