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
import controllers.UserController;
import models.Guest;
import utils.CustomTableModel;
import utils.Pair;
import views.components.DataPanel;
import views.components.Tab;
import views.dialogs.guests.AddGuestDialog;
import views.dialogs.guests.EditGuestDialog;

public class GuestsTab extends Tab<Guest> {
	
	public GuestsTab(JFrame parent) {
		super(parent);
	}
	
	@Override
	protected void addColumns() {
		columns.add(new Pair<String, String>("ID", "id")); // 0
		columns.add(new Pair<String, String>("Role", "role")); // 1
		columns.add(new Pair<String, String>("Name", "name")); // 2
		columns.add(new Pair<String, String>("Surname", "surname")); // 3
		columns.add(new Pair<String, String>("Username", "username")); // 4
		columns.add(new Pair<String, String>("Gender", "gender")); // 5
		columns.add(new Pair<String, String>("Date of birth", "birthdate")); // 6
		columns.add(new Pair<String, String>("Address", "address")); // 7
		columns.add(new Pair<String, String>("Phone", "phone")); // 8 // 11
	}

	@Override
	protected void addModel() {
		model = new CustomTableModel<Guest>(this, columns,
				new CustomTableModel.TableDataManiplations<Guest>() {

					@Override
					public ArrayList<Guest> getData() {
						return UserController.getGuests();
					}

					@Override
					public ControllerActionStatus edit(Guest model) {
						return UserController.updateUser(model);
					}

					@Override
					public ControllerActionStatus remove(Guest model) {
						return UserController.deleteUser(model);
					}

					@Override
					public ControllerActionStatus add(Guest model) {
						return UserController.addUser(model);
					}

				}, new Guest());
		
	}

	@Override
	protected void addDataPanel() {
		dataPanel = new DataPanel<Guest>(model);
	}

	@Override
	protected void setColumnsSize() {
		TableColumnModel columnModel = dataPanel.getTable().getColumnModel();
		columnModel.getColumn(0).setMinWidth(150);
		columnModel.getColumn(1).setMinWidth(150);
		columnModel.getColumn(2).setMinWidth(100);
		columnModel.getColumn(3).setMinWidth(100);
		columnModel.getColumn(4).setMinWidth(100);
		columnModel.getColumn(5).setMinWidth(100);
		columnModel.getColumn(6).setMinWidth(100);
		columnModel.getColumn(7).setMinWidth(300);
		columnModel.getColumn(8).setMinWidth(150);
	}

	@Override
	protected void addRefreshButtonAction() {
		dataPanel.getRefreshBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				((CustomTableModel<Guest>) dataPanel.getTable().getModel()).refresh();
				dataPanel.getTable().updateUI();
			}
		});
	}

	@Override
	protected void addAddButtonAction() {
		dataPanel.getAddBtn().setText("Add Guest");
		
		dataPanel.getAddBtn().addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				AddGuestDialog dialog = new AddGuestDialog();
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@SuppressWarnings("unchecked")
					@Override
					public void windowClosed(WindowEvent e) {
						if (!dialog.isOk())
							return;
						ControllerActionStatus status = ((CustomTableModel<Guest>) dataPanel.getTable().getModel()).add(dialog.getGuest());
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Guest added successfully", "Success",
									JOptionPane.INFORMATION_MESSAGE);
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(parent.getContentPane(), "User with this username already exists",
									"Error", JOptionPane.ERROR_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(parent.getContentPane(), "An error occured", "Error",
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
		dataPanel.getEditBtn().setText("Edit Guest");
		
		dataPanel.getEditBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {

				CustomTableModel<Guest> customTableModel = (CustomTableModel<Guest>) dataPanel.getTable().getModel();
				Guest guest = (Guest) customTableModel.get(dataPanel.getTable().getSelectedRow());
				EditGuestDialog dialog = new EditGuestDialog(guest);
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@SuppressWarnings("rawtypes")
					@Override
					public void windowClosed(WindowEvent e) {
						if (!dialog.isOk())
							return;
						ControllerActionStatus status = ((CustomTableModel) dataPanel.getTable().getModel()).edit(guest);
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Guest updated successfully", "Success",
									JOptionPane.INFORMATION_MESSAGE);
							break;
						case NO_RECORD:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Guest not found", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(parent.getContentPane(), "User with this username already exists",
									"Error", JOptionPane.ERROR_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(parent.getContentPane(), "An error occured", "Error",
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
		dataPanel.getDeleteBtn().setText("Delete Guest");
		
		dataPanel.getDeleteBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				CustomTableModel<Guest> customTableModel = (CustomTableModel<Guest>) dataPanel.getTable().getModel();
				int res = JOptionPane.showConfirmDialog(parent.getContentPane(), "Are you sure you want to delete this user?",
						"Delete user", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
				if (res != JOptionPane.YES_OPTION)
					return;
				ControllerActionStatus status = customTableModel.remove(dataPanel.getTable().getSelectedRow());
				switch (status) {
				case SUCCESS:
					JOptionPane.showMessageDialog(parent.getContentPane(), "Guest deleted successfully", "Success",
							JOptionPane.INFORMATION_MESSAGE);
					break;
				case NO_RECORD:
					JOptionPane.showMessageDialog(parent.getContentPane(), "Guest not found", "Error", JOptionPane.ERROR_MESSAGE);
					break;
				default:
					JOptionPane.showMessageDialog(parent.getContentPane(), "An error occured", "Error", JOptionPane.ERROR_MESSAGE);
				}
				dataPanel.getTable().updateUI();
			}
		});
	}
	
}
