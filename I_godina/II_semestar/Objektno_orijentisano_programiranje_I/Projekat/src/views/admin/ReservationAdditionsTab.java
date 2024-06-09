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
import models.ReservationAddition;
import utils.CustomTableModel;
import utils.CustomTableModelWithInitialPrice;
import utils.Pair;
import views.components.DataPanel;
import views.components.Tab;
import views.dialogs.reservation_additions.AddReservationAdditionDialog;
import views.dialogs.room_additions.EditRoomAdditionDialog;

public class ReservationAdditionsTab extends Tab<ReservationAddition> {

	public ReservationAdditionsTab(JFrame parent) {
		super(parent);
	}

	@Override
	protected void addColumns() {
		columns.add(new Pair<String, String>("ID", "id")); // 0
		columns.add(new Pair<String, String>("Name", "name")); // 1
	}

	@Override
	protected void addModel() {
		model = new CustomTableModelWithInitialPrice<ReservationAddition>(this, columns,
				new CustomTableModelWithInitialPrice.TableDataManiplationsWithPrice<ReservationAddition>() {

					@Override
					public ArrayList<ReservationAddition> getData() {
						return ReservationController.getReservationAdditions();
					}

					@Override
					public ControllerActionStatus edit(ReservationAddition model) {
						return ReservationController.updateReservationAddition(model);
					}

					@Override
					public ControllerActionStatus remove(ReservationAddition model) {
						return ReservationController.deleteReservationAddition(model);
					}

					@Override
					public ControllerActionStatus add(ReservationAddition model) {
						throw new UnsupportedOperationException();
					}

					@Override
					public ControllerActionStatus add(ReservationAddition model, double price) {
						return ReservationController.addReservationAddition(model, price);
					}

				}, new ReservationAddition());
	}

	@Override
	protected void addDataPanel() {
		dataPanel = new DataPanel<ReservationAddition>(model);
	}

	@Override
	protected void setColumnsSize() {
		TableColumnModel columnModel = dataPanel.getTable().getColumnModel();
		columnModel.getColumn(0).setMinWidth(150);
		columnModel.getColumn(1).setMinWidth(500);
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
		dataPanel.getAddBtn().setText("Add Reservation Addition");
		dataPanel.getAddBtn().addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				AddReservationAdditionDialog dialog = new AddReservationAdditionDialog();
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@SuppressWarnings("unchecked")
					@Override
					public void windowClosed(WindowEvent e) {
						if (!dialog.isOk())
							return;
						ControllerActionStatus status = ((CustomTableModelWithInitialPrice<ReservationAddition>) dataPanel
                                .getTable().getModel()).add(new ReservationAddition(dialog.getValue()), dialog.getPrice());
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(parent, "Reservation Addition added successfully");
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(parent, "Reservation Addition with this ID already exists",
									"Error", JOptionPane.ERROR_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(parent, "An error occured", "Error",
									JOptionPane.ERROR_MESSAGE);
						}
						dataPanel.getTable().updateUI();
					}
				});

			}
		});
	}

	@Override
	protected void addEditButtonAction() {
		dataPanel.getEditBtn().setText("Edit Reservation Addition");
		dataPanel.getEditBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				CustomTableModel<ReservationAddition> customTableModel = (CustomTableModel<ReservationAddition>) dataPanel
						.getTable().getModel();
				ReservationAddition reservationAddition = (ReservationAddition) customTableModel
						.get(dataPanel.getTable().getSelectedRow());
				EditRoomAdditionDialog dialog = new EditRoomAdditionDialog(reservationAddition.getName());
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@SuppressWarnings("rawtypes")
					@Override
					public void windowClosed(WindowEvent e) {
						if (!dialog.isOk())
							return;
						reservationAddition.setName(dialog.getValue());
						ControllerActionStatus status = ((CustomTableModel) dataPanel.getTable().getModel())
								.edit(reservationAddition);
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(parent, "Reservation Addition edited successfully");
							break;
						case NO_RECORD:
							JOptionPane.showMessageDialog(parent, "Reservation Addition not found", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(parent, "Reservation Addition with this ID already exists",
									"Error", JOptionPane.ERROR_MESSAGE);
						default:
							JOptionPane.showMessageDialog(parent, "An error occured", "Error",
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
		dataPanel.getDeleteBtn().setText("Delete Reservation Addition");
		dataPanel.getDeleteBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				CustomTableModel<ReservationAddition> customTableModel = (CustomTableModel<ReservationAddition>) dataPanel
						.getTable().getModel();
				int res = JOptionPane.showConfirmDialog(parent.getContentPane(),
						"Are you sure you want to delete this reservation addition?", "Delete reservation addition",
						JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
				if (res != JOptionPane.YES_OPTION)
					return;
				ControllerActionStatus status = customTableModel.remove(dataPanel.getTable().getSelectedRow());
				switch (status) {
				case SUCCESS:
					JOptionPane.showMessageDialog(parent, "Reservation Addition deleted successfully");
					break;
				case NO_RECORD:
					JOptionPane.showMessageDialog(parent, "Reservation Addition not found", "Error",
							JOptionPane.ERROR_MESSAGE);
					break;
				default:
					JOptionPane.showMessageDialog(parent, "An error occured", "Error", JOptionPane.ERROR_MESSAGE);
				}
				dataPanel.getTable().updateUI();
			}
		});
	}

}
