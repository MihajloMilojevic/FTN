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
import models.RoomType;
import utils.CustomTableModel;
import utils.CustomTableModelWithInitialPrice;
import utils.Pair;
import views.components.DataPanel;
import views.components.Tab;
import views.dialogs.room_types.AddRoomTypesDialog;
import views.dialogs.room_types.EditRoomTypeDialog;

public class RoomTypesTab extends Tab<RoomType> {

	public RoomTypesTab(JFrame parent) {
		super(parent);
	}

	@Override
	protected void addColumns() {
		columns.add(new Pair<String, String>("ID", "id")); // 0
		columns.add(new Pair<String, String>("Name", "name")); // 1
		columns.add(new Pair<String, String>("Max Capacity", "maxCapacity")); // 2
	}
	
	@Override
	protected void addModel() {
		model = new CustomTableModelWithInitialPrice<RoomType>(this, columns, new CustomTableModelWithInitialPrice.TableDataManiplationsWithPrice<RoomType>() {

			@Override
			public ArrayList<RoomType> getData() {
				return RoomController.getRoomTypes();
			}

			@Override
			public ControllerActionStatus edit(RoomType model) {
				return RoomController.updateRoomType(model);
			}

			@Override
			public ControllerActionStatus remove(RoomType model) {
				return RoomController.deleteRoomType(model);
			}

			@Override
			public ControllerActionStatus add(RoomType model) {
				throw new UnsupportedOperationException();
			}
			
			public ControllerActionStatus add(RoomType model, double price) {
				return RoomController.addRoomType(model, price);
			}

		}, new RoomType());
	}

	@Override
	protected void addDataPanel() {
		dataPanel = new DataPanel<RoomType>(model);
	}

	@Override
	protected void setColumnsSize() {
		TableColumnModel columnModel = dataPanel.getTable().getColumnModel();
		columnModel.getColumn(0).setMinWidth(150);
		columnModel.getColumn(1).setMinWidth(500);
		columnModel.getColumn(2).setMinWidth(150);
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
		dataPanel.getAddBtn().setText("Add Room Type");
		dataPanel.getAddBtn().addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				AddRoomTypesDialog dialog = new AddRoomTypesDialog();
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@Override
					public void windowClosed(WindowEvent e) {
						if (!dialog.isOk())
							return;
						ControllerActionStatus status = ((CustomTableModelWithInitialPrice<RoomType>)model).add(dialog.getRoomType(), dialog.getInitialPrice());
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(null, "Room Type added successfully");
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(null, "Room Type already exists");
							break;
						default:
							JOptionPane.showMessageDialog(null, "Error adding Room Type");

						}
						dataPanel.getTable().updateUI();
					}
				});

			}
		});
	}

	@Override
	protected void addEditButtonAction() {
		dataPanel.getEditBtn().setText("Edit Room Type");
		dataPanel.getEditBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				CustomTableModel<RoomType> customTableModel = (CustomTableModel<RoomType>) dataPanel.getTable()
						.getModel();
				RoomType roomType = (RoomType) customTableModel.get(dataPanel.getTable().getSelectedRow());
				EditRoomTypeDialog dialog = new EditRoomTypeDialog(roomType);
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@SuppressWarnings("rawtypes")
					@Override
					public void windowClosed(WindowEvent e) {
						if (!dialog.isOk())
							return;
						ControllerActionStatus status = ((CustomTableModel) dataPanel.getTable().getModel())
								.edit(roomType);
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(null, "Room Type edited successfully");
							break;
						case NO_RECORD:
							JOptionPane.showMessageDialog(null, "Room Type does not exist");
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(null, "Room Type already exists");
							break;
						default:
							JOptionPane.showMessageDialog(null, "Error editing Room Type");
						}
						dataPanel.getTable().updateUI();
					}
				});
			}
		});
	}

	@Override
	protected void addRemoveButtonAction() {
		dataPanel.getDeleteBtn().setText("Delete Room Type");
		dataPanel.getDeleteBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				CustomTableModel<RoomType> customTableModel = (CustomTableModel<RoomType>) dataPanel.getTable()
						.getModel();
				int res = JOptionPane.showConfirmDialog(parent.getContentPane(),
						"Are you sure you want to delete this room type?", "Delete room type",
						JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
				if (res != JOptionPane.YES_OPTION)
					return;
				ControllerActionStatus status = customTableModel.remove(dataPanel.getTable().getSelectedRow());
				switch (status) {
				case SUCCESS:
					JOptionPane.showMessageDialog(parent.getContentPane(), "Room Type deleted successfully");
					break;
				case NO_RECORD:
					JOptionPane.showMessageDialog(parent.getContentPane(), "Room Type does not exist");
					break;
				case IN_USE:
					JOptionPane.showMessageDialog(parent.getContentPane(), "Room Type is in use");
					break;
				default:
					JOptionPane.showMessageDialog(parent.getContentPane(), "Error deleting Room Type");
				}
				dataPanel.getTable().updateUI();
			}
		});
	}

}
