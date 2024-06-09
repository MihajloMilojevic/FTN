package views.receptionist;

import java.awt.Color;
import java.awt.Font;
import java.time.LocalDate;
import java.util.ArrayList;

import javax.swing.JDialog;
import javax.swing.table.TableColumnModel;

import controllers.ControllerActionStatus;
import controllers.RoomController;
import models.Guest;
import models.Reservation;
import models.Room;
import models.RoomType;
import models.enums.RoomStatus;
import utils.CustomTableModel;
import utils.Pair;
import utils.WindowUtils;
import views.components.DataPanel;

public class RoomsDialog extends JDialog {

	private static final long serialVersionUID = -8428612301527655534L;

	public RoomsDialog() {
		setTitle("Rooms");
		setFont(new Font("Times New Roman", Font.PLAIN, 14));
		setModal(true);
		setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
		setBounds(100, 100, (int) (WindowUtils.getToolkit().getScreenSize().getWidth() * 0.8),
				(int) (WindowUtils.getToolkit().getScreenSize().getHeight() * 0.8));
		setLocationRelativeTo(null);
		setIconImage(WindowUtils.getIconImage());

		setForeground(new Color(255, 255, 255));
		setBackground(new Color(73, 73, 73));

		ArrayList<Pair<String, String>> columns = new ArrayList<Pair<String, String>>();
		columns.add(new Pair<String, String>("ID", "id"));
		columns.add(new Pair<String, String>("Number", "number"));
		columns.add(new Pair<String, String>("Type", "type"));
		columns.add(new Pair<String, String>("Status", "status"));
		columns.add(new Pair<String, String>("Occupied Until", "endDate"));
		columns.add(new Pair<String, String>("Guest", "guest"));

		CustomTableModel<ReceptioniosRoomView> model = new CustomTableModel<ReceptioniosRoomView>(null, columns,
				new CustomTableModel.TableDataManiplations<ReceptioniosRoomView>() {

					@Override
					public ArrayList<ReceptioniosRoomView> getData() {
						ArrayList<ReceptioniosRoomView> rooms = new ArrayList<ReceptioniosRoomView>();
						ArrayList<Pair<Room, Reservation>> roomReservations = RoomController.getReceptionistRooms();
						for (Pair<Room, Reservation> pair : roomReservations) {
							rooms.add(new ReceptioniosRoomView(pair.getFirst(), pair.getSecond()));
						}
						return rooms;
					}

					@Override
					public ControllerActionStatus edit(ReceptioniosRoomView model) {
						throw new UnsupportedOperationException();
					}

					@Override
					public ControllerActionStatus remove(ReceptioniosRoomView model) {
						throw new UnsupportedOperationException();
					}

					@Override
					public ControllerActionStatus add(ReceptioniosRoomView model) {
						throw new UnsupportedOperationException();
					}

				}, new ReceptioniosRoomView(new Room(), null)) {
			private static final long serialVersionUID = -4762274401058873540L;

			@Override
			public String getValueAt(int row, int column) {
				ReceptioniosRoomView room = data.get(row);
				switch (column) {
				case 0:
					return room.getId();
				case 1:
					return Integer.toString(room.getNumber());
				case 2:
					return getStringValue(room.getType());
				case 3:
					return getStringValue(room.getStatus());
				case 4:
					return getStringValue(room.getEndDate());
				case 5:
					return getStringValue(room.getGuest());
				default:
					return "";
				}
			}
			@Override
			public Class<?> getColumnClass(int columnIndex) {
				return String.class;
			}
		};
		DataPanel<ReceptioniosRoomView> dataPanel = new DataPanel<ReceptioniosRoomView>(model);
		add(dataPanel);
		TableColumnModel columnModel = dataPanel.getTable().getColumnModel();
		columnModel.getColumn(0).setMinWidth(150);
		columnModel.getColumn(1).setMinWidth(150);
		columnModel.getColumn(2).setMinWidth(150);
		columnModel.getColumn(3).setMinWidth(150);
		columnModel.getColumn(4).setMinWidth(150);
		columnModel.getColumn(5).setMinWidth(250);

		dataPanel.getRefreshBtn().setVisible(false);
		dataPanel.getAddBtn().setVisible(false);
		dataPanel.getEditBtn().setVisible(false);
		dataPanel.getDeleteBtn().setVisible(false);
	}

	private class ReceptioniosRoomView extends Room {
		Guest guest;
		LocalDate endDate;

		public ReceptioniosRoomView(Room room, Reservation reservation) {
			super(room.getId(), room.getNumber(), room.getType(), room.getStatus(), room.getRoomAdditions());
			if (reservation != null) {
				this.guest = reservation.getGuest();
				this.endDate = reservation.getEndDate();
			}
		}

		/**
		 * @return the guest
		 */
		public Guest getGuest() {
			return guest;
		}

		/**
		 * @return the endDate
		 */
		public LocalDate getEndDate() {
			return endDate;
		}

	};

	private String getStringValue(Object obj) {
		if (obj == null) {
			return "";
		}
		if (obj instanceof RoomType) {
			return ((RoomType) obj).getName();
		}
		if (obj instanceof Integer) {
			return Integer.toString((Integer) obj);
		}
		if (obj instanceof RoomStatus) {
			return ((RoomStatus) obj).toString();
		}
		if (obj instanceof LocalDate) {
			return String.format("%d.%d.%d.", ((LocalDate) obj).getDayOfMonth(), ((LocalDate) obj).getMonthValue(),
					((LocalDate) obj).getYear());
		}
		if (obj instanceof Guest) {
			return ((Guest) obj).getName() + " " + ((Guest) obj).getSurname();
		}
		return obj.toString();
	}
}
