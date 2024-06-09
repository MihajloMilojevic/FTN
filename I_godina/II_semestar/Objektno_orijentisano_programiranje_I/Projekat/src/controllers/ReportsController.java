package controllers;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.HashMap;

import app.AppState;
import database.SelectCondition;
import models.CleaningLog;
import models.Employee;
import models.Maid;
import models.Model;
import models.Reservation;
import models.Room;
import models.RoomType;
import models.User;
import models.enums.ReservationStatus;
import utils.Pair;

public class ReportsController {
	public static ArrayList<String> getDailyCheckins() {
		return new ArrayList<String>(
				AppState.getInstance().getDatabase().getReservations().select(new SelectCondition() {
					@Override
					public boolean check(Model model) {
						Reservation reservation = (Reservation) model;
						return !reservation.isDeleted() && reservation.getCheckInDate() != null
								&& reservation.getCheckInDate().equals(LocalDate.now());
					}
				}).stream().map(r -> r.getGuest().getName() + " " + r.getGuest().getSurname()).toList());
	}

	public static ArrayList<String> getDailyCheckouts() {
		return new ArrayList<String>(
				AppState.getInstance().getDatabase().getReservations().select(new SelectCondition() {
					@Override
					public boolean check(Model model) {
						Reservation reservation = (Reservation) model;
						return !reservation.isDeleted() && reservation.getCheckOutDate() != null
								&& reservation.getCheckOutDate().equals(LocalDate.now());
					}
				}).stream().map(r -> r.getGuest().getName() + " " + r.getGuest().getSurname()).toList());
	}

	public static ArrayList<String> getDailyNotYet() {
		return new ArrayList<String>(
				AppState.getInstance().getDatabase().getReservations().select(new SelectCondition() {
					@Override
					public boolean check(Model model) {
						Reservation reservation = (Reservation) model;
						return !reservation.isDeleted() && reservation.getCheckInDate() == null
								&& reservation.getStartDate().equals(LocalDate.now());
					}
				}).stream().map(r -> r.getGuest().getName() + " " + r.getGuest().getSurname()).toList());
	}

	private static String[] monthsNames = new String[] { "January", "February", "March", "April", "May", "June", "July",
			"August", "September", "October", "November", "December" };

	public static ArrayList<Revenue> getRevenue() {
		int monthToday = LocalDate.now().getMonthValue();
		String months[] = new String[12];
		for (int i = 0; i < 12; i++) {
			months[11 - i] = monthsNames[LocalDate.now().minusMonths(i).getMonthValue() - 1];
		}
		ArrayList<Revenue> revenue = new ArrayList<Revenue>();
		for (RoomType type : AppState.getInstance().getDatabase().getRoomTypes().getRows()) {
			Revenue r = new Revenue(type, months);
			revenue.add(r);
		}
		ArrayList<Reservation> reservations = AppState.getInstance().getDatabase().getReservations()
				.select(new SelectCondition() {
					@Override
					public boolean check(Model model) {
						Reservation reservation = (Reservation) model;
						return !reservation.isDeleted() && reservation.getRoom() != null
								&& reservation.getStartDate().isAfter(LocalDate.now().minusMonths(12));
					}
				});

		for (Reservation reservation : reservations) {

			int month = reservation.getStartDate().getMonthValue();
			// get the index of the month where 0 is the month 12 months ago and 11 is the
			// current month
			int index = (monthToday - month + 12) % 12;
			double price = reservation.getPrice();
			Revenue r = null;
			for (Revenue rev : revenue) {
				if (rev.getType().getId() == reservation.getRoom().getType().getId()) {
					r = rev;
					break;
				}
			}
			if (r == null) {
				continue;
			}
			r.getMonthlyRevenue()[11 - index] += price;
		}

		return revenue;
	}

	public static HashMap<Maid, Integer> getMaidWorkload(LocalDate startDate, LocalDate endDate) {
		HashMap<Maid, Integer> workload = new HashMap<Maid, Integer>();
		for (User user : AppState.getInstance().getDatabase().getUsers().getRows()) {
			if (user instanceof Maid) {
				workload.put((Maid) user, 0);
			}
		}
		for (Room room : AppState.getInstance().getDatabase().getRooms().getRows()) {
			for (CleaningLog log : room.getCleaningLogs()) {
				if ((log.getDate().isAfter(startDate) && log.getDate().isBefore(endDate))
						|| log.getDate().equals(startDate) || log.getDate().equals(endDate)) {
					int current = workload.get(log.getMaid());
					workload.put(log.getMaid(), current + 1);
				}
			}
		}
		return workload;
	}

	public static HashMap<ReservationStatus, Integer> getReservationStatuses() {
		HashMap<ReservationStatus, Integer> statuses = new HashMap<ReservationStatus, Integer>();
		for (ReservationStatus status : ReservationStatus.values()) {
			statuses.put(status, 0);
		}
		ArrayList<Reservation> reservations = AppState.getInstance().getDatabase().getReservations()
				.select(new SelectCondition() {
					@Override
					public boolean check(Model model) {
						Reservation reservation = (Reservation) model;
						return !reservation.isDeleted()
								&& reservation.getCreatedAtDate().isAfter(LocalDate.now().minusDays(30));
					}
				});
		for (Reservation reservation : reservations) {
			int current = statuses.get(reservation.getStatus());
			statuses.put(reservation.getStatus(), current + 1);
		}
		return statuses;
	}
	
