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
import models.Maid;
import models.Room;
import utils.CustomTableModel;
import utils.Pair;
import views.components.DataPanel;
import views.components.Tab;
import views.dialogs.rooms.AddRoomDialog;
import views.dialogs.rooms.EditRoomDialog;

public class RoomsTab extends Tab<Room> {

	public RoomsTab(JFrame parent) {
		super(parent);
	}

	@Override
	protected void addColumns() {
		columns.add(new Pair<String, String>("ID", "id")); // 0
		columns.add(new Pair<String, String>("Number", "number")); // 1
		columns.add(new Pair<String, String>("Type", "type")); // 2
		columns.add(new Pair<String, String>("Status", "status")); // 3
		columns.add(new Pair<String, String>("Additions", "roomAdditions")); // 4
		columns.add(new Pair<String, String>("Maid", "maid")); // 5
	}

	@Override
	protected void addModel() {
		model = new CustomTableModel<Room>(this, columns, new CustomTableModel.TableDataManiplations<Room>() {

			@Override
			public ArrayList<Room> getData() {
				return RoomController.getRooms();
			}

			@Override
			public ControllerActionStatus edit(Room model) {
				return RoomController.updateRoom(model);
			}

			@Override
			public ControllerActionStatus remove(Room model) {
				return RoomController.deleteRoom(model);
			}

			@Override
			public ControllerActionStatus add(Room model) {
				return RoomController.addRoom(model);
			}

		}, new Room()) {

			private static final long serialVersionUID = -4762274401058873540L;

			@Override
			public Object getValueAt(int rowIndex, int columnIndex) {
				if (columns.get(columnIndex).getSecond().equals("roomAdditions")) {
					return String.join(", ", ((Room) data.get(rowIndex)).getRoomAdditions().stream()
							.map(ra -> ra.getName()).toArray(String[]::new));
				}
				if (columns.get(columnIndex).getSecond().equals("type")) {
					if (((Room) data.get(rowIndex)).getType() == null)
						return "";
					return ((Room) data.get(rowIndex)).getType().getName();
				}
				if (columns.get(columnIndex).getSecond().equals("maid")) {
					if (((Room) data.get(rowIndex)).getMaid() == null)
						return "";
					Maid maid = ((Room) data.get(rowIndex)).getMaid();
					return maid.getName() + " " + maid.getSurname();
				}
				return super.getValueAt(rowIndex, columnIndex);
			}

			@Override
			public Class<?> getColumnClass(int columnIndex) {
				if (columns.get(columnIndex).getSecond().equals("roomAdditions")) {
					return String.class;
				}
				if (columns.get(columnIndex).getSecond().equals("type")) {
					return String.class;
				}
				if (columns.get(columnIndex).getSecond().equals("maid")) {
					return String.class;
				}
				return super.getColumnClass(columnIndex);
			}
		};
	}

	@Override
	protected void addDataPanel() {
		dataPanel = new DataPanel<Room>(model);
	}

	@Override
	protected void setColumnsSize() {
		TableColumnModel columnModel = dataPanel.getTable().getColumnModel();
		columnModel.getColumn(0).setMinWidth(150);
		columnModel.getColumn(1).setMinWidth(50);
		columnModel.getColumn(2).setMinWidth(150);
		columnModel.getColumn(3).setMinWidth(75);
		columnModel.getColumn(4).setMinWidth(350);
		columnModel.getColumn(5).setMinWidth(200);
	}

	@Override
	protected void addRefreshButtonAction() {
		dataPanel.getRefreshBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				((CustomTableModel<Room>) dataPanel.getTable().getModel()).refresh();
				dataPanel.getTable().updateUI();
			}
		});
	}

	@Override
	protected void addAddButtonAction() {
		dataPanel.getAddBtn().setText("Add Room");
		dataPanel.getAddBtn().addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				AddRoomDialog dialog = new AddRoomDialog();
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@SuppressWarnings("unchecked")
					@Override
					public void windowClosed(WindowEvent e) {
						if (!dialog.isOk())
							return;
						ControllerActionStatus status = ((CustomTableModel<Room>) dataPanel.getTable().getModel())
								.add(dialog.getRoom());
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(parent, "Room added successfully", "Success",
									JOptionPane.INFORMATION_MESSAGE);
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(parent, "Room with this number already exists", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(parent, "An error occured", "Error",
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
		dataPanel.getEditBtn().setText("Edit Room");
		dataPanel.getEditBtn().addActionListener(new ActionListener() {
			// @SuppressWarnings("unchecked")
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				CustomTableModel<Room> customTableModel = (CustomTableModel<Room>) dataPanel.getTable().getModel();
				Room room = (Room) customTableModel.get(dataPanel.getTable().getSelectedRow());
				EditRoomDialog dialog = new EditRoomDialog(room);
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@SuppressWarnings("rawtypes")
					@Override
					public void windowClosed(WindowEvent e) {
						if (!dialog.isOk())
							return;
						ControllerActionStatus status = ((CustomTableModel) dataPanel.getTable().getModel()).edit(room);
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(parent, "Room edited successfully", "Success",
									JOptionPane.INFORMATION_MESSAGE);
							break;
						case NO_RECORD:
							JOptionPane.showMessageDialog(parent, "Room not found", "Error", JOptionPane.ERROR_MESSAGE);
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(parent, "Room with this number already exists", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(parent, "An error occured", "Error",
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
	protected void addRemoveButtonAction() {
		dataPanel.getDeleteBtn().setText("Delete Room");
		dataPanel.getDeleteBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				CustomTableModel<Room> customTableModel = (CustomTableModel<Room>) dataPanel.getTable().getModel();
				int res = JOptionPane.showConfirmDialog(parent.getContentPane(),
						"Are you sure you want to delete this room?", "Delete room", JOptionPane.YES_NO_OPTION,
						JOptionPane.QUESTION_MESSAGE);
				if (res != JOptionPane.YES_OPTION)
					return;
				ControllerActionStatus status = customTableModel.remove(dataPanel.getTable().getSelectedRow());
				switch (status) {
				case SUCCESS:
					JOptionPane.showMessageDialog(parent, "Room deleted successfully", "Success",
							JOptionPane.INFORMATION_MESSAGE);
					break;
				case NO_RECORD:
					JOptionPane.showMessageDialog(parent, "Room not found", "Error", JOptionPane.ERROR_MESSAGE);
					break;
				default:
					JOptionPane.showMessageDialog(parent, "An error occured", "Error", JOptionPane.ERROR_MESSAGE);
					break;
				}
				dataPanel.getTable().updateUI();
			}
		});
	}

	@Override
	protected void addNewButton() {
		dataPanel.addButton("View Cleaning Logs", "./assets/icons/clean.png", new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Room room = (Room) model.get(dataPanel.getTable().getSelectedRow());
				CleaningLogsDialog dialog = new CleaningLogsDialog(room);
				dialog.setVisible(true);
			}
		}, true);
	}
}
