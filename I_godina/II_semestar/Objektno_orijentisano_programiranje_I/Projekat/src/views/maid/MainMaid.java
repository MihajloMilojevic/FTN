package views.maid;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Frame;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.table.TableColumnModel;

import app.AppState;
import controllers.ControllerActionStatus;
import controllers.RoomController;
import models.Maid;
import models.Room;
import utils.CustomTableModel;
import utils.Pair;
import utils.WindowUtils;
import views.components.DataPanel;

public class MainMaid extends JFrame {

	private static final long serialVersionUID = 165846546645L;
	private JPanel contentPane;
	private DataPanel<Room> dataPanel;
	private CustomTableModel<Room> model;

	// @SuppressWarnings("unchecked")
	public MainMaid() {
		setIconImage(WindowUtils.getIconImage());
		setTitle("MHotelify | Maid");
		setForeground(new Color(255, 255, 255));
		setBackground(new Color(73, 73, 73));
		setBounds(200, 100, 754, 586);
		setLocationRelativeTo(null);
		setExtendedState(Frame.MAXIMIZED_BOTH);
		setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);

		addMenu();

		contentPane = new JPanel();
		contentPane.setForeground(new Color(255, 255, 255));
		contentPane.setBackground(new Color(73, 73, 73));

		setContentPane(contentPane);
		contentPane.setLayout(new BorderLayout(0, 0));

		addRooms();

		addWindowListener(WindowUtils.getWindowClosing());
	}

	private void addMenu() {
		setJMenuBar(new MaidMenu(this));
	}

	private void addRooms() {

		ArrayList<Pair<String, String>> columns = new ArrayList<Pair<String, String>>();
		columns.add(new Pair<String, String>("ID", "id")); // 0
		columns.add(new Pair<String, String>("Number", "number")); // 1
		columns.add(new Pair<String, String>("Type", "type")); // 2
		
		model = new CustomTableModel<Room>(null, columns, new CustomTableModel.TableDataManiplations<Room>() {

			@Override
			public ArrayList<Room> getData() {
				return RoomController.getRoomsForMaid((Maid)AppState.getInstance().getUser());
			}

			@Override
			public ControllerActionStatus edit(Room model) {
				throw new UnsupportedOperationException();
			}

			@Override
			public ControllerActionStatus remove(Room model) {
				throw new UnsupportedOperationException();
			}

			@Override
			public ControllerActionStatus add(Room model) {
				throw new UnsupportedOperationException();
			}

		}, new Room()) {

			private static final long serialVersionUID = 9169960940041846844L;

			@Override
			public Object getValueAt(int rowIndex, int columnIndex) {
				if (columns.get(columnIndex).getSecond().equals("type")) {
					if (((Room) data.get(rowIndex)).getType() == null)
						return "";
					return ((Room) data.get(rowIndex)).getType().getName();
				}
				return super.getValueAt(rowIndex, columnIndex);
			}

			@Override
			public Class<?> getColumnClass(int columnIndex) {
				if (columns.get(columnIndex).getSecond().equals("type")) {
					return String.class;
				}
				return super.getColumnClass(columnIndex);
			}
		};
		
		dataPanel = new DataPanel<Room>(model);
		
		TableColumnModel columnModel = dataPanel.getTable().getColumnModel();
		columnModel.getColumn(0).setMinWidth(150);
		columnModel.getColumn(1).setMinWidth(50);
		columnModel.getColumn(2).setMinWidth(150);
		
		dataPanel.getRefreshBtn().addActionListener(e -> {
			model.refresh();
			dataPanel.getTable().updateUI();
		});
		dataPanel.getAddBtn().setVisible(false);
		dataPanel.getEditBtn().setVisible(false);
		dataPanel.getDeleteBtn().setVisible(false);
		
		dataPanel.addButton("Mark as cleaned", "./assets/icons/clean.png", new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				Room room = model.get(dataPanel.getTable().getSelectedRow());
				int res = JOptionPane.showConfirmDialog(null, "Are you sure you want to mark room " + room.getNumber() + " as cleaned?", "Mark as cleaned", JOptionPane.YES_NO_OPTION);
				if (res != JOptionPane.YES_OPTION)
					return;
				ControllerActionStatus status = RoomController.markRoomAsCleaned(room);
				switch (status) {
				case SUCCESS:
					JOptionPane.showMessageDialog(null, "Room marked as cleaned.", "Success",
							JOptionPane.INFORMATION_MESSAGE);
					break;
				case NO_RECORD:
					JOptionPane.showMessageDialog(null, "Room not found.", "Error", JOptionPane.ERROR_MESSAGE);
					break;
				default:
					JOptionPane.showMessageDialog(null, "An error occurred.", "Error", JOptionPane.ERROR_MESSAGE);
					break;
				}
				model.refresh();
				dataPanel.getTable().updateUI();
			}
		}, true);

		contentPane.add(dataPanel, BorderLayout.CENTER);
	}
}
