package views.dialogs.reservations;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.FocusAdapter;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.time.LocalDate;
import java.time.ZoneId;
import java.util.ArrayList;

import javax.swing.Box;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSpinner;
import javax.swing.JTextField;
import javax.swing.ListCellRenderer;
import javax.swing.SpinnerNumberModel;
import javax.swing.SwingConstants;
import javax.swing.border.EmptyBorder;

import com.toedter.calendar.JDateChooser;

import controllers.ReservationController;
import controllers.RoomController;
import controllers.UserController;
import exceptions.PriceException;
import models.Guest;
import models.Model;
import models.Reservation;
import models.ReservationAddition;
import models.RoomAddition;
import models.RoomType;


public class AddReservationDialog extends JDialog {

	/**
	 * @return the ok
	 */
	public boolean isOk() {
		return ok;
	}

	/**
	 * @return the guest
	 */
	public Reservation getReservation() {
		return reservation;
	}

	private static final long serialVersionUID = 1L;
	private final JPanel contentPanel = new JPanel();
	private JLabel lblNewLabel_4;
	private JLabel lblNewLabel_5;
	private JLabel lblNewLabel_g;
	private JLabel lblNewLabel_2_1;
	private JTextField idTf;
	private JComboBox<RoomType> typeCb;
	private JComboBox<Guest> guestCb;
	private JTextField priceTf;
	private JDateChooser startDateCh;
	private JDateChooser endDateCh;
	private JSpinner numberOfGuestsSp;
	private ArrayList<JCheckBox> roomAdditionsCBs;
	private ArrayList<JCheckBox> reservationAdditionsCBs;
	
	private Reservation reservation;
	private boolean ok = false;

