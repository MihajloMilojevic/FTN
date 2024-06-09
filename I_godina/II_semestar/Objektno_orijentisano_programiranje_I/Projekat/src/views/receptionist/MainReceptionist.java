package views.receptionist;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.Frame;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.ArrayList;

import javax.swing.Box;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.table.TableColumnModel;

import controllers.ControllerActionStatus;
import controllers.ReservationController;
import controllers.UserController;
import models.Guest;
import models.Reservation;
import utils.CustomTableModel;
import utils.Filters;
import utils.Pair;
import utils.WindowUtils;
import views.components.DataPanel;
import views.components.FiltersDialog;
import views.dialogs.guests.AddGuestDialog;
import views.dialogs.reservations.AddReservationDialog;
import views.dialogs.reservations.EditReservationDialog;

public class MainReceptionist extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private JPanel toolBar;
	private JButton filtersBtn;
	private JButton checkInBtn;
	private JButton checkOutBtn;
	private JButton addGuestBtn;
	private DataPanel<Reservation> dataPanel;
	private CustomTableModel<Reservation> model;

	// @SuppressWarnings("unchecked")
	public MainReceptionist() {
		setIconImage(WindowUtils.getIconImage());
		setTitle("MHotelify | Receptionist");
		setForeground(new Color(255, 255, 255));
		setBackground(new Color(73, 73, 73));
		setBounds(200, 100, 754, 586);
		setLocationRelativeTo(null);
		setExtendedState(Frame.MAXIMIZED_BOTH);
		setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);

		Filters.reset();

		addMenu();

		contentPane = new JPanel();
		contentPane.setForeground(new Color(255, 255, 255));
		contentPane.setBackground(new Color(73, 73, 73));

		setContentPane(contentPane);
		contentPane.setLayout(new BorderLayout(0, 0));

		JPanel topPanel = new JPanel();
		topPanel.setBackground(new Color(73, 73, 73));
		contentPane.add(topPanel, BorderLayout.NORTH);
		topPanel.setLayout(new BorderLayout(0, 0));

		toolBar = new JPanel();
		FlowLayout flowLayout_1 = (FlowLayout) toolBar.getLayout();
		flowLayout_1.setAlignment(FlowLayout.LEFT);
		toolBar.setForeground(new Color(255, 255, 255));
		toolBar.setBackground(new Color(73, 73, 73));
		topPanel.add(toolBar, BorderLayout.CENTER);

		addButtons();
		addReservations();

		addWindowListener(WindowUtils.getWindowClosing());
	}

	private void addMenu() {
		setJMenuBar(new ReceptionistMenu(this));
	}

	private void addButtons() {

		filtersBtn = new JButton("Filters");
		filtersBtn.setIcon(new ImageIcon("./assets/icons/filters.png"));
		filtersBtn.setMnemonic('F');
		filtersBtn.setFont(new Font("Tahoma", Font.PLAIN, 14));
		filtersBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				FiltersDialog dialog = new FiltersDialog();
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@Override
					public void windowClosed(WindowEvent windowEvent) {
						model.refresh();
						dataPanel.getTable().updateUI();
					}
				});
			}
		});
		toolBar.add(filtersBtn);

		Component horizontalStrut_1 = Box.createHorizontalStrut(25);
		toolBar.add(horizontalStrut_1);

		checkInBtn = new JButton("Check IN");
		checkInBtn.setIcon(new ImageIcon("./assets/icons/check_in.png"));
		checkInBtn.setFont(new Font("Tahoma", Font.PLAIN, 14));
		checkInBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				CheckINDialog dialog = new CheckINDialog();
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@Override
					public void windowClosed(WindowEvent windowEvent) {
						model.refresh();
						dataPanel.getTable().updateUI();
					}
				});
			}
		});
		toolBar.add(checkInBtn);

		checkOutBtn = new JButton("Check OUT");
		checkOutBtn.setIcon(new ImageIcon("./assets/icons/check_out.png"));
		checkOutBtn.setFont(new Font("Tahoma", Font.PLAIN, 14));
		checkOutBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				CheckOUTDialog dialog = new CheckOUTDialog();
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@Override
					public void windowClosed(WindowEvent windowEvent) {
						model.refresh();
						dataPanel.getTable().updateUI();
					}
				});
			}
		});
		toolBar.add(checkOutBtn);

		Component horizontalStrut = Box.createHorizontalStrut(25);
		toolBar.add(horizontalStrut);

		addGuestBtn = new JButton("Add Guest");
		addGuestBtn.setIcon(new ImageIcon("./assets/icons/plus.png"));
		addGuestBtn.setFont(new Font("Tahoma", Font.PLAIN, 14));
		addGuestBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				AddGuestDialog dialog = new AddGuestDialog();
				dialog.setVisible(true);
				dialog.addWindowListener(WindowUtils.getWindowClosing());
				dialog.addWindowListener(new WindowAdapter() {
					@Override
					public void windowClosed(WindowEvent windowEvent) {
						if (!dialog.isOk())
							return;
						Guest guest = dialog.getGuest();
						ControllerActionStatus status = UserController.addUser(guest);
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(contentPane, "Guest added successfully", "Success",
									JOptionPane.INFORMATION_MESSAGE);
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(contentPane, "Guest already exists", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(contentPane, "An error occured", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						}
					}
				});
			}
		});
		toolBar.add(addGuestBtn);
	}

	private void addReservations() {

		ArrayList<Pair<String, String>> columns = new ArrayList<Pair<String, String>>();
		columns.add(new Pair<String, String>("ID", "id")); // 0
		columns.add(new Pair<String, String>("Status", "status")); // 1
		columns.add(new Pair<String, String>("Guest", "guest")); // 2
		columns.add(new Pair<String, String>("Room Type", "roomType")); // 3
		columns.add(new Pair<String, String>("Start Date", "startDate")); // 4
		columns.add(new Pair<String, String>("End Date", "endDate")); // 5
		columns.add(new Pair<String, String>("Room Additions", "roomAdditions")); // 6
		columns.add(new Pair<String, String>("Reservation Additions", "reservationAdditions")); // 7
		columns.add(new Pair<String, String>("Price", "price")); // 8

		model = new CustomTableModel<Reservation>(columns, new CustomTableModel.TableDataManiplations<Reservation>() {

			@Override
			public ArrayList<Reservation> getData() {
				return ReservationController.getReservations(Filters.getCondition());
			}

			@Override
			public ControllerActionStatus edit(Reservation model) {
				return ReservationController.updateReservation(model);
			}

			@Override
			public ControllerActionStatus remove(Reservation model) {
				return ReservationController.deleteReservation(model);
			}

			@Override
			public ControllerActionStatus add(Reservation model) {
				return ReservationController.addReservation(model);
			}

		}, new Reservation()) {

			private static final long serialVersionUID = -172170127567309241L;

			@Override
			public Object getValueAt(int rowIndex, int columnIndex) {
				if (columns.get(columnIndex).getSecond().equals("roomAdditions")) {
					return String.join(", ", ((Reservation) data.get(rowIndex)).getRoomAdditions().stream()
							.map(ra -> ra.getName()).toArray(String[]::new));
				}
				if (columns.get(columnIndex).getSecond().equals("reservationAdditions")) {
					return String.join(", ", ((Reservation) data.get(rowIndex)).getReservationAdditions().stream()
							.map(ra -> ra.getName()).toArray(String[]::new));
				}
				if (columns.get(columnIndex).getSecond().equals("roomType")) {
					if (((Reservation) data.get(rowIndex)).getRoomType() == null)
						return "";
					return ((Reservation) data.get(rowIndex)).getRoomType().getName();
				}
				if (columns.get(columnIndex).getSecond().equals("guest")) {
					Guest g = ((Guest) data.get(rowIndex).getGuest());
					return g.getName() + " " + g.getSurname();
				}
				return super.getValueAt(rowIndex, columnIndex);
			}

			@Override
			public Class<?> getColumnClass(int columnIndex) {
				if (columns.get(columnIndex).getSecond().equals("roomAdditions")) {
					return String.class;
				}
				if (columns.get(columnIndex).getSecond().equals("reservationAdditions")) {
					return String.class;
				}
				if (columns.get(columnIndex).getSecond().equals("roomType")) {
					return String.class;
				}
				if (columns.get(columnIndex).getSecond().equals("guest")) {
					return String.class;
				}
				return super.getColumnClass(columnIndex);
			}

		};

		dataPanel = new DataPanel<Reservation>(model);

		TableColumnModel columnModel = dataPanel.getTable().getColumnModel();
		columnModel.getColumn(0).setMinWidth(150);
		columnModel.getColumn(1).setMinWidth(150);
		columnModel.getColumn(2).setMinWidth(250);
		columnModel.getColumn(3).setMinWidth(200);
		columnModel.getColumn(4).setMinWidth(150);
		columnModel.getColumn(5).setMinWidth(150);
		columnModel.getColumn(6).setMinWidth(350);
		columnModel.getColumn(7).setMinWidth(350);
		columnModel.getColumn(8).setMinWidth(150);

		dataPanel.getRefreshBtn().addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				model.refresh();
				dataPanel.getTable().updateUI();
			}
		});
		dataPanel.getAddBtn().setText("Add Reservation");
		dataPanel.getAddBtn().addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				AddReservationDialog dialog = new AddReservationDialog(null);
				dialog.setVisible(true);
				dialog.addWindowListener(WindowUtils.getWindowClosing());
				dialog.addWindowListener(new WindowAdapter() {
					@Override
					public void windowClosed(WindowEvent windowEvent) {
						if (!dialog.isOk())
							return;
						Reservation reservation = dialog.getReservation();
						ControllerActionStatus status = model.add(reservation);
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(contentPane, "Reservation added successfully", "Success",
									JOptionPane.INFORMATION_MESSAGE);
							break;
						case NO_ROOM:
							JOptionPane.showMessageDialog(contentPane,
									"There is not an available room for this reservation", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(contentPane, "Reservation already exists", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(contentPane, "An error occured", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						}
						dataPanel.getTable().updateUI();
					}
				});
			}
		});

		dataPanel.getEditBtn().setText("Edit Reservation");
		dataPanel.getEditBtn().addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				Reservation reservation = model.get(dataPanel.getTable().getSelectedRow());
				EditReservationDialog dialog = new EditReservationDialog(reservation);
				dialog.setVisible(true);
				dialog.addWindowListener(WindowUtils.getWindowClosing());
				dialog.addWindowListener(new WindowAdapter() {
					@Override
					public void windowClosed(WindowEvent windowEvent) {
						if (!dialog.isOk())
							return;
						Reservation updatedReservation = dialog.getReservation();
						ControllerActionStatus status = model.edit(updatedReservation);
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(contentPane, "Reservation updated successfully", "Success",
									JOptionPane.INFORMATION_MESSAGE);
							break;
						case NO_ROOM:
							JOptionPane.showMessageDialog(contentPane,
									"There is not an available room for this reservation", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						case OLD:
							JOptionPane.showMessageDialog(contentPane, "You cannot edit reservations from the past",
									"Error", JOptionPane.ERROR_MESSAGE);
							break;
						case NO_RECORD:
							JOptionPane.showMessageDialog(contentPane, "Reservation not found", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(contentPane, "Reservation already exists", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(contentPane, "An error occured", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						}
						dataPanel.getTable().updateUI();
					}
				});
			}
		});

		dataPanel.getDeleteBtn().setVisible(false);

		dataPanel.addButton("Approve Reservation", "./assets/icons/approve.png", new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				int res = JOptionPane.showConfirmDialog(contentPane,
						"Are you sure you want to approve this reservation?", "Approve Reservation",
						JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
				if (res != JOptionPane.YES_OPTION)
					return;
				Reservation reservation = model.get(dataPanel.getTable().getSelectedRow());
				ControllerActionStatus status = ReservationController.approveReservation(reservation);
				switch (status) {
				case SUCCESS:
					JOptionPane.showMessageDialog(contentPane, "Reservation approved successfully", "Success",
							JOptionPane.INFORMATION_MESSAGE);
					break;
				case NO_ROOM:
					JOptionPane.showMessageDialog(contentPane, "There is not an available room for this reservation",
							"Error", JOptionPane.ERROR_MESSAGE);
					break;
				case INCORECT_STATUS:
					JOptionPane.showMessageDialog(contentPane, "Only pending reservations can be approved", "Error",
							JOptionPane.ERROR_MESSAGE);
					break;
				case NO_RECORD:
					JOptionPane.showMessageDialog(contentPane, "Reservation not found", "Error",
							JOptionPane.ERROR_MESSAGE);
					break;
				default:
					JOptionPane.showMessageDialog(contentPane, "An error occured", "Error", JOptionPane.ERROR_MESSAGE);
					break;
				}
				model.refresh();
				dataPanel.getTable().updateUI();
			}
		}, true);

		dataPanel.addButton("Reject Reservation", "./assets/icons/reject.png", new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				int res = JOptionPane.showConfirmDialog(contentPane,
						"Are you sure you want to reject this reservation?", "Reject Reservation",
						JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
				if (res != JOptionPane.YES_OPTION)
					return;
				Reservation reservation = model.get(dataPanel.getTable().getSelectedRow());
				ControllerActionStatus status = ReservationController.rejectReservation(reservation);
				switch (status) {
				case SUCCESS:
					JOptionPane.showMessageDialog(contentPane, "Reservation rejected successfully", "Success",
							JOptionPane.INFORMATION_MESSAGE);
					break;
				case NO_RECORD:
					JOptionPane.showMessageDialog(contentPane, "Reservation not found", "Error",
							JOptionPane.ERROR_MESSAGE);
					break;
				case INCORECT_STATUS:
					JOptionPane.showMessageDialog(contentPane, "Only pending reservations can be rejected", "Error",
							JOptionPane.ERROR_MESSAGE);
					break;
				default:
					JOptionPane.showMessageDialog(contentPane, "An error occured", "Error", JOptionPane.ERROR_MESSAGE);
					break;
				}
				model.refresh();
				dataPanel.getTable().updateUI();
			}
		}, true);

		contentPane.add(dataPanel, BorderLayout.CENTER);
	}
}
