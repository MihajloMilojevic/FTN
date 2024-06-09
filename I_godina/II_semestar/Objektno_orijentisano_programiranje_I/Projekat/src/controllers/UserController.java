package controllers;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import app.AppState;
import database.Database;
import database.SelectCondition;
import exceptions.DuplicateIndexException;
import exceptions.NoElementException;
import models.Employee;
import models.Guest;
import models.Model;
import models.User;

public class UserController {

	public static ControllerActionStatus login(String username, String password) {
		if (username.isBlank() || password.isBlank()) {
			return ControllerActionStatus.INCOPLETE_DATA;
		}
		Database db = AppState.getInstance().getDatabase();
        User user = (User) db.getUsers().selectByIndex("username", username);
        if (user == null) {
            return ControllerActionStatus.NO_RECORD;
        }
		if (!user.getPassword().equals(password)) {
			return ControllerActionStatus.WRONG_PASSWORD;
		}
		AppState.getInstance().setUser(user);
		return ControllerActionStatus.SUCCESS;
    }

	public static ControllerActionStatus logout() {
		AppState.getInstance().setUser(null);
		return ControllerActionStatus.SUCCESS;
	}

	public static ControllerActionStatus deleteUser(User user) {
		try {
			AppState.getInstance().getDatabase().getUsers().delete(user);
		} catch (Exception e) {
			return ControllerActionStatus.ERROR;
		}
		return ControllerActionStatus.SUCCESS;
	}

	public static ControllerActionStatus updateUser(User user) {
		try {
			if (user == null) {
				return ControllerActionStatus.INCOPLETE_DATA;
			}
			if (!user.isValid()) {
				return ControllerActionStatus.INCOPLETE_DATA;
			}
			if (user instanceof Employee) {
				Employee employee = (Employee) user;
				employee.setSalary(calculateSalary(employee));
			}
			AppState.getInstance().getDatabase().getUsers().update(user);
			return ControllerActionStatus.SUCCESS;
		} catch (NoElementException e) {
            return ControllerActionStatus.NO_RECORD;
        } catch (Exception e) {
            return ControllerActionStatus.ERROR;
        }
	}

	public static ControllerActionStatus addUser(User user) {
		try {
			if (user == null) {
				return ControllerActionStatus.INCOPLETE_DATA;
			}
			if (!user.isValid()) {
				return ControllerActionStatus.INCOPLETE_DATA;
			}
			if (user instanceof Employee) {
				Employee employee = (Employee) user;
				employee.setSalary(calculateSalary(employee));
			}
			AppState.getInstance().getDatabase().getUsers().insert(user);
			return ControllerActionStatus.SUCCESS;
		} catch (DuplicateIndexException e) {
			return ControllerActionStatus.DUPLICATE_INDEX;
		} catch (Exception e) {
			return ControllerActionStatus.ERROR;
		}
	}
	
	public static ArrayList<Employee> getEmployees() {
		List<Employee> fromDb = AppState.getInstance().getDatabase().getUsers().select(new SelectCondition() {

			@Override
			public boolean check(Model row) {
				return row instanceof Employee && !row.isDeleted();
			}
            
        }).stream().map(row -> (Employee) row).toList();
		ArrayList<Employee> employees = new ArrayList<Employee>();
		employees.addAll(fromDb);
		Collections.sort(employees, (o1, o2) -> o2.getRole().compareTo(o1.getRole()));
		return employees;
	}

	public static ArrayList<Guest> getGuests() {
		List<Guest> dbList = AppState.getInstance().getDatabase().getUsers().select(new SelectCondition() {

			@Override
			public boolean check(Model row) {
				return row instanceof Guest && !row.isDeleted();
			}
            
        }).stream().map(row -> (Guest) row).toList();
		ArrayList<Guest> guests = new ArrayList<Guest>();
		guests.addAll(dbList);
		return guests;
	}

	private static double calculateSalary(Employee employee) {
		double baseSalary = 1500;
		switch (employee.getLevelOfProfessionalEducation()) {
		case PRIMARY_SCHOOL:
			baseSalary += 500;
			break;
		case SECONDARY_SCHOOL:
			baseSalary += 1000;
			break;
		case ASSOCIATE_DEGREE:
			baseSalary += 1500;
			break;
		case BACHELORS_DEGREE:
			baseSalary += 2000;
			break;
		case MASTERS_DEGREE:
			baseSalary += 2500;
			break;
		case DOCTORATE_DEGREE:
			baseSalary += 3500;
			break;
		default:
			break;
		}
		double experienceBonus = (employee.getYearsOfWorkExperience() / 2) * 500;
		return (baseSalary + experienceBonus) * 30;
	}
}