	/**
	 * Create the dialog.
	 */
	public AddReservationDialog(Guest guest) {
		reservation = new Reservation();
		setTitle("Add New Reservation");
		setModal(true);
		setIconImage(new ImageIcon("./assets/icons/reservations.png").getImage());
		setFont(new Font("Times New Roman", Font.PLAIN, 14));
		setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
		getContentPane().setBackground(new Color(73, 73, 73));
		setBackground(new Color(73, 73, 73));
		getContentPane().setForeground(new Color(255, 255, 255));
		setForeground(new Color(255, 255, 255));
		setBounds(100, 100, 600, 550);
		setLocationRelativeTo(null);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBackground(new Color(73, 73, 73));
		contentPanel.setForeground(new Color(255, 255, 255));
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		int y = 0;
		FocusAdapter focusAdapter = new FocusAdapter() {
			@Override
			public void focusLost(java.awt.event.FocusEvent e) {
				calculatePrice();
			}
		};
		ItemListener itemListener = new ItemListener() {
			
			@Override
			public void itemStateChanged(ItemEvent e) {
				calculatePrice();
			}
		};
		contentPanel.setLayout(new BorderLayout(0, 0));
		{
			JScrollPane scrollPane = new JScrollPane();
			scrollPane.getViewport().setBackground(new Color(73, 73, 73));
			contentPanel.add(scrollPane, BorderLayout.CENTER);
			{
				JPanel panel = new JPanel();
				panel.setBorder(new EmptyBorder(5, 5, 5, 5));
				panel.setBackground(new Color(73, 73, 73));
				scrollPane.setViewportView(panel);
				GridBagLayout gbl_panel = new GridBagLayout();
				gbl_panel.columnWidths = new int[] {0, 0};
				gbl_panel.rowHeights = new int[] {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
				gbl_panel.columnWeights = new double[]{0.0, 0.0, 1.0};
				gbl_panel.rowWeights = new double[]{0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, Double.MIN_VALUE};
				panel.setLayout(gbl_panel);
				{
					JLabel lblNewLabel = new JLabel("Add Reservation:");
					lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
					lblNewLabel.setForeground(new Color(255, 255, 255));
					lblNewLabel.setFont(new Font("Times New Roman", Font.PLAIN, 24));
					GridBagConstraints gbc_lblNewLabel = new GridBagConstraints();
					gbc_lblNewLabel.insets = new Insets(0, 0, 5, 0);
					gbc_lblNewLabel.gridwidth = 3;
					gbc_lblNewLabel.fill = GridBagConstraints.BOTH;
					gbc_lblNewLabel.gridx = 0;
					gbc_lblNewLabel.gridy = y++;
					panel.add(lblNewLabel, gbc_lblNewLabel);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(15);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 0;
					gbc_verticalStrut.gridy = y++;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					lblNewLabel_2_1 = new JLabel("Id:");
					lblNewLabel_2_1.setForeground(Color.WHITE);
					lblNewLabel_2_1.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_2_1 = new GridBagConstraints();
					gbc_lblNewLabel_2_1.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_2_1.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_2_1.gridx = 1;
					gbc_lblNewLabel_2_1.gridy = y;
					panel.add(lblNewLabel_2_1, gbc_lblNewLabel_2_1);
				}
				{
					idTf = new JTextField();
					lblNewLabel_2_1.setLabelFor(idTf);
					idTf.setEditable(false);
					idTf.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					idTf.setColumns(10);
					GridBagConstraints gbc_idTf = new GridBagConstraints();
					gbc_idTf.insets = new Insets(0, 0, 5, 0);
					gbc_idTf.fill = GridBagConstraints.HORIZONTAL;
					gbc_idTf.gridx = 2;
					gbc_idTf.gridy = y++;
					panel.add(idTf, gbc_idTf);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(5);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = y++;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					lblNewLabel_4 = new JLabel("Room Type:");
					lblNewLabel_4.setForeground(Color.WHITE);
					lblNewLabel_4.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_4 = new GridBagConstraints();
					gbc_lblNewLabel_4.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_4.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_4.gridx = 1;
					gbc_lblNewLabel_4.gridy = y;
					panel.add(lblNewLabel_4, gbc_lblNewLabel_4);
				}
				{
					typeCb = new JComboBox<RoomType>();
					lblNewLabel_4.setLabelFor(typeCb);
					typeCb.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_typeCb = new GridBagConstraints();
					gbc_typeCb.insets = new Insets(0, 0, 5, 0);
					gbc_typeCb.fill = GridBagConstraints.HORIZONTAL;
					gbc_typeCb.gridx = 2;
					gbc_typeCb.gridy = y++;
					panel.add(typeCb, gbc_typeCb);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(5);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = y++;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					lblNewLabel_4 = new JLabel("Number of Guests:");
					lblNewLabel_4.setForeground(Color.WHITE);
					lblNewLabel_4.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_4 = new GridBagConstraints();
					gbc_lblNewLabel_4.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_4.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_4.gridx = 1;
					gbc_lblNewLabel_4.gridy = y;
					panel.add(lblNewLabel_4, gbc_lblNewLabel_4);
				}
				{
					numberOfGuestsSp = new JSpinner();
					lblNewLabel_4.setLabelFor(typeCb);
					numberOfGuestsSp.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					numberOfGuestsSp.setModel(new SpinnerNumberModel(1, 1, null, 1));
					GridBagConstraints gbc_typeCb = new GridBagConstraints();
					gbc_typeCb.insets = new Insets(0, 0, 5, 0);
					gbc_typeCb.fill = GridBagConstraints.HORIZONTAL;
					gbc_typeCb.gridx = 2;
					gbc_typeCb.gridy = y++;
					panel.add(numberOfGuestsSp, gbc_typeCb);
				}
				{
					if (guest == null) {
						Component verticalStrut = Box.createVerticalStrut(5);
						GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
						gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
						gbc_verticalStrut.gridx = 1;
						gbc_verticalStrut.gridy = y++;
						panel.add(verticalStrut, gbc_verticalStrut);
					}
				}
				{
					if ( guest == null ) {
						lblNewLabel_g = new JLabel("Guest:");
						lblNewLabel_g.setForeground(Color.WHITE);
						lblNewLabel_g.setFont(new Font("Times New Roman", Font.PLAIN, 14));
						GridBagConstraints gbc_lblNewLabel_g = new GridBagConstraints();
						gbc_lblNewLabel_g.anchor = GridBagConstraints.WEST;
						gbc_lblNewLabel_g.insets = new Insets(0, 0, 5, 5);
						gbc_lblNewLabel_g.gridx = 1;
						gbc_lblNewLabel_g.gridy = y;
						panel.add(lblNewLabel_g, gbc_lblNewLabel_g);
					}
				}
				{
					if ( guest == null ) {
						guestCb = new JComboBox<Guest>();
						lblNewLabel_g.setLabelFor(guestCb);
						guestCb.setFont(new Font("Times New Roman", Font.PLAIN, 14));
						GridBagConstraints gbc_guestCb = new GridBagConstraints();
						gbc_guestCb.insets = new Insets(0, 0, 5, 0);
						gbc_guestCb.fill = GridBagConstraints.HORIZONTAL;
						gbc_guestCb.gridx = 2;
						gbc_guestCb.gridy = y++;
						panel.add(guestCb, gbc_guestCb);
					}
				}
				{
					Component verticalStrut = Box.createVerticalStrut(5);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = y++;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					lblNewLabel_5 = new JLabel("Start date:");
					lblNewLabel_5.setForeground(Color.WHITE);
					lblNewLabel_5.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_5 = new GridBagConstraints();
					gbc_lblNewLabel_5.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_5.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_5.gridx = 1;
					gbc_lblNewLabel_5.gridy = y;
					panel.add(lblNewLabel_5, gbc_lblNewLabel_5);
				}
				{
					startDateCh = new JDateChooser();
					GridBagConstraints gbc_startDateCh = new GridBagConstraints();
					gbc_startDateCh.anchor = GridBagConstraints.NORTH;
					gbc_startDateCh.insets = new Insets(0, 0, 5, 0);
					gbc_startDateCh.fill = GridBagConstraints.HORIZONTAL;
					gbc_startDateCh.gridx = 2;
					gbc_startDateCh.gridy = y++;
					panel.add(startDateCh, gbc_startDateCh);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(5);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = y++;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					JLabel lblNewLabel_5_1 = new JLabel("End date:");
					lblNewLabel_5_1.setForeground(Color.WHITE);
					lblNewLabel_5_1.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_5_1 = new GridBagConstraints();
					gbc_lblNewLabel_5_1.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_5_1.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_5_1.gridx = 1;
					gbc_lblNewLabel_5_1.gridy = y;
					panel.add(lblNewLabel_5_1, gbc_lblNewLabel_5_1);
				}
				{
					endDateCh = new JDateChooser();
					GridBagConstraints gbc_endDateCh = new GridBagConstraints();
					gbc_endDateCh.insets = new Insets(0, 0, 5, 0);
					gbc_endDateCh.fill = GridBagConstraints.BOTH;
					gbc_endDateCh.gridx = 2;
					gbc_endDateCh.gridy = y++;
					panel.add(endDateCh, gbc_endDateCh);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(5);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = y++;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					JLabel lblNewLabel_5_1 = new JLabel("Reservation additions:");
					lblNewLabel_5_1.setForeground(Color.WHITE);
					lblNewLabel_5_1.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_5_1 = new GridBagConstraints();
					gbc_lblNewLabel_5_1.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_5_1.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_5_1.gridx = 1;
					gbc_lblNewLabel_5_1.gridy = y;
					panel.add(lblNewLabel_5_1, gbc_lblNewLabel_5_1);
				}
				{
					reservationAdditionsCBs = new ArrayList<JCheckBox>();
					for (ReservationAddition ra : ReservationController.getReservationAdditions()) {
						JCheckBox cb = new JCheckBox(ra.getName());
						reservationAdditionsCBs.add(cb);
						cb.setFont(new Font("Times New Roman", Font.PLAIN, 14));
						GridBagConstraints constrains = new GridBagConstraints();
						constrains.fill = GridBagConstraints.HORIZONTAL;
						constrains.gridwidth = 1;
						constrains.insets = new Insets(0, 0, 5, 0);
						constrains.gridx = 2;
						constrains.gridy = y++;
						panel.add(cb, constrains);
					}
				}
				{
					Component verticalStrut = Box.createVerticalStrut(5);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = y++;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					JLabel lblNewLabel_5_1 = new JLabel("Room additions:");
					lblNewLabel_5_1.setForeground(Color.WHITE);
					lblNewLabel_5_1.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_5_1 = new GridBagConstraints();
					gbc_lblNewLabel_5_1.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_5_1.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_5_1.gridx = 1;
					gbc_lblNewLabel_5_1.gridy = y;
					panel.add(lblNewLabel_5_1, gbc_lblNewLabel_5_1);
				}
				{
					roomAdditionsCBs = new ArrayList<JCheckBox>();
					for (RoomAddition ra : RoomController.getRoomAdditions()) {
						JCheckBox cb = new JCheckBox(ra.getName());
						roomAdditionsCBs.add(cb);
						cb.setFont(new Font("Times New Roman", Font.PLAIN, 14));
						GridBagConstraints constrains = new GridBagConstraints();
						constrains.fill = GridBagConstraints.HORIZONTAL;
						constrains.gridwidth = 1;
						constrains.insets = new Insets(0, 0, 5, 0);
						constrains.gridx = 2;
						constrains.gridy = y++;
						panel.add(cb, constrains);
					}
				}
				{
					Component verticalStrut = Box.createVerticalStrut(5);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = y++;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					JLabel lblNewLabel_5_1 = new JLabel("Price:");
					lblNewLabel_5_1.setForeground(Color.WHITE);
					lblNewLabel_5_1.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_5_1 = new GridBagConstraints();
					gbc_lblNewLabel_5_1.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_5_1.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_5_1.gridx = 1;
					gbc_lblNewLabel_5_1.gridy = y;
					panel.add(lblNewLabel_5_1, gbc_lblNewLabel_5_1);
				}
				{
					priceTf = new JTextField();
					priceTf.setEditable(false);
					priceTf.setText("0");
					GridBagConstraints gbc_spinner = new GridBagConstraints();
					gbc_spinner.fill = GridBagConstraints.HORIZONTAL;
					gbc_spinner.insets = new Insets(0, 0, 5, 0);
					gbc_spinner.gridx = 2;
					gbc_spinner.gridy = y++;
					panel.add(priceTf, gbc_spinner);
				}
			}
		}
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setBackground(new Color(73, 73, 73));
			buttonPane.setForeground(new Color(255, 255, 255));
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				JButton okButton = new JButton("OK");
				okButton.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						
						String id = idTf.getText().trim();
						if (typeCb.getSelectedItem() == null) {
							JOptionPane.showMessageDialog(null, "Room type is required!", "Error", JOptionPane.ERROR_MESSAGE);
							return;
						}
						if (startDateCh.getDate() == null) {
							JOptionPane.showMessageDialog(null, "Start date is required!", "Error",
									JOptionPane.ERROR_MESSAGE);
							return;
						}
						if (endDateCh.getDate() == null) {
							JOptionPane.showMessageDialog(null, "End date is required!", "Error",
									JOptionPane.ERROR_MESSAGE);
							return;
						}
						LocalDate startDate = startDateCh.getDate().toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
						LocalDate endDate = endDateCh.getDate().toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
						if (startDate.isAfter(endDate)) {
							JOptionPane.showMessageDialog(null, "Start date must be before end date!", "Error",
									JOptionPane.ERROR_MESSAGE);
							return;
						}
						if (startDate.isBefore(LocalDate.now())) {
							JOptionPane.showMessageDialog(null, "Start date must be after today!", "Error",
									JOptionPane.ERROR_MESSAGE);
							return;
						}
						if (guest == null && guestCb.getSelectedItem() == null) {
							JOptionPane.showMessageDialog(null, "Guest is required!", "Error",
									JOptionPane.ERROR_MESSAGE);
							return;
						}
						if ((int) numberOfGuestsSp.getValue() < 1) {
							JOptionPane.showMessageDialog(null, "Number of guests must be at least 1!", "Error",
									JOptionPane.ERROR_MESSAGE);
							return;
						}
						reservation.setId(id);
						reservation.setRoomType((RoomType) typeCb.getSelectedItem());
						reservation.setStartDate(startDate);
						reservation.setEndDate(endDate);
						reservation.setNumberOfGuests((int) numberOfGuestsSp.getValue());
						ArrayList<RoomAddition> roomAdditions = new ArrayList<RoomAddition>();
						for (JCheckBox cb : roomAdditionsCBs) {
							if (cb.isSelected()) {
								roomAdditions.add(RoomController.getRoomAdditionByName(cb.getText()));
							}
						}
						reservation.setRoomAdditions(roomAdditions);
						ArrayList<ReservationAddition> reservationAdditions = new ArrayList<ReservationAddition>();
						for (JCheckBox cb : reservationAdditionsCBs) {
							if (cb.isSelected()) {
								reservationAdditions.add(ReservationController.getReservationAdditionByName(cb.getText()));
							}
						}
						reservation.setReservationAdditions(reservationAdditions);
						if (guest == null)
							reservation.setGuest((Guest)guestCb.getSelectedItem());
						else
							reservation.setGuest(guest);
						if (!ReservationController.isThereRoom(reservation)) {
							JOptionPane.showMessageDialog(null, "There is no available room for selected criteria!",
									"Error", JOptionPane.ERROR_MESSAGE);
							return;
						}
						ok = true;
						dispose();
					}
				});
				okButton.setFont(new Font("Times New Roman", Font.PLAIN, 14));
				okButton.setActionCommand("OK");
				buttonPane.add(okButton);
				getRootPane().setDefaultButton(okButton);
			}
			{
				JButton cancelButton = new JButton("Cancel");
				cancelButton.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						dispose();
					}
				});
				cancelButton.setFont(new Font("Times New Roman", Font.PLAIN, 14));
				cancelButton.setActionCommand("Cancel");
				buttonPane.add(cancelButton);
			}
		}
		
		typeCb.addItemListener(itemListener);
		startDateCh.addFocusListener(focusAdapter);
		endDateCh.addFocusListener(focusAdapter);
		roomAdditionsCBs.forEach(cb -> cb.addItemListener(itemListener));
		reservationAdditionsCBs.forEach(cb -> cb.addItemListener(itemListener));
		
		typeCb.setRenderer(new ListCellRenderer<RoomType>() {
            @Override
            public Component getListCellRendererComponent(JList<? extends RoomType> list, RoomType value, int index,
                    boolean isSelected, boolean cellHasFocus) {
                JLabel label = new JLabel(value.getName());
                label.setOpaque(true);
                label.setBackground(isSelected ? new Color(51, 153, 255) : new Color(73, 73, 73));
                label.setForeground(Color.WHITE);
                label.setFont(new Font("Times New Roman", Font.PLAIN, 14));
                return label;
            }
        });
		
		if (guest == null) {
			for (Guest g : UserController.getGuests()) {
				guestCb.addItem(g);
			}
			guestCb.setRenderer(new ListCellRenderer<Guest>() {
				@Override
				public Component getListCellRendererComponent(JList<? extends Guest> list, Guest value, int index,
						boolean isSelected, boolean cellHasFocus) {
					JLabel label = new JLabel(value.getName() + " " + value.getSurname());
					label.setOpaque(true);
					label.setBackground(isSelected ? new Color(51, 153, 255) : new Color(73, 73, 73));
					label.setForeground(Color.WHITE);
					label.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					return label;
				}
			});
		}
		RoomController.getRoomTypes().forEach(typeCb::addItem);
		
		idTf.setText(Model.generateId());
		
	}

	private void calculatePrice() {
		Reservation testReservation = new Reservation();
		testReservation.setRoomType((RoomType) typeCb.getSelectedItem());
		if (startDateCh.getDate() != null) {
			testReservation.setStartDate(startDateCh.getDate().toInstant().atZone(ZoneId.systemDefault()).toLocalDate());
		}
		if (endDateCh.getDate() != null) {
			testReservation.setEndDate(endDateCh.getDate().toInstant().atZone(ZoneId.systemDefault()).toLocalDate());
		}
		ArrayList<RoomAddition> roomAdditions = new ArrayList<RoomAddition>();
		for (JCheckBox cb : roomAdditionsCBs) {
			if (cb.isSelected()) {
				roomAdditions.add(RoomController.getRoomAdditionByName(cb.getText()));
			}
		}
		testReservation.setRoomAdditions(roomAdditions);
		ArrayList<ReservationAddition> reservationAdditions = new ArrayList<ReservationAddition>();
		for (JCheckBox cb : reservationAdditionsCBs) {
			if (cb.isSelected()) {
				reservationAdditions.add(ReservationController.getReservationAdditionByName(cb.getText()));
			}
		}
		testReservation.setReservationAdditions(reservationAdditions);
		try {
			testReservation.setPrice(ReservationController.calculateTotalPrice(testReservation));
			priceTf.setText(String.valueOf(testReservation.getPrice()));
        } catch (PriceException e) {
        	priceTf.setText(e.getMessage().split(":")[1].trim() + " is not available for the selected period");
		}
	}
}
