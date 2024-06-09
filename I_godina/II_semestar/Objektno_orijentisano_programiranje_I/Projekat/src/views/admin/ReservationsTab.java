package views.admin;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.table.TableColumnModel;

import controllers.ControllerActionStatus;
import controllers.ReservationController;
import models.Guest;
import models.Reservation;
import models.ReservationAddition;
import utils.CustomTableModel;
import utils.Pair;
import views.components.DataPanel;
import views.components.Tab;
import views.dialogs.reservations.AddReservationDialog;
import views.dialogs.reservations.EditReservationDialog;

public class ReservationsTab extends Tab<Reservation> {

	public ReservationsTab(JFrame parent) {
		super(parent);
	}

	@Override
	protected void addColumns() {
		columns.add(new Pair<String, String>("ID", "id")); // 0
		columns.add(new Pair<String, String>("Status", "status")); // 1
		columns.add(new Pair<String, String>("Guest", "guest")); // 2
		columns.add(new Pair<String, String>("Room Type", "roomType")); // 3
		columns.add(new Pair<String, String>("Start Date", "startDate")); // 4
		columns.add(new Pair<String, String>("End Date", "endDate")); // 5
		columns.add(new Pair<String, String>("Room Additions", "roomAdditions")); // 6
		columns.add(new Pair<String, String>("Reservation Additions", "reservationAdditions")); // 7
		columns.add(new Pair<String, String>("Price", "price")); // 8
		columns.add(new Pair<String, String>("Number of Guests", "numberOfGuests")); // 9
		columns.add(new Pair<String, String>("Room", "room")); // 10
	}

	@Override
	protected void addModel() {
		model = new CustomTableModel<Reservation>(this, columns,
				new CustomTableModel.TableDataManiplations<Reservation>() {

					@Override
					public ArrayList<Reservation> getData() {
						return ReservationController.getReservations();
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
				if (columns.get(columnIndex).getSecond().equals("room")) {
					if (((Reservation) data.get(rowIndex)).getRoom() == null)
						return "";
					return ((Reservation) data.get(rowIndex)).getRoom().getNumber();
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
	}

	@Override
	protected void addDataPanel() {
		dataPanel = new DataPanel<Reservation>(model);
	}

	@Override
	protected void setColumnsSize() {
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
		columnModel.getColumn(9).setMinWidth(150);
		columnModel.getColumn(10).setMinWidth(150);
	}

	@Override
	protected void addRefreshButtonAction() {
		dataPanel.getRefreshBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				((CustomTableModel<ReservationAddition>) dataPanel.getTable().getModel()).refresh();
				dataPanel.getTable().updateUI();
			}
		});
	}

	@Override
	protected void addAddButtonAction() {
		dataPanel.getAddBtn().setText("Add Reservation");
		dataPanel.getAddBtn().addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				AddReservationDialog dialog = new AddReservationDialog(null);
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@SuppressWarnings("unchecked")
					@Override
					public void windowClosed(WindowEvent e) {
						if (!dialog.isOk())
							return;
						ControllerActionStatus status = ((CustomTableModel<Reservation>) dataPanel.getTable()
								.getModel()).add(dialog.getReservation());
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Reservation added successfully",
									"Success", JOptionPane.INFORMATION_MESSAGE);
							break;
						case NO_ROOM:
							JOptionPane.showMessageDialog(parent.getContentPane(), "There is not an available room for this reservation",
									"Error", JOptionPane.ERROR_MESSAGE);
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Reservation already exists",
									"Error", JOptionPane.ERROR_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Error adding reservation", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						}
						dataPanel.getTable().updateUI();
					}
				});
			}
		});
	}

	@Override
	protected void addEditButtonAction() {
		dataPanel.getEditBtn().setText("Edit Reservation");
		dataPanel.getEditBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				CustomTableModel<Reservation> customTableModel = (CustomTableModel<Reservation>) dataPanel.getTable()
						.getModel();
				Reservation reservation = (Reservation) customTableModel.get(dataPanel.getTable().getSelectedRow());
				EditReservationDialog dialog;
				try {
					dialog = new EditReservationDialog((Reservation)reservation.clone());
				} catch (CloneNotSupportedException e1) {
					e1.printStackTrace();
					return;
				}
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@SuppressWarnings("rawtypes")
					@Override
					public void windowClosed(WindowEvent e) {
						if (!dialog.isOk())
							return;
						ControllerActionStatus status = ((CustomTableModel) dataPanel.getTable().getModel())
								.edit(dialog.getReservation());
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Reservation edited successfully",
									"Success", JOptionPane.INFORMATION_MESSAGE);
							break;
						case NO_ROOM:
							JOptionPane.showMessageDialog(parent.getContentPane(), "There is not an available room for this reservation",
									"Error", JOptionPane.ERROR_MESSAGE);
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Reservation already exists",
									"Error", JOptionPane.ERROR_MESSAGE);
							break;
						case OLD:
							JOptionPane.showMessageDialog(parent.getContentPane(), "You cannot edit reservations from the past", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						case NO_RECORD:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Reservation not found", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Error editing reservation", "Error",
									JOptionPane.ERROR_MESSAGE);

						}
						dataPanel.getTable().updateUI();
					}
				});
			}
		});
	}

	@Override
	protected void addRemoveButtonAction() {
		dataPanel.getDeleteBtn().setText("Delete Reservation");
		dataPanel.getDeleteBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				CustomTableModel<Reservation> customTableModel = (CustomTableModel<Reservation>) dataPanel.getTable()
						.getModel();
				int res = JOptionPane.showConfirmDialog(parent.getContentPane(),
						"Are you sure you want to delete this reservation?", "Delete reservation",
						JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
				if (res != JOptionPane.YES_OPTION)
					return;
				ControllerActionStatus status = customTableModel.remove(dataPanel.getTable().getSelectedRow());
				switch (status) {
				case SUCCESS:
					JOptionPane.showMessageDialog(parent.getContentPane(), "Reservation deleted successfully",
							"Success", JOptionPane.INFORMATION_MESSAGE);
					break;
				case NO_RECORD:
					JOptionPane.showMessageDialog(parent.getContentPane(), "Reservation not found", "Error",
							JOptionPane.ERROR_MESSAGE);
					break;
				default:
					JOptionPane.showMessageDialog(parent.getContentPane(), "Error deleting reservation", "Error",
							JOptionPane.ERROR_MESSAGE);
					break;
				}
				dataPanel.getTable().updateUI();
			}
		});
	}

}
