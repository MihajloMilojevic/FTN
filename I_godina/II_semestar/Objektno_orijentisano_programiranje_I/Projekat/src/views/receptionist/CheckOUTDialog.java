package views.receptionist;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.table.TableColumnModel;

import controllers.ControllerActionStatus;
import controllers.ReservationController;
import models.Guest;
import models.Reservation;
import utils.CustomTableModel;
import utils.Pair;
import utils.WindowUtils;
import views.components.DataPanel;

public class CheckOUTDialog extends JDialog {

	private static final long serialVersionUID = 1L;
	private final JPanel contentPanel = new JPanel();
	private CustomTableModel<Reservation> model;
	private DataPanel<Reservation> dataPanel;

	/**
	 * Create the dialog.
	 */
	public CheckOUTDialog() {
		setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
		setTitle("Check OUT");
		setIconImage(new ImageIcon("./assets/icons/check_out.png").getImage());
		setModal(true);
		setFont(new Font("Times New Roman", Font.PLAIN, 14));
		setBounds(100, 100, (int) (WindowUtils.getToolkit().getScreenSize().getWidth() * 0.8),
				(int) (WindowUtils.getToolkit().getScreenSize().getHeight() * 0.8));
		setLocationRelativeTo(null);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBackground(new Color(73, 73, 73));
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		contentPanel.setLayout(new BorderLayout(0, 0));
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setBackground(new Color(73, 73, 73));
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				JButton okButton = new JButton("OK");
				okButton.setFont(new Font("Times New Roman", Font.PLAIN, 14));
				okButton.setActionCommand("OK");
				okButton.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						dispose();
					}
				});
				buttonPane.add(okButton);
				getRootPane().setDefaultButton(okButton);
			}
		}
		addReservations();
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
				return ReservationController.getCheckOutReservations();
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
		dataPanel.getAddBtn().setVisible(false);
		dataPanel.getEditBtn().setVisible(false);
		dataPanel.getDeleteBtn().setVisible(false);

		dataPanel.addButton("Check Out Reservation", "./assets/icons/check_out.png", new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				Reservation reservation = model.get(dataPanel.getTable().getSelectedRow());
				if (reservation == null) {
					JOptionPane.showMessageDialog(dataPanel, "Please select a reservation", "Error",
							JOptionPane.ERROR_MESSAGE);
					return;
				}
				int res = JOptionPane.showConfirmDialog(dataPanel,
						"Are you sure you want to check out this reservation?", "Check out", JOptionPane.YES_NO_OPTION);
				if (res != JOptionPane.YES_OPTION)
					return; 
				ControllerActionStatus status = ReservationController.checkOut(reservation);
				switch (status) {
				case SUCCESS:
					JOptionPane.showMessageDialog(dataPanel, "Reservation checked out successfully", "Success",
							JOptionPane.INFORMATION_MESSAGE);
					dispose();
					break;
				case NO_RECORD:
					JOptionPane.showMessageDialog(dataPanel, "Reservation not found", "Error",
							JOptionPane.ERROR_MESSAGE);
					break;
				default:
					JOptionPane.showMessageDialog(dataPanel, "An error occured", "Error", JOptionPane.ERROR_MESSAGE);
					break;
				}

				model.refresh();
				dataPanel.getTable().updateUI();
			}
		}, true);

		contentPanel.add(dataPanel, BorderLayout.CENTER);
	}

}
