package utils;

import java.util.ArrayList;

import controllers.ReservationController;
import controllers.RoomController;
import database.SelectCondition;
import models.Model;
import models.Reservation;
import models.ReservationAddition;
import models.RoomAddition;
import models.RoomType;
import models.enums.ReservationStatus;

public class Filters {

	private static ArrayList<ReservationStatus> statuses;
	private static ArrayList<RoomType> roomTypes;
	private static ArrayList<ReservationAddition> reservationAdditions;
	private static ArrayList<RoomAddition> roomAdditions;
	private static int minPrice;
	private static int maxPrice;
	private static boolean priceEnabled;
	
	public static void reset() {
		statuses = new ArrayList<ReservationStatus>();
		roomTypes = new ArrayList<RoomType>();
		reservationAdditions = new ArrayList<ReservationAddition>();
		roomAdditions = new ArrayList<RoomAddition>();
		minPrice = 0;
		maxPrice = 0;
		priceEnabled = false;
		for (ReservationStatus status : ReservationStatus.values()) {
			statuses.add(status);
		}
		for (RoomType roomType : RoomController.getRoomTypes()) {
			roomTypes.add(roomType);
		}
		for (ReservationAddition addition : ReservationController.getReservationAdditions()) {
			reservationAdditions.add(addition);
		}
	}
	
	static {
		reset();
	}
	
	public static SelectCondition getCondition() {
		return new SelectCondition() {
			@Override
			public boolean check(Model row) {
				if (! (row instanceof Reservation)) return false;
				if (row.isDeleted()) return false;
				
				Reservation reservation = (Reservation) row;
				if (statuses.size() > 0 && !statuses.contains(reservation.getStatus())) {
					return false;
				}
				if (roomTypes.size() > 0 && !roomTypes.contains(reservation.getRoomType())) {
					return false;
				}
				if (reservationAdditions.size() > 0
						&& !reservationAdditions.containsAll(reservation.getReservationAdditions())) {
					return false;
				}
				if (roomAdditions.size() > 0 && !roomAdditions.containsAll(reservation.getRoomAdditions())) {
					return false;
				}
				if (priceEnabled && (reservation.getPrice() < minPrice || reservation.getPrice() > maxPrice)) {
					return false;
				}
				return true;
			}
		};
	}

	/**
	 * @return the statuses
	 */
	public static ArrayList<ReservationStatus> getStatuses() {
		return statuses;
	}

	/**
	 * @param statuses the statuses to set
	 */
	public static void setStatuses(ArrayList<ReservationStatus> statuses) {
		Filters.statuses = statuses;
	}

	/**
	 * @return the roomTypes
	 */
	public static ArrayList<RoomType> getRoomTypes() {
		return roomTypes;
	}

	/**
	 * @param roomTypes the roomTypes to set
	 */
	public static void setRoomTypes(ArrayList<RoomType> roomTypes) {
		Filters.roomTypes = roomTypes;
	}

	/**
	 * @return the reservationAdditions
	 */
	public static ArrayList<ReservationAddition> getReservationAdditions() {
		return reservationAdditions;
	}

	/**
	 * @param reservationAdditions the reservationAdditions to set
	 */
	public static void setReservationAdditions(ArrayList<ReservationAddition> reservationAdditions) {
		Filters.reservationAdditions = reservationAdditions;
	}

	/**
	 * @return the roomAdditions
	 */
	public static ArrayList<RoomAddition> getRoomAdditions() {
		return roomAdditions;
	}

	/**
	 * @param roomAdditions the roomAdditions to set
	 */
	public static void setRoomAdditions(ArrayList<RoomAddition> roomAdditions) {
		Filters.roomAdditions = roomAdditions;
	}

	/**
	 * @return the minPrice
	 */
	public static int getMinPrice() {
		return minPrice;
	}

	/**
	 * @param minPrice the minPrice to set
	 */
	public static void setMinPrice(int minPrice) {
		Filters.minPrice = minPrice;
	}

	/**
	 * @return the maxPrice
	 */
	public static int getMaxPrice() {
		return maxPrice;
	}

	/**
	 * @param maxPrice the maxPrice to set
	 */
	public static void setMaxPrice(int maxPrice) {
		Filters.maxPrice = maxPrice;
	}

	/**
	 * @return the priceEnabled
	 */
	public static boolean isPriceEnabled() {
		return priceEnabled;
	}

	/**
	 * @param priceEnabled the priceEnabled to set
	 */
	public static void setPriceEnabled(boolean priceEnabled) {
		Filters.priceEnabled = priceEnabled;
	}

}
