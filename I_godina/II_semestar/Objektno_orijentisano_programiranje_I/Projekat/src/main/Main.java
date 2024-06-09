package main;

import javax.swing.JOptionPane;

import app.AppState;
import controllers.ReservationController;
import database.InitialDatabase;
import views.entry.Login;

public class Main {

	public static void main(String[] args) {
		try {
			// should initialize the database with initial data
			boolean init = false;
			//init = true;
			if(init) {
				InitialDatabase.init();
				return;
			}
			
			// load data from files
			AppState.getInstance().load();

			// automatically reject expired reservations
			ReservationController.rejectExpiredReservations();
			
			// start the GUI
			Login frame = new Login();
			frame.setVisible(true);
			System.out.println("GUI started");
		} catch (Exception e) {
			JOptionPane.showMessageDialog(null, "Error: " + e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
			e.printStackTrace();
		}
	}
}
