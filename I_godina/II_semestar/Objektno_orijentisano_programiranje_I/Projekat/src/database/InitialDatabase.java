package database;

import java.time.LocalDate;

import app.AppState;
import controllers.ReservationController;
import models.Admin;
import models.CleaningLog;
import models.Guest;
import models.Maid;
import models.PriceList;
import models.Receptionist;
import models.Reservation;
import models.ReservationAddition;
import models.Room;
import models.RoomAddition;
import models.RoomType;
import models.enums.EducationLevel;
import models.enums.Gender;

public class InitialDatabase {

	public static void init() {

		try {
			AppState.getInstance().getSettings().load();
			Database db = AppState.getInstance().getDatabase();
			/*
			 * ****************************** Users ***************************************
			 */

			Admin mihajlo = new Admin("Mihajlo", "Milojević", Gender.MALE, LocalDate.of(2004, 5, 21), "+381649781191",
					"Braće Dronjak 6, Novi Sad", "admin", "admin", EducationLevel.DOCTORATE_DEGREE, 2, 210_000);
			db.getUsers().insert(mihajlo);

			Receptionist petar = new Receptionist("Petar", "Popović", Gender.MALE, LocalDate.of(2004, 6, 6),
					"+381628361185", "Bulevar despota Stefana 7, Novi Sad", "petar", "Petar123", EducationLevel.BACHELORS_DEGREE, 1,
					105_000);
			Receptionist sara1 = new Receptionist("Sara", "Stojkov", Gender.FEMALE, LocalDate.of(2004, 9, 17),
					"+381612599941", "Maksima Gorkog 12, Novi Sad", "sara", "Sara987", EducationLevel.MASTERS_DEGREE, 3, 135_000);
			db.getUsers().insert(petar);
			db.getUsers().insert(sara1);

			Maid luka = new Maid("Luka", "Prlinčević", Gender.MALE, LocalDate.of(2004, 8, 26), "+381640862775",
					"Bulevar despota Stefana 7, Novi Sad", "luka", "Luka123", EducationLevel.PRIMARY_SCHOOL, 0, 60_000);
			Maid nikola = new Maid("Nikola", "Rogonjić", Gender.MALE, LocalDate.of(2004, 9, 10), "+381644606859",
					"Samaila 5, Kraljevo", "nikola", "Nikola123", EducationLevel.SECONDARY_SCHOOL, 0, 75_000);
			db.getUsers().insert(luka);
			db.getUsers().insert(nikola);

			Guest djordje = new Guest("Đorđe", "Milojević", Gender.MALE, LocalDate.of(2008, 5, 4), "+381642723956",
					"8. Mart 70, Kraljevo", "Djole", "Majmunce");
			Guest sofija = new Guest("Sofija", "Obradović", Gender.FEMALE, LocalDate.of(2004, 4, 21), "+381659786412",
					"Bulevar vojvode Stepe 17, Novi Sad", "Sofija", "Sofija123");
			Guest sara2 = new Guest("Sara", "Spasojević", Gender.FEMALE, LocalDate.of(2004, 4, 20), "+381628361185",
					"Ulica 9. maja 15, Kraljevo", "caja", "Sara123");
			db.getUsers().insert(djordje);
			db.getUsers().insert(sofija);
			db.getUsers().insert(sara2);

			/*
			 * ****************************** Room Types
			 * ***************************************
			 */

			RoomType single = new RoomType("Single", 1);
			RoomType doubleSingleBed = new RoomType("Double Single Bed", 2);
			RoomType doubleTwoBeds = new RoomType("Double Two Beds", 2);
			RoomType tripleThreeBeds = new RoomType("Triple Three Beds", 3);
			RoomType tripleTwoBeds = new RoomType("Triple Two Beds", 3);
			RoomType apartment = new RoomType("Apartment", 6);
			RoomType penthouse = new RoomType("Penthouse", 10);
			db.getRoomTypes().insert(single);
			db.getRoomTypes().insert(doubleSingleBed);
			db.getRoomTypes().insert(doubleTwoBeds);
			db.getRoomTypes().insert(tripleThreeBeds);
			db.getRoomTypes().insert(tripleTwoBeds);
			db.getRoomTypes().insert(apartment);
			db.getRoomTypes().insert(penthouse);

			/*
			 * ****************************** Room Additions
			 * ***************************************
			 */

			RoomAddition balcony = new RoomAddition("Balcony");
			RoomAddition cityView = new RoomAddition("City View");
			RoomAddition jacuzzi = new RoomAddition("Jacuzzi");
			RoomAddition tv = new RoomAddition("TV");
			RoomAddition wifi = new RoomAddition("WiFi");
			RoomAddition climate = new RoomAddition("AC Unit");
			db.getRoomAdditions().insert(balcony);
			db.getRoomAdditions().insert(cityView);
			db.getRoomAdditions().insert(jacuzzi);
			db.getRoomAdditions().insert(tv);
			db.getRoomAdditions().insert(wifi);
			db.getRoomAdditions().insert(climate);

			/*
			 * ****************************** Reservation Additions
			 * ***************************************
			 */

			ReservationAddition breakfast = new ReservationAddition("Breakfast");
			ReservationAddition lunch = new ReservationAddition("Lunch");
			ReservationAddition dinner = new ReservationAddition("Dinner");
			ReservationAddition allInclusive = new ReservationAddition("All Inclusive");
			ReservationAddition spa = new ReservationAddition("Spa");
			ReservationAddition gym = new ReservationAddition("Gym");
			ReservationAddition pool = new ReservationAddition("Pool");
			ReservationAddition parking = new ReservationAddition("Parking");
			ReservationAddition roomService = new ReservationAddition("Room Service");
			ReservationAddition extraBed = new ReservationAddition("Extra Bed");
			db.getReservationAdditions().insert(breakfast);
			db.getReservationAdditions().insert(lunch);
			db.getReservationAdditions().insert(dinner);
			db.getReservationAdditions().insert(allInclusive);
			db.getReservationAdditions().insert(spa);
			db.getReservationAdditions().insert(gym);
			db.getReservationAdditions().insert(pool);
			db.getReservationAdditions().insert(parking);
			db.getReservationAdditions().insert(roomService);
			db.getReservationAdditions().insert(extraBed);

			/*
			 * ****************************** Rooms ***************************************
			 */

			Room room101 = new Room(101, single);
			Room room102 = new Room(102, single);
			Room room103 = new Room(103, single);
			Room room104 = new Room(104, single);
			Room room105 = new Room(105, doubleSingleBed);
			Room room106 = new Room(106, doubleSingleBed);
			Room room107 = new Room(107, doubleSingleBed);
			Room room108 = new Room(108, doubleSingleBed);
			Room room109 = new Room(109, doubleTwoBeds);
			Room room110 = new Room(110, doubleTwoBeds);
			Room room111 = new Room(111, doubleTwoBeds);
			Room room112 = new Room(112, doubleTwoBeds);
			Room room113 = new Room(113, tripleThreeBeds);
			Room room114 = new Room(114, tripleThreeBeds);
			Room room115 = new Room(115, tripleThreeBeds);
			Room room116 = new Room(116, tripleThreeBeds);
			Room room117 = new Room(117, tripleTwoBeds);
			Room room118 = new Room(118, tripleTwoBeds);
			Room room119 = new Room(119, tripleTwoBeds);
			Room room120 = new Room(120, tripleTwoBeds);
			Room room121 = new Room(121, apartment);
			Room room122 = new Room(122, apartment);
			Room room123 = new Room(123, apartment);
			Room room124 = new Room(124, apartment);
			
			Room room201 = new Room(201, single);
			Room room202 = new Room(202, single);
			Room room203 = new Room(203, single);
			Room room204 = new Room(204, single);
			Room room205 = new Room(205, doubleSingleBed);
			Room room206 = new Room(206, doubleSingleBed);
			Room room207 = new Room(207, doubleSingleBed);
			Room room208 = new Room(208, doubleSingleBed);
			Room room209 = new Room(209, doubleTwoBeds);
			Room room210 = new Room(210, doubleTwoBeds);
			Room room211 = new Room(211, doubleTwoBeds);
			Room room212 = new Room(212, doubleTwoBeds);
			Room room213 = new Room(213, tripleThreeBeds);
			Room room214 = new Room(214, tripleThreeBeds);
			Room room215 = new Room(215, tripleThreeBeds);
			Room room216 = new Room(216, tripleThreeBeds);
			Room room217 = new Room(217, tripleTwoBeds);
			Room room218 = new Room(218, tripleTwoBeds);
			Room room219 = new Room(219, tripleTwoBeds);
			Room room220 = new Room(220, tripleTwoBeds);
			Room room221 = new Room(221, apartment);
			Room room222 = new Room(222, apartment);
			Room room223 = new Room(223, apartment);
			Room room224 = new Room(224, apartment);
			
			Room room301 = new Room(301, single);
			Room room302 = new Room(302, single);
			Room room303 = new Room(303, single);
			Room room304 = new Room(304, single);
			Room room305 = new Room(305, doubleSingleBed);
			Room room306 = new Room(306, doubleSingleBed);
			Room room307 = new Room(307, doubleSingleBed);
			Room room308 = new Room(308, doubleSingleBed);
			Room room309 = new Room(309, doubleTwoBeds);
			Room room310 = new Room(310, doubleTwoBeds);
			Room room311 = new Room(311, doubleTwoBeds);
			Room room312 = new Room(312, doubleTwoBeds);
			Room room313 = new Room(313, tripleThreeBeds);
			Room room314 = new Room(314, tripleThreeBeds);
			Room room315 = new Room(315, tripleThreeBeds);
			Room room316 = new Room(316, tripleThreeBeds);
			Room room317 = new Room(317, tripleTwoBeds);
			Room room318 = new Room(318, tripleTwoBeds);
			Room room319 = new Room(319, tripleTwoBeds);
			Room room320 = new Room(320, tripleTwoBeds);
			Room room321 = new Room(321, apartment);
			Room room322 = new Room(322, apartment);
			Room room323 = new Room(323, apartment);
			Room room324 = new Room(324, apartment);
			

			Room room401 = new Room(401, single);
			Room room402 = new Room(402, single);
			Room room403 = new Room(403, single);
			Room room404 = new Room(404, single);
			Room room405 = new Room(405, doubleSingleBed);
			Room room406 = new Room(406, doubleSingleBed);
			Room room407 = new Room(407, doubleSingleBed);
			Room room408 = new Room(408, doubleSingleBed);
			Room room409 = new Room(409, doubleTwoBeds);
			Room room410 = new Room(410, doubleTwoBeds);
			Room room411 = new Room(411, doubleTwoBeds);
			Room room412 = new Room(412, doubleTwoBeds);
			Room room413 = new Room(413, tripleThreeBeds);
			Room room414 = new Room(414, tripleThreeBeds);
			Room room415 = new Room(415, tripleThreeBeds);
			Room room416 = new Room(416, tripleThreeBeds);
			Room room417 = new Room(417, tripleTwoBeds);
			Room room418 = new Room(418, tripleTwoBeds);
			Room room419 = new Room(419, tripleTwoBeds);
			Room room420 = new Room(420, tripleTwoBeds);
			Room room421 = new Room(421, apartment);
			Room room422 = new Room(422, apartment);
			Room room423 = new Room(423, apartment);
			Room room424 = new Room(424, apartment);
			
			
			Room room501 = new Room(501, single);
			Room room502 = new Room(502, single);
			Room room503 = new Room(503, single);
			Room room504 = new Room(504, single);
			Room room505 = new Room(505, doubleSingleBed);
			Room room506 = new Room(506, doubleSingleBed);
			Room room507 = new Room(507, doubleSingleBed);
			Room room508 = new Room(508, doubleSingleBed);
			Room room509 = new Room(509, doubleTwoBeds);
			Room room510 = new Room(510, doubleTwoBeds);
			Room room511 = new Room(511, doubleTwoBeds);
			Room room512 = new Room(512, doubleTwoBeds);
			Room room513 = new Room(513, tripleThreeBeds);
			Room room514 = new Room(514, tripleThreeBeds);
			Room room515 = new Room(515, tripleThreeBeds);
			Room room516 = new Room(516, tripleThreeBeds);
			Room room517 = new Room(517, tripleTwoBeds);
			Room room518 = new Room(518, tripleTwoBeds);
			Room room519 = new Room(519, tripleTwoBeds);
			Room room520 = new Room(520, tripleTwoBeds);
			Room room521 = new Room(521, apartment);
			Room room522 = new Room(522, apartment);
			Room room523 = new Room(523, apartment);
			Room room524 = new Room(524, apartment);

			Room room601 = new Room(601, penthouse);
			Room room701 = new Room(701, penthouse);
			Room room801 = new Room(801, penthouse);
			
			room101.addRoomAddition(cityView);
			room102.addRoomAddition(jacuzzi);
			room102.addRoomAddition(balcony);
			room102.addRoomAddition(cityView);
			room103.addRoomAddition(wifi);
			room103.addRoomAddition(jacuzzi);
			room103.addRoomAddition(balcony);
			room103.addRoomAddition(cityView);
			room103.addRoomAddition(tv);
			room104.addRoomAddition(balcony);
			room104.addRoomAddition(wifi);
			room105.addRoomAddition(tv);
			room105.addRoomAddition(balcony);
			room105.addRoomAddition(jacuzzi);
			room105.addRoomAddition(cityView);
			room106.addRoomAddition(cityView);
			room106.addRoomAddition(balcony);
			room106.addRoomAddition(tv);
			room106.addRoomAddition(jacuzzi);
			room107.addRoomAddition(wifi);
			room107.addRoomAddition(balcony);
			room107.addRoomAddition(cityView);
			room108.addRoomAddition(balcony);
			room108.addRoomAddition(wifi);
			room108.addRoomAddition(tv);
			room109.addRoomAddition(wifi);
			room109.addRoomAddition(jacuzzi);
			room110.addRoomAddition(balcony);
			room110.addRoomAddition(cityView);
			room110.addRoomAddition(jacuzzi);
			room110.addRoomAddition(wifi);
			room110.addRoomAddition(tv);
			room111.addRoomAddition(balcony);
			room111.addRoomAddition(wifi);
			room111.addRoomAddition(jacuzzi);
			room111.addRoomAddition(cityView);
			room111.addRoomAddition(tv);
			room112.addRoomAddition(cityView);
			room112.addRoomAddition(tv);
			room112.addRoomAddition(balcony);
			room113.addRoomAddition(cityView);
			room113.addRoomAddition(wifi);
			room113.addRoomAddition(jacuzzi);
			room114.addRoomAddition(jacuzzi);
			room114.addRoomAddition(wifi);
			room114.addRoomAddition(tv);
			room114.addRoomAddition(cityView);
			room115.addRoomAddition(tv);
			room115.addRoomAddition(cityView);
			room115.addRoomAddition(wifi);
			room116.addRoomAddition(cityView);
			room116.addRoomAddition(wifi);
			room117.addRoomAddition(balcony);
			room117.addRoomAddition(cityView);
			room117.addRoomAddition(tv);
			room118.addRoomAddition(balcony);
			room118.addRoomAddition(jacuzzi);
			room119.addRoomAddition(cityView);
			room120.addRoomAddition(wifi);
			room120.addRoomAddition(tv);
			room120.addRoomAddition(cityView);
			room120.addRoomAddition(balcony);
			room120.addRoomAddition(jacuzzi);
			room121.addRoomAddition(tv);
			room121.addRoomAddition(cityView);
			room121.addRoomAddition(balcony);
			room122.addRoomAddition(tv);
			room122.addRoomAddition(jacuzzi);
			room123.addRoomAddition(wifi);
			room123.addRoomAddition(cityView);
			room123.addRoomAddition(jacuzzi);
			room124.addRoomAddition(tv);
			room124.addRoomAddition(wifi);
			room124.addRoomAddition(balcony);
			
			room201.addRoomAddition(tv);
			room201.addRoomAddition(wifi);
			room201.addRoomAddition(jacuzzi);
			room201.addRoomAddition(balcony);
			room202.addRoomAddition(jacuzzi);
			room202.addRoomAddition(cityView);
			room202.addRoomAddition(balcony);
			room202.addRoomAddition(tv);
			room202.addRoomAddition(wifi);
			room203.addRoomAddition(wifi);
			room204.addRoomAddition(wifi);
			room205.addRoomAddition(tv);
			room205.addRoomAddition(balcony);
			room206.addRoomAddition(cityView);
			room207.addRoomAddition(tv);
			room207.addRoomAddition(balcony);
			room207.addRoomAddition(jacuzzi);
			room208.addRoomAddition(tv);
			room208.addRoomAddition(jacuzzi);
			room208.addRoomAddition(cityView);
			room208.addRoomAddition(wifi);
			room208.addRoomAddition(balcony);
			room209.addRoomAddition(wifi);
			room209.addRoomAddition(jacuzzi);
			room209.addRoomAddition(tv);
			room209.addRoomAddition(balcony);
			room210.addRoomAddition(wifi);
			room210.addRoomAddition(cityView);
			room210.addRoomAddition(balcony);
			room210.addRoomAddition(tv);
			room211.addRoomAddition(tv);
			room211.addRoomAddition(jacuzzi);
			room211.addRoomAddition(cityView);
			room211.addRoomAddition(wifi);
			room211.addRoomAddition(balcony);
			room212.addRoomAddition(cityView);
			room212.addRoomAddition(tv);
			room212.addRoomAddition(wifi);
			room213.addRoomAddition(wifi);
			room213.addRoomAddition(tv);
			room213.addRoomAddition(cityView);
			room213.addRoomAddition(jacuzzi);
			room213.addRoomAddition(balcony);
			room214.addRoomAddition(wifi);
			room214.addRoomAddition(balcony);
			room214.addRoomAddition(cityView);
			room214.addRoomAddition(jacuzzi);
			room215.addRoomAddition(tv);
			room215.addRoomAddition(cityView);
			room216.addRoomAddition(tv);
			room216.addRoomAddition(wifi);
			room216.addRoomAddition(balcony);
			room217.addRoomAddition(wifi);
			room217.addRoomAddition(cityView);
			room217.addRoomAddition(jacuzzi);
			room217.addRoomAddition(balcony);
			room218.addRoomAddition(tv);
			room218.addRoomAddition(balcony);
			room218.addRoomAddition(wifi);
			room218.addRoomAddition(cityView);
			room219.addRoomAddition(balcony);
			room219.addRoomAddition(tv);
			room219.addRoomAddition(jacuzzi);
			room219.addRoomAddition(cityView);
			room220.addRoomAddition(balcony);
			room220.addRoomAddition(jacuzzi);
			room221.addRoomAddition(cityView);
			room222.addRoomAddition(jacuzzi);
			room222.addRoomAddition(cityView);
			room222.addRoomAddition(tv);
			room222.addRoomAddition(balcony);
			room223.addRoomAddition(balcony);
			room224.addRoomAddition(jacuzzi);
			room224.addRoomAddition(tv);
			
			room301.addRoomAddition(jacuzzi);
			room302.addRoomAddition(balcony);
			room302.addRoomAddition(tv);
			room302.addRoomAddition(cityView);
			room303.addRoomAddition(jacuzzi);
			room303.addRoomAddition(wifi);
			room303.addRoomAddition(balcony);
			room303.addRoomAddition(cityView);
			room303.addRoomAddition(tv);
			room304.addRoomAddition(wifi);
			room304.addRoomAddition(jacuzzi);
			room304.addRoomAddition(balcony);
			room305.addRoomAddition(tv);
			room305.addRoomAddition(balcony);
			room305.addRoomAddition(cityView);
			room306.addRoomAddition(tv);
			room306.addRoomAddition(jacuzzi);
			room306.addRoomAddition(wifi);
			room306.addRoomAddition(cityView);
			room306.addRoomAddition(balcony);
			room307.addRoomAddition(jacuzzi);
			room307.addRoomAddition(cityView);
			room307.addRoomAddition(tv);
			room307.addRoomAddition(wifi);
			room307.addRoomAddition(balcony);
			room308.addRoomAddition(tv);
			room308.addRoomAddition(balcony);
			room308.addRoomAddition(cityView);
			room308.addRoomAddition(wifi);
			room309.addRoomAddition(wifi);
			room309.addRoomAddition(tv);
			room309.addRoomAddition(jacuzzi);
			room310.addRoomAddition(cityView);
			room310.addRoomAddition(balcony);
			room310.addRoomAddition(wifi);
			room310.addRoomAddition(jacuzzi);
			room310.addRoomAddition(tv);
			room311.addRoomAddition(wifi);
			room311.addRoomAddition(balcony);
			room311.addRoomAddition(jacuzzi);
			room311.addRoomAddition(cityView);
			room311.addRoomAddition(tv);
			room312.addRoomAddition(cityView);
			room312.addRoomAddition(balcony);
			room312.addRoomAddition(wifi);
			room312.addRoomAddition(tv);
			room313.addRoomAddition(tv);
			room313.addRoomAddition(jacuzzi);
			room314.addRoomAddition(jacuzzi);
			room314.addRoomAddition(tv);
			room315.addRoomAddition(balcony);
			room315.addRoomAddition(jacuzzi);
			room315.addRoomAddition(wifi);
			room316.addRoomAddition(wifi);
			room316.addRoomAddition(cityView);
			room317.addRoomAddition(cityView);
			room317.addRoomAddition(balcony);
			room317.addRoomAddition(tv);
			room318.addRoomAddition(wifi);
			room318.addRoomAddition(jacuzzi);
			room319.addRoomAddition(cityView);
			room319.addRoomAddition(tv);
			room319.addRoomAddition(balcony);
			room319.addRoomAddition(jacuzzi);
			room320.addRoomAddition(jacuzzi);
			room320.addRoomAddition(balcony);
			room320.addRoomAddition(wifi);
			room321.addRoomAddition(tv);
			room321.addRoomAddition(balcony);
			room321.addRoomAddition(jacuzzi);
			room322.addRoomAddition(cityView);
			room322.addRoomAddition(tv);
			room323.addRoomAddition(tv);
			room323.addRoomAddition(cityView);
			room323.addRoomAddition(wifi);
			room323.addRoomAddition(jacuzzi);
			room324.addRoomAddition(wifi);
			room324.addRoomAddition(tv);
			room324.addRoomAddition(cityView);
			
			room401.addRoomAddition(cityView);
			room401.addRoomAddition(wifi);
			room401.addRoomAddition(balcony);
			room401.addRoomAddition(jacuzzi);
			room401.addRoomAddition(tv);
			room402.addRoomAddition(jacuzzi);
			room402.addRoomAddition(balcony);
			room402.addRoomAddition(wifi);
			room402.addRoomAddition(tv);
			room403.addRoomAddition(wifi);
			room403.addRoomAddition(balcony);
			room403.addRoomAddition(cityView);
			room403.addRoomAddition(jacuzzi);
			room403.addRoomAddition(tv);
			room404.addRoomAddition(tv);
			room405.addRoomAddition(balcony);
			room405.addRoomAddition(wifi);
			room405.addRoomAddition(cityView);
			room405.addRoomAddition(tv);
			room406.addRoomAddition(tv);
			room406.addRoomAddition(balcony);
			room406.addRoomAddition(jacuzzi);
			room406.addRoomAddition(cityView);
			room406.addRoomAddition(wifi);
			room407.addRoomAddition(balcony);
			room407.addRoomAddition(jacuzzi);
			room407.addRoomAddition(wifi);
			room407.addRoomAddition(tv);
			room407.addRoomAddition(cityView);
			room408.addRoomAddition(tv);
			room409.addRoomAddition(balcony);
			room409.addRoomAddition(wifi);
			room409.addRoomAddition(cityView);
			room410.addRoomAddition(wifi);
			room410.addRoomAddition(cityView);
			room410.addRoomAddition(jacuzzi);
			room411.addRoomAddition(jacuzzi);
			room411.addRoomAddition(tv);
			room411.addRoomAddition(wifi);
			room411.addRoomAddition(cityView);
			room412.addRoomAddition(balcony);
			room412.addRoomAddition(cityView);
			room412.addRoomAddition(tv);
			room413.addRoomAddition(balcony);
			room413.addRoomAddition(tv);
			room413.addRoomAddition(wifi);
			room413.addRoomAddition(jacuzzi);
			room414.addRoomAddition(jacuzzi);
			room414.addRoomAddition(cityView);
			room414.addRoomAddition(balcony);
			room415.addRoomAddition(cityView);
			room415.addRoomAddition(tv);
			room415.addRoomAddition(balcony);
			room415.addRoomAddition(wifi);
			room416.addRoomAddition(balcony);
			room416.addRoomAddition(jacuzzi);
			room417.addRoomAddition(tv);
			room418.addRoomAddition(tv);
			room418.addRoomAddition(jacuzzi);
			room419.addRoomAddition(balcony);
			room419.addRoomAddition(tv);
			room420.addRoomAddition(wifi);
			room420.addRoomAddition(tv);
			room420.addRoomAddition(balcony);
			room420.addRoomAddition(cityView);
			room421.addRoomAddition(cityView);
			room421.addRoomAddition(tv);
			room421.addRoomAddition(jacuzzi);
			room421.addRoomAddition(balcony);
			room422.addRoomAddition(wifi);
			room422.addRoomAddition(balcony);
			room422.addRoomAddition(tv);
			room422.addRoomAddition(cityView);
			room423.addRoomAddition(wifi);
			room423.addRoomAddition(cityView);
			room424.addRoomAddition(wifi);
			room424.addRoomAddition(jacuzzi);
			room424.addRoomAddition(balcony);
			room424.addRoomAddition(cityView);
			room424.addRoomAddition(tv);
			
			room501.addRoomAddition(balcony);
			room501.addRoomAddition(cityView);
			room501.addRoomAddition(jacuzzi);
			room501.addRoomAddition(wifi);
			room501.addRoomAddition(tv);
			room502.addRoomAddition(tv);
			room502.addRoomAddition(cityView);
			room503.addRoomAddition(jacuzzi);
			room503.addRoomAddition(tv);
			room504.addRoomAddition(jacuzzi);
			room504.addRoomAddition(balcony);
			room504.addRoomAddition(wifi);
			room505.addRoomAddition(balcony);
			room506.addRoomAddition(cityView);
			room506.addRoomAddition(balcony);
			room506.addRoomAddition(jacuzzi);
			room507.addRoomAddition(cityView);
			room507.addRoomAddition(wifi);
			room507.addRoomAddition(tv);
			room508.addRoomAddition(tv);
			room508.addRoomAddition(cityView);
			room509.addRoomAddition(cityView);
			room509.addRoomAddition(wifi);
			room510.addRoomAddition(tv);
			room510.addRoomAddition(jacuzzi);
			room510.addRoomAddition(wifi);
			room511.addRoomAddition(tv);
			room511.addRoomAddition(jacuzzi);
			room511.addRoomAddition(cityView);
			room512.addRoomAddition(tv);
			room512.addRoomAddition(wifi);
			room512.addRoomAddition(jacuzzi);
			room512.addRoomAddition(cityView);
			room512.addRoomAddition(balcony);
			room513.addRoomAddition(wifi);
			room513.addRoomAddition(balcony);
			room513.addRoomAddition(cityView);
			room513.addRoomAddition(jacuzzi);
			room514.addRoomAddition(jacuzzi);
			room514.addRoomAddition(cityView);
			room514.addRoomAddition(balcony);
			room514.addRoomAddition(wifi);
			room514.addRoomAddition(tv);
			room515.addRoomAddition(balcony);
			room515.addRoomAddition(cityView);
			room515.addRoomAddition(tv);
			room515.addRoomAddition(wifi);
			room516.addRoomAddition(jacuzzi);
			room517.addRoomAddition(wifi);
			room517.addRoomAddition(jacuzzi);
			room518.addRoomAddition(balcony);
			room518.addRoomAddition(cityView);
			room519.addRoomAddition(balcony);
			room519.addRoomAddition(cityView);
			room520.addRoomAddition(tv);
			room520.addRoomAddition(wifi);
			room520.addRoomAddition(cityView);
			room521.addRoomAddition(wifi);
			room522.addRoomAddition(balcony);
			room522.addRoomAddition(jacuzzi);
			room523.addRoomAddition(balcony);
			room523.addRoomAddition(wifi);
			room523.addRoomAddition(tv);
			room524.addRoomAddition(jacuzzi);
			room524.addRoomAddition(wifi);
			room524.addRoomAddition(cityView);
			room524.addRoomAddition(tv);

			
			room601.addRoomAddition(balcony);
			room601.addRoomAddition(cityView);
			room601.addRoomAddition(jacuzzi);
			room601.addRoomAddition(tv);
			room601.addRoomAddition(wifi);
			room601.addRoomAddition(climate);

			room701.addRoomAddition(balcony);
			room701.addRoomAddition(cityView);
			room701.addRoomAddition(jacuzzi);
			room701.addRoomAddition(tv);
			room701.addRoomAddition(wifi);
			room701.addRoomAddition(climate);

			room801.addRoomAddition(balcony);
			room801.addRoomAddition(cityView);
			room801.addRoomAddition(jacuzzi);
			room801.addRoomAddition(tv);
			room801.addRoomAddition(wifi);
			room801.addRoomAddition(climate);

			db.getRooms().insert(room101);
			db.getRooms().insert(room102);
			db.getRooms().insert(room103);
			db.getRooms().insert(room104);
			db.getRooms().insert(room105);
			db.getRooms().insert(room106);
			db.getRooms().insert(room107);
			db.getRooms().insert(room108);
			db.getRooms().insert(room109);
			db.getRooms().insert(room110);
			db.getRooms().insert(room111);
			db.getRooms().insert(room112);
			db.getRooms().insert(room113);
			db.getRooms().insert(room114);
			db.getRooms().insert(room115);
			db.getRooms().insert(room116);
			db.getRooms().insert(room117);
			db.getRooms().insert(room118);
			db.getRooms().insert(room119);
			db.getRooms().insert(room120);
			db.getRooms().insert(room121);
			db.getRooms().insert(room122);
			db.getRooms().insert(room123);
			db.getRooms().insert(room124);
			
			db.getRooms().insert(room201);
			db.getRooms().insert(room202);
			db.getRooms().insert(room203);
			db.getRooms().insert(room204);
			db.getRooms().insert(room205);
			db.getRooms().insert(room206);
			db.getRooms().insert(room207);
			db.getRooms().insert(room208);
			db.getRooms().insert(room209);
			db.getRooms().insert(room210);
			db.getRooms().insert(room211);
			db.getRooms().insert(room212);
			db.getRooms().insert(room213);
			db.getRooms().insert(room214);
			db.getRooms().insert(room215);
			db.getRooms().insert(room216);
			db.getRooms().insert(room217);
			db.getRooms().insert(room218);
			db.getRooms().insert(room219);
			db.getRooms().insert(room220);
			db.getRooms().insert(room221);
			db.getRooms().insert(room222);
			db.getRooms().insert(room223);
			db.getRooms().insert(room224);

			db.getRooms().insert(room301);
			db.getRooms().insert(room302);
			db.getRooms().insert(room303);
			db.getRooms().insert(room304);
			db.getRooms().insert(room305);
			db.getRooms().insert(room306);
			db.getRooms().insert(room307);
			db.getRooms().insert(room308);
			db.getRooms().insert(room309);
			db.getRooms().insert(room310);
			db.getRooms().insert(room311);
			db.getRooms().insert(room312);
			db.getRooms().insert(room313);
			db.getRooms().insert(room314);
			db.getRooms().insert(room315);
			db.getRooms().insert(room316);
			db.getRooms().insert(room317);
			db.getRooms().insert(room318);
			db.getRooms().insert(room319);
			db.getRooms().insert(room320);
			db.getRooms().insert(room321);
			db.getRooms().insert(room322);
			db.getRooms().insert(room323);
			db.getRooms().insert(room324);
			
			db.getRooms().insert(room401);
			db.getRooms().insert(room402);
			db.getRooms().insert(room403);
			db.getRooms().insert(room404);
			db.getRooms().insert(room405);
			db.getRooms().insert(room406);
			db.getRooms().insert(room407);
			db.getRooms().insert(room408);
			db.getRooms().insert(room409);
			db.getRooms().insert(room410);
			db.getRooms().insert(room411);
			db.getRooms().insert(room412);
			db.getRooms().insert(room413);
			db.getRooms().insert(room414);
			db.getRooms().insert(room415);
			db.getRooms().insert(room416);
			db.getRooms().insert(room417);
			db.getRooms().insert(room418);
			db.getRooms().insert(room419);
			db.getRooms().insert(room420);
			db.getRooms().insert(room421);
			db.getRooms().insert(room422);
			db.getRooms().insert(room423);
			db.getRooms().insert(room424);
			
			db.getRooms().insert(room501);
			db.getRooms().insert(room502);
			db.getRooms().insert(room503);
			db.getRooms().insert(room504);
			db.getRooms().insert(room505);
			db.getRooms().insert(room506);
			db.getRooms().insert(room507);
			db.getRooms().insert(room508);
			db.getRooms().insert(room509);
			db.getRooms().insert(room510);
			db.getRooms().insert(room511);
			db.getRooms().insert(room512);
			db.getRooms().insert(room513);
			db.getRooms().insert(room514);
			db.getRooms().insert(room515);
			db.getRooms().insert(room516);
			db.getRooms().insert(room517);
			db.getRooms().insert(room518);
			db.getRooms().insert(room519);
			db.getRooms().insert(room520);
			db.getRooms().insert(room521);
			db.getRooms().insert(room522);
			db.getRooms().insert(room523);
			db.getRooms().insert(room524);

			db.getRooms().insert(room601);

			db.getRooms().insert(room701);

			db.getRooms().insert(room801);

			/* ****************************** Price Lists *************************************** */

			PriceList may = new PriceList(LocalDate.of(2024, 5, 1),  LocalDate.of(2024, 5, 31));
			may.setPrice(single, 1000);
			may.setPrice(doubleSingleBed, 1200);
			may.setPrice(doubleTwoBeds, 1400);
			may.setPrice(tripleThreeBeds, 1600);
			may.setPrice(tripleTwoBeds, 1800);
			may.setPrice(apartment, 2000);
			may.setPrice(penthouse, 3000);
			may.setPrice(breakfast, 120);
			may.setPrice(lunch, 300);
			may.setPrice(dinner, 200);
			may.setPrice(allInclusive, 600);
			may.setPrice(spa, 500);
			may.setPrice(gym, 300);
			may.setPrice(pool, 300);
			may.setPrice(parking, 300);
			may.setPrice(roomService, 300);
			may.setPrice(extraBed, 500);
			db.getPriceLists().insert(may);
			
			PriceList june = new PriceList(LocalDate.of(2024, 6, 1),  LocalDate.of(2024, 6, 30));
			june.setPrice(single, 1200);
			june.setPrice(doubleSingleBed, 1400);
			june.setPrice(doubleTwoBeds, 1600);
			june.setPrice(tripleThreeBeds, 1800);
			june.setPrice(tripleTwoBeds, 2000);
			june.setPrice(apartment, 2200);
			june.setPrice(penthouse, 3200);
			june.setPrice(breakfast, 140);
			june.setPrice(lunch, 320);
			june.setPrice(dinner, 220);
			june.setPrice(allInclusive, 700);
			june.setPrice(spa, 600);
			june.setPrice(gym, 400);
			june.setPrice(pool, 400);
			june.setPrice(parking, 400);
			june.setPrice(roomService, 400);
			june.setPrice(extraBed, 600);
			db.getPriceLists().insert(june);
			
			PriceList july = new PriceList(LocalDate.of(2024, 7, 1),  LocalDate.of(2024, 7, 31));
			july.setPrice(single, 1400);
			july.setPrice(doubleSingleBed, 1600);
			july.setPrice(doubleTwoBeds, 1800);
			july.setPrice(tripleThreeBeds, 2000);
			july.setPrice(tripleTwoBeds, 2200);
			july.setPrice(apartment, 2400);
			july.setPrice(penthouse, 3400);
			july.setPrice(breakfast, 160);
			july.setPrice(lunch, 340);
			july.setPrice(dinner, 240);
			july.setPrice(allInclusive, 800);
			july.setPrice(spa, 700);
			july.setPrice(gym, 500);
			july.setPrice(pool, 500);
			july.setPrice(parking, 500);
			july.setPrice(roomService, 500);
			july.setPrice(extraBed, 700);
			db.getPriceLists().insert(july);
			
			PriceList rest = new PriceList(LocalDate.of(2024, 8, 1),  null);
			rest.setPrice(single, 1000);
			rest.setPrice(doubleSingleBed, 1200);
			rest.setPrice(doubleTwoBeds, 1400);
			rest.setPrice(tripleThreeBeds, 1600);
			rest.setPrice(tripleTwoBeds, 1800);
			rest.setPrice(apartment, 2000);
			rest.setPrice(penthouse, 3000);
			rest.setPrice(breakfast, 120);
			rest.setPrice(lunch, 300);
			rest.setPrice(dinner, 200);
			rest.setPrice(allInclusive, 600);
			rest.setPrice(spa, 500);
			rest.setPrice(gym, 300);
			rest.setPrice(pool, 300);
			rest.setPrice(parking, 300);
			rest.setPrice(roomService, 300);
			rest.setPrice(extraBed, 500);
			db.getPriceLists().insert(rest);
			
			/* ****************************** Reservations *************************************** */
			Reservation r1 = new Reservation(penthouse, djordje, LocalDate.of(2024, 6, 11), LocalDate.of(2024, 6, 14), 4);
			
			r1.addReservationAddition(breakfast);
			r1.addReservationAddition(lunch);
			r1.addReservationAddition(dinner);
			
			r1.addRoomAddition(climate);
			r1.addRoomAddition(wifi);
			
			r1.setPrice(ReservationController.calculateTotalPrice(r1));
			
			db.getReservations().insert(r1);
			
			Reservation r2 = new Reservation(doubleTwoBeds, sofija, LocalDate.of(2024, 6, 12), LocalDate.of(2024, 6, 17), 2);
			
			r2.addReservationAddition(allInclusive);
			r2.addReservationAddition(spa);
			
			r2.addRoomAddition(tv);
			
			r2.setPrice(ReservationController.calculateTotalPrice(r2));
			
			db.getReservations().insert(r2);
			
			Reservation r3 = new Reservation(single, sara2, LocalDate.of(2024, 6, 14), LocalDate.of(2024, 6, 29), 2);
			
			r3.addReservationAddition(extraBed);
			r3.addReservationAddition(roomService);
			r3.addReservationAddition(pool);
			
			r3.addRoomAddition(jacuzzi);
			r3.addRoomAddition(tv);
            r3.setPrice(ReservationController.calculateTotalPrice(r3));
            
            db.getReservations().insert(r3);
            
            CleaningLog cl1 = new CleaningLog(LocalDate.of(2024, 5, 31), nikola);
            db.getCleaningLogs().insert(cl1);
            room101.addCleaningLog(cl1);
            db.getRooms().update(room101);
            
            /*
            // Scenario to test checking availability of rooms
            RoomType testType = new RoomType("Test type", "Test Type");
            db.getRoomTypes().insert(testType);
            Room testRoom = new Room(1000, testType);
            testRoom.addRoomAddition(wifi);
            testRoom.addRoomAddition(tv);
            db.getRooms().insert(testRoom);
            Room testRoom2 = new Room(1001, testType);
            testRoom2.addRoomAddition(tv);
            db.getRooms().insert(testRoom2);
            Room testRoom3 = new Room(1002, testType);
            testRoom3.addRoomAddition(wifi);
            testRoom3.addRoomAddition(tv);
            testRoom3.addRoomAddition(balcony);
            db.getRooms().insert(testRoom3);
            Reservation testReservation2 = new Reservation(testType, djordje, LocalDate.of(2024, 6, 11), LocalDate.of(2024, 6, 20));
            testReservation2.addRoomAddition(wifi);
            testReservation2.addRoomAddition(tv);
            db.getReservations().insert(testReservation2);
            Reservation testReservation3 = new Reservation(testType, djordje, LocalDate.of(2024, 6, 5), LocalDate.of(2024, 6, 17));
            testReservation3.addRoomAddition(tv);
            db.getReservations().insert(testReservation3);
            Reservation testReservation4 = new Reservation(testType, djordje, LocalDate.of(2024, 6, 5), LocalDate.of(2024, 6, 14));
            testReservation4.addRoomAddition(tv);
            testReservation4.addRoomAddition(wifi);
            testReservation4.addRoomAddition(balcony);
            db.getReservations().insert(testReservation4);
            may.setPrice(testType, 1000);
            june.setPrice(testType, 1500);
            july.setPrice(testType, 2000);
            rest.setPrice(testType, 1000);
            */
            
            
			db.save();
			
		} catch (Exception e) {
			System.err.println(e.getMessage());
			e.printStackTrace();
		}
	}

}
