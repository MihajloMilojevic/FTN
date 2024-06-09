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
import controllers.RoomController;
import models.RoomAddition;
import utils.CustomTableModel;
import utils.Pair;
import views.components.DataPanel;
import views.components.Tab;
import views.dialogs.room_additions.AddRoomAdditionDialog;
import views.dialogs.room_additions.EditRoomAdditionDialog;

public class RoomAdditionsTab extends Tab<RoomAddition> {

	public RoomAdditionsTab(JFrame parent) {
		super(parent);
	}

	@Override
	protected void addColumns() {
		columns.add(new Pair<String, String>("ID", "id")); // 0
		columns.add(new Pair<String, String>("Name", "name")); // 1
	}

	@Override
	protected void addModel() {
		model = new CustomTableModel<RoomAddition>(this, columns,
				new CustomTableModel.TableDataManiplations<RoomAddition>() {

					@Override
					public ArrayList<RoomAddition> getData() {
						return RoomController.getRoomAdditions();
					}

					@Override
					public ControllerActionStatus edit(RoomAddition model) {
						return RoomController.updateRoomAddition(model);
					}

					@Override
					public ControllerActionStatus remove(RoomAddition model) {
						return RoomController.deleteRoomAddition(model);
					}

					@Override
					public ControllerActionStatus add(RoomAddition model) {
						return RoomController.addRoomAddition(model);
					}

				}, new RoomAddition());
	}

	@Override
	protected void addDataPanel() {
		dataPanel = new DataPanel<RoomAddition>(model);
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
				((CustomTableModel<RoomAddition>) dataPanel.getTable().getModel()).refresh();
				dataPanel.getTable().updateUI();
			}
		});
	}

	@Override
	protected void addAddButtonAction() {
		dataPanel.getAddBtn().setText("Add Room Addition");
		dataPanel.getAddBtn().addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				AddRoomAdditionDialog dialog = new AddRoomAdditionDialog();
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@SuppressWarnings("unchecked")
					@Override
					public void windowClosed(WindowEvent e) {
						if (!dialog.isOk())
							return;
						ControllerActionStatus status = ((CustomTableModel<RoomAddition>) dataPanel.getTable()
								.getModel()).add(new RoomAddition(dialog.getValue()));
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Room addition added successfully",
									"Success", JOptionPane.INFORMATION_MESSAGE);
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Room addition already exists",
									"Error", JOptionPane.ERROR_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(parent.getContentPane(), "An error occured", "Error",
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
		dataPanel.getEditBtn().setText("Edit Room Addition");
		dataPanel.getEditBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				CustomTableModel<RoomAddition> customTableModel = (CustomTableModel<RoomAddition>) dataPanel.getTable()
						.getModel();
				RoomAddition roomAddition = (RoomAddition) customTableModel.get(dataPanel.getTable().getSelectedRow());
				EditRoomAdditionDialog dialog = new EditRoomAdditionDialog(roomAddition.getName());
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@SuppressWarnings("rawtypes")
					@Override
					public void windowClosed(WindowEvent e) {
						if (!dialog.isOk())
							return;
						roomAddition.setName(dialog.getValue());
						ControllerActionStatus status = ((CustomTableModel) dataPanel.getTable().getModel())
								.edit(roomAddition);
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Room addition updated successfully",
									"Success", JOptionPane.INFORMATION_MESSAGE);
							break;
						case NO_RECORD:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Room addition not found", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Room addition already exists",
									"Error", JOptionPane.ERROR_MESSAGE);
						default:
							JOptionPane.showMessageDialog(parent.getContentPane(), "An error occured room addition tab edit", "Error",
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
		dataPanel.getDeleteBtn().setText("Delete Room Addition");
		dataPanel.getDeleteBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				CustomTableModel<RoomAddition> customTableModel = (CustomTableModel<RoomAddition>) dataPanel.getTable()
						.getModel();
				int res = JOptionPane.showConfirmDialog(parent.getContentPane(),
						"Are you sure you want to delete this room addition?", "Delete room addition",
						JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
				if (res != JOptionPane.YES_OPTION)
					return;
				ControllerActionStatus status = customTableModel.remove(dataPanel.getTable().getSelectedRow());
				switch (status) {
				case SUCCESS:
					JOptionPane.showMessageDialog(parent.getContentPane(), "Room addition deleted successfully",
							"Success", JOptionPane.INFORMATION_MESSAGE);
					break;
				case NO_RECORD:
					JOptionPane.showMessageDialog(parent.getContentPane(), "Room addition not found", "Error",
							JOptionPane.ERROR_MESSAGE);
					break;
				default:
					JOptionPane.showMessageDialog(parent.getContentPane(), "An error occured", "Error",
							JOptionPane.ERROR_MESSAGE);
				}
				dataPanel.getTable().updateUI();
			}
		});
	}

}
