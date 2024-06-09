package views.admin;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.Frame;
import java.util.ArrayList;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;
import javax.swing.border.EmptyBorder;

import utils.WindowUtils;
import views.components.Tab;

public class MainAdmin extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private JTabbedPane tabbedPane;
	private ArrayList<Tab<?>> tabs;

	@SuppressWarnings("unchecked")
	public MainAdmin() {
		setIconImage(WindowUtils.getIconImage());
		setTitle("MHotelify | Admin");
		setForeground(new Color(255, 255, 255));
		setBackground(new Color(73, 73, 73));
		setBounds(200, 100, 600, 600);
		setLocationRelativeTo(null);
		setExtendedState(Frame.MAXIMIZED_BOTH);
		setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);

		addMenu();

		contentPane = new JPanel();
		contentPane.setForeground(new Color(255, 255, 255));
		contentPane.setBorder(new EmptyBorder(0, 0, 0, 0));
		contentPane.setBackground(new Color(73, 73, 73));

		setContentPane(contentPane);
		contentPane.setLayout(new BorderLayout(0, 0));

		tabbedPane = new JTabbedPane(JTabbedPane.LEFT);
		tabbedPane.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		tabbedPane.setForeground(new Color(255, 255, 255));
		tabbedPane.setBackground(new Color(73, 73, 73));
		tabbedPane.setTabLayoutPolicy(JTabbedPane.SCROLL_TAB_LAYOUT);
		contentPane.add(tabbedPane, BorderLayout.CENTER);

		tabs = new ArrayList<Tab<?>>();

		addEmpoloyeesTab();
		addGuestsTab();
		addRoomsTab();
		addRoomAdditionsTab();
		addRoomTypesTab();
		addReservationAdditionsTab();
		addReservationsTab();
		addPriceListsTab();

		for (Tab<?> tab : tabs) {
			tab.setTabs((ArrayList<Tab<?>>) tabs.clone());
			tab.removeTab(tab);
		}
		ReportsTab reportsTab = new ReportsTab();
		tabbedPane.addTab("Reports", new ImageIcon("./assets/icons/guests.png"), reportsTab, null);

		addWindowListener(WindowUtils.getWindowClosing());

	}

	private void addMenu() {
		setJMenuBar(new AdminMenu(this));
	}

	private void addGuestsTab() {
		GuestsTab guestsTab = new GuestsTab(this);
		tabs.add(guestsTab);
		tabbedPane.addTab("Guests", new ImageIcon("./assets/icons/guests.png"), guestsTab.getDataPanel(), null);
	}

	private void addEmpoloyeesTab() {
		EmployeesTab employeesTab = new EmployeesTab(this);
		tabs.add(employeesTab);
		tabbedPane.addTab("Employees", new ImageIcon("./assets/icons/employees.png"), employeesTab.getDataPanel(),
				null);
	}

	private void addRoomsTab() {
		RoomsTab roomsTab = new RoomsTab(this);
		tabs.add(roomsTab);
		tabbedPane.addTab("Rooms", new ImageIcon("./assets/icons/rooms.png"), roomsTab.getDataPanel(), null);
	}

	private void addRoomAdditionsTab() {
		RoomAdditionsTab roomsAdditionsTab = new RoomAdditionsTab(this);
		tabs.add(roomsAdditionsTab);
		tabbedPane.addTab("Room Additions", new ImageIcon("./assets/icons/room_additions.png"),
				roomsAdditionsTab.getDataPanel(), null);
	}

	private void addRoomTypesTab() {
		RoomTypesTab roomTypesTab = new RoomTypesTab(this);
		tabs.add(roomTypesTab);
		tabbedPane.addTab("Room Types", new ImageIcon("./assets/icons/room_types.png"), roomTypesTab.getDataPanel(),
				null);
	}

	private void addReservationAdditionsTab() {
		ReservationAdditionsTab reservationAdditionsTab = new ReservationAdditionsTab(this);
		tabs.add(reservationAdditionsTab);
		tabbedPane.addTab("Reservation Additions", new ImageIcon("./assets/icons/reservation_additions.png"),
				reservationAdditionsTab.getDataPanel(), null);
	}

	private void addReservationsTab() {
		ReservationsTab reservationTab = new ReservationsTab(this);
		tabs.add(reservationTab);
		tabbedPane.addTab("Reservations", new ImageIcon("./assets/icons/reservations.png"),
				reservationTab.getDataPanel(), null);
	}

	private void addPriceListsTab() {
		PriceListsTab priceListsTab = new PriceListsTab(this);
		tabs.add(priceListsTab);
		tabbedPane.addTab("Price Lists", new ImageIcon("./assets/icons/price_lists.png"), priceListsTab.getDataPanel(),
				null);
	}

}