	public static HashMap<ReservationStatus,Integer> getReservationStatusesForPeriod(LocalDate startDate, LocalDate endDate) {
		HashMap<ReservationStatus, Integer> statuses = new HashMap<ReservationStatus, Integer>();
		for (ReservationStatus status : ReservationStatus.values()) {
			statuses.put(status, 0);
		}
		ArrayList<Reservation> reservations = AppState.getInstance().getDatabase().getReservations()
				.select(new SelectCondition() {
					@Override
					public boolean check(Model model) {
						Reservation reservation = (Reservation) model;
						return !reservation.isDeleted() && reservation.getStartDate().isBefore(endDate)
								&& reservation.getEndDate().isAfter(startDate);
					}
				});
		for (Reservation reservation : reservations) {
			int current = statuses.get(reservation.getStatus());
			statuses.put(reservation.getStatus(), current + 1);
		}
		return statuses;
	}

	public static Pair<Double, Double> getRevenueForPeriod(LocalDate startDate, LocalDate endDate) {
		Pair<Double, Double> revenue = new Pair<Double, Double>(0.0, 0.0);
		ArrayList<Reservation> reservations = AppState.getInstance().getDatabase().getReservations()
				.select(new SelectCondition() {
					@Override
					public boolean check(Model model) {
						Reservation reservation = (Reservation) model;
						return !reservation.isDeleted() && reservation.getStartDate().isBefore(endDate)
								&& reservation.getEndDate().isAfter(startDate);
					}
				});
		for (Reservation reservation : reservations) {
			revenue.setFirst(revenue.getFirst() + reservation.getPrice());
		}
		
		long days = startDate.until(endDate).getDays();
		for (User user : AppState.getInstance().getDatabase().getUsers().getRows()) {
			if (!(user instanceof Employee)) continue;
			Employee employee = (Employee) user;
			revenue.setSecond(revenue.getSecond() + employee.getSalary() * days / 30.0);
		}
		return revenue;
	}
	
	public static ArrayList<RoomsReport> getRoomsReportForPeriod(LocalDate startDate, LocalDate endDate) {
		ArrayList<RoomsReport> reports = new ArrayList<RoomsReport>();
		HashMap<Room, RoomsReport> reportsMap = new HashMap<Room, RoomsReport>();
		for (Room room : AppState.getInstance().getDatabase().getRooms().getRows()) {
			RoomsReport report = new RoomsReport(room);
			reportsMap.put(room, report);
		}
		for (Reservation reservation : AppState.getInstance().getDatabase().getReservations().getRows()) {
			if (reservation.isDeleted()) {
				continue;
			}
			if (reservation.getStartDate().isAfter(endDate)) {
				continue;
			}
			if (reservation.getEndDate().isBefore(startDate)) {
				continue;
			}
			if (reservation.getRoom() == null) {
				continue;
			}
			RoomsReport report = reportsMap.get(reservation.getRoom());
			if (report == null) {
				continue;
			}
			report.includeReservation(reservation, startDate, endDate);
		}
		reports.addAll(reportsMap.values());
		reports.sort((r1, r2) -> {
			return r1.getRoom().getNumber() - r2.getRoom().getNumber();
		});
		return reports;
	}

	public static class Revenue {
		private RoomType type;
		private double[] monthlyRevenue;
		private String[] months;

		public Revenue(RoomType type, String[] months) {
			this.type = type;
			this.monthlyRevenue = new double[12];
			for (int i = 0; i < 12; i++) {
				this.monthlyRevenue[i] = 0;
			}
			this.months = months;
		}

		/**
		 * @return the type
		 */
		public RoomType getType() {
			return type;
		}

		/**
		 * @return the monthlyRevenue
		 */
		public double[] getMonthlyRevenue() {
			return monthlyRevenue;
		}

		/**
		 * @return the months
		 */
		public String[] getMonths() {
			return months;
		}

	}
	
	public static class RoomsReport {
		private Room room;
		private int nights;
		private double revenue;
		
		public RoomsReport(Room room) {
			this.room = room;
			this.nights = 0;
			this.revenue = 0;
		}
		
		public void includeReservation(Reservation reservation, LocalDate startDate, LocalDate endDate) {
			LocalDate start = reservation.getStartDate();
			LocalDate end = reservation.getEndDate();
			if (start.isBefore(startDate)) {
				start = startDate;
			}
			if (end.isAfter(endDate)) {
				end = endDate;
			}
			int nights = (int) start.until(end).getDays();
			this.nights += nights;
			this.revenue += reservation.getPrice();
		}

		/**
		 * @return the room
		 */
		public Room getRoom() {
			return room;
		}

		/**
		 * @return the nights
		 */
		public int getNights() {
			return nights;
		}

		/**
		 * @return the revenue
		 */
		public double getRevenue() {
			return revenue;
		}
		
	}
}
