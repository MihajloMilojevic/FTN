package views.receptionist;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.util.ArrayList;

import javax.swing.Box;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JScrollPane;
import javax.swing.SwingConstants;

import models.Room;
import utils.WindowUtils;

public class SelectRoomDialog extends JDialog {

	public Room getSelectedRoom() {
		return selectedRoom;
	}

	public boolean isOk() {
		return ok;
	}
	
	private static final long serialVersionUID = 1L;
	private ArrayList<JRadioButton> roomTypesRB;
	private ButtonGroup buttonGroup;
	private Room selectedRoom = null;
	private boolean ok = false;

	/**
	 * Create the dialog.
	 */
	public SelectRoomDialog(ArrayList<Room> availableRooms) {
		setTitle("Room selection dialog");
		setFont(new Font("Times New Roman", Font.PLAIN, 14));
		setModal(true);
		setIconImage(WindowUtils.getIconImage());
		setBounds(100, 100, 450, 300);
		setLocationRelativeTo(null);
		int y = 0;
		roomTypesRB = new ArrayList<>();
		buttonGroup = new ButtonGroup();
		getContentPane().setLayout(new BorderLayout());
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setForeground(new Color(255, 255, 255));
			buttonPane.setBackground(new Color(73, 73, 73));
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				JButton okButton = new JButton("OK");
				okButton.setFont(new Font("Times New Roman", Font.PLAIN, 14));
				okButton.setActionCommand("OK");
				buttonPane.add(okButton);
				okButton.addActionListener(e -> {
					for (JRadioButton r : roomTypesRB) {
						if (r.isSelected()) {
							selectedRoom = availableRooms.get(roomTypesRB.indexOf(r));
							ok = true;
							dispose();
							return;
						}
					}
					JOptionPane.showMessageDialog(this, "Please select a room", "Error", JOptionPane.ERROR_MESSAGE);
				});
				getRootPane().setDefaultButton(okButton);
			}
			{
				JButton cancelButton = new JButton("Cancel");
				cancelButton.setFont(new Font("Times New Roman", Font.PLAIN, 14));
				cancelButton.setActionCommand("Cancel");
				cancelButton.addActionListener(e -> {
					ok = false;
					dispose();
				});
				buttonPane.add(cancelButton);
			}
		}
		{
			JScrollPane scrollPane = new JScrollPane();
			getContentPane().add(scrollPane, BorderLayout.CENTER);
			{
				JPanel panel = new JPanel();
				panel.setForeground(new Color(255, 255, 255));
				panel.setBackground(new Color(73, 73, 73));
				scrollPane.setViewportView(panel);
				GridBagLayout gbl_panel = new GridBagLayout();
				gbl_panel.columnWidths = new int[]{0, 0};
				gbl_panel.rowHeights = new int[]{0, 0, 0};
				gbl_panel.columnWeights = new double[]{1.0, Double.MIN_VALUE};
				gbl_panel.rowWeights = new double[]{0.0, 0.0, Double.MIN_VALUE};
				panel.setLayout(gbl_panel);
				{
					JLabel lblNewLabel = new JLabel("Select A Room");
					lblNewLabel.setForeground(new Color(255, 255, 255));
					lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
					lblNewLabel.setFont(new Font("Times New Roman", Font.PLAIN, 24));
					GridBagConstraints gbc_lblNewLabel = new GridBagConstraints();
					gbc_lblNewLabel.insets = new Insets(0, 0, 5, 0);
					gbc_lblNewLabel.gridx = 0;
					gbc_lblNewLabel.gridy = y++;
					panel.add(lblNewLabel, gbc_lblNewLabel);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(25);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.gridx = 0;
					gbc_verticalStrut.gridy = y++;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					for (Room room : availableRooms) {
						JRadioButton rdbtnNewRadioButton = new JRadioButton(String.format("Room %d", room.getNumber()) + " - " + room.getStatus().toString());
						rdbtnNewRadioButton.setFont(new Font("Times New Roman", Font.PLAIN, 14));
						rdbtnNewRadioButton.setForeground(Color.WHITE);
						rdbtnNewRadioButton.setBackground(new Color(73, 73, 73));
						GridBagConstraints gbc_rdbtnNewRadioButton = new GridBagConstraints();
						gbc_rdbtnNewRadioButton.insets = new Insets(0, 0, 5, 0);
						gbc_rdbtnNewRadioButton.gridx = 0;
						gbc_rdbtnNewRadioButton.gridy = y++;
						panel.add(rdbtnNewRadioButton, gbc_rdbtnNewRadioButton);
						buttonGroup.add(rdbtnNewRadioButton);
						roomTypesRB.add(rdbtnNewRadioButton);
					}
				}
			}
		}
	}

}
