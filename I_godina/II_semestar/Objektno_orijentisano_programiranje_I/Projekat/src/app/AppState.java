package app;

import java.io.IOException;
import java.text.ParseException;

import database.Database;
import exceptions.NoElementException;
import models.User;

public class AppState {


	private static AppState instance;

	private User user;

	public void load() throws IOException, ParseException, NoElementException {
		getSettings().load();
		getDatabase().load();
		System.out.println("App state loaded.");
	}

	public void save() throws IOException, ParseException {
		getSettings().save();
		getDatabase().save();
		System.out.println("App state saved.");
	}

	public static AppState getInstance() {
		if (instance == null) {
			instance = new AppState();
		}
		return instance;
	}
	
	/* ******************* GETTERS AND SETTERS ******************* */

	/**
	 * @return the user
	 */
	public User getUser() {
		return user;
	}

	/**
	 * @param user the user to set
	 */
	public void setUser(User user) {
		this.user = user;
	}
	
	
	/**
	 * @return the settings
	 */
	public AppSettings getSettings() {
		return AppSettings.getInstance();
	}

	/**
	 * @return the database
	 */
	public Database getDatabase() {
		return Database.getInstance(getSettings());
	}
}
