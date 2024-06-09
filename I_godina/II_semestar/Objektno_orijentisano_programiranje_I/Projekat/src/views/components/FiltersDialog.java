package views.components;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemListener;
import java.util.ArrayList;

import javax.swing.Box;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSpinner;
import javax.swing.SpinnerNumberModel;
import javax.swing.SwingConstants;
import javax.swing.border.EmptyBorder;

import controllers.ReservationController;
import controllers.RoomController;
import models.ReservationAddition;
import models.RoomAddition;
import models.RoomType;
import models.enums.ReservationStatus;
import utils.Filters;
import utils.Pair;

public class FiltersDialog extends JDialog {

	private static final long serialVersionUID = 1L;
	private JSpinner minPriceSp;
	private JSpinner maxPriceSp;
	private JCheckBox enablePriceCb;
	private ArrayList<Pair<JCheckBox, ReservationStatus>> statuses;
	private ArrayList<Pair<JCheckBox, RoomType>> roomTypes;
	private ArrayList<Pair<JCheckBox, ReservationAddition>> reservationAdditions;
	private ArrayList<Pair<JCheckBox, RoomAddition>> roomAdditions;

	public FiltersDialog() {
		setResizable(true);
		setModal(true);
		setTitle("Filter Reservations");
		setIconImage(Toolkit.getDefaultToolkit()
				.getImage("C:\\MIHAJLO_MILOJEVIC\\PROJEKTI\\MHotelify_OOP1\\assets\\icons\\filters.png"));
		setFont(new Font("Times New Roman", Font.PLAIN, 14));
		setBounds(100, 100, 498, 412);
		setLocationRelativeTo(null);
		setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
		statuses = new ArrayList<>();
		roomTypes = new ArrayList<>();
		reservationAdditions = new ArrayList<>();
		roomAdditions = new ArrayList<>();

		ItemListener priceListener = new ItemListener() {
			@Override
			public void itemStateChanged(java.awt.event.ItemEvent e) {
				minPriceSp.setEnabled(enablePriceCb.isSelected());
				maxPriceSp.setEnabled(enablePriceCb.isSelected());
			}
		};

		int y = 0;
		getContentPane().setLayout(new BorderLayout());
		{
			JScrollPane scrollPane = new JScrollPane();
			getContentPane().add(scrollPane, BorderLayout.CENTER);
			{
				JPanel contentPanel = new JPanel();
				contentPanel.setForeground(Color.WHITE);
				contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
				contentPanel.setBackground(new Color(73, 73, 73));
				scrollPane.setViewportView(contentPanel);
				GridBagLayout gbl_contentPanel = new GridBagLayout();
				gbl_contentPanel.columnWidths = new int[] { 0, 0, 0 };
				gbl_contentPanel.rowHeights = new int[] { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
				gbl_contentPanel.columnWeights = new double[] { 0.0, 1.0, Double.MIN_VALUE };
				gbl_contentPanel.rowWeights = new double[] { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
						0.0, 0.0, 0.0, Double.MIN_VALUE };
				contentPanel.setLayout(gbl_contentPanel);
				{
					JLabel lblNewLabel = new JLabel("Filter Reservations");
					lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
					lblNewLabel.setForeground(Color.WHITE);
					lblNewLabel.setFont(new Font("Times New Roman", Font.PLAIN, 18));
					GridBagConstraints gbc_lblNewLabel = new GridBagConstraints();
					gbc_lblNewLabel.fill = GridBagConstraints.HORIZONTAL;
					gbc_lblNewLabel.gridwidth = 2;
					gbc_lblNewLabel.insets = new Insets(0, 0, 5, 0);
					gbc_lblNewLabel.gridx = 0;
					gbc_lblNewLabel.gridy = y++;
					contentPanel.add(lblNewLabel, gbc_lblNewLabel);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(25);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 0;
					gbc_verticalStrut.gridy = y++;
					contentPanel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					JLabel lblReservationStatus = new JLabel("Reservation status:");
					lblReservationStatus.setHorizontalAlignment(SwingConstants.LEFT);
					lblReservationStatus.setForeground(Color.WHITE);
					lblReservationStatus.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblReservationStatus = new GridBagConstraints();
					gbc_lblReservationStatus.anchor = GridBagConstraints.WEST;
					gbc_lblReservationStatus.insets = new Insets(0, 0, 5, 5);
					gbc_lblReservationStatus.gridx = 0;
					gbc_lblReservationStatus.gridy = y;
					contentPanel.add(lblReservationStatus, gbc_lblReservationStatus);
				}
				{
					for (ReservationStatus rs : ReservationStatus.values()) {
						JCheckBox cb = new JCheckBox(rs.toString());
						cb.setForeground(Color.WHITE);
						cb.setFont(new Font("Times New Roman", Font.PLAIN, 14));
						cb.setBackground(new Color(73, 73, 73));
						cb.setSelected(Filters.getStatuses().contains(rs));
						statuses.add(new Pair<>(cb, rs));
						GridBagConstraints gbc_cb = new GridBagConstraints();
						gbc_cb.fill = GridBagConstraints.HORIZONTAL;
						gbc_cb.insets = new Insets(0, 0, 5, 0);
						gbc_cb.gridx = 1;
						gbc_cb.gridy = y++;
						contentPanel.add(cb, gbc_cb);
					}
				}
				{
					Component verticalStrut = Box.createVerticalStrut(10);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 0;
					gbc_verticalStrut.gridy = y++;
					contentPanel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					JLabel lblRoomTypes = new JLabel("Room Types:");
					lblRoomTypes.setHorizontalAlignment(SwingConstants.LEFT);
					lblRoomTypes.setForeground(Color.WHITE);
					lblRoomTypes.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblRoomTypes = new GridBagConstraints();
					gbc_lblRoomTypes.anchor = GridBagConstraints.WEST;
					gbc_lblRoomTypes.insets = new Insets(0, 0, 5, 5);
					gbc_lblRoomTypes.gridx = 0;
					gbc_lblRoomTypes.gridy = y;
					contentPanel.add(lblRoomTypes, gbc_lblRoomTypes);
				}
				{
					for (RoomType rt : RoomController.getRoomTypes()) {
						JCheckBox cb = new JCheckBox(rt.getName());
						cb.setForeground(Color.WHITE);
						cb.setFont(new Font("Times New Roman", Font.PLAIN, 14));
						cb.setBackground(new Color(73, 73, 73));
						cb.setSelected(Filters.getRoomTypes().contains(rt));
						roomTypes.add(new Pair<>(cb, rt));
						GridBagConstraints gbc_cb = new GridBagConstraints();
						gbc_cb.fill = GridBagConstraints.HORIZONTAL;
						gbc_cb.insets = new Insets(0, 0, 5, 0);
						gbc_cb.gridx = 1;
						gbc_cb.gridy = y++;
						contentPanel.add(cb, gbc_cb);
					}
				}
				{
					Component verticalStrut = Box.createVerticalStrut(10);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 0;
					gbc_verticalStrut.gridy = y++;
					contentPanel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					JLabel lblRoomAdditions = new JLabel("Room Additions:");
					lblRoomAdditions.setHorizontalAlignment(SwingConstants.LEFT);
					lblRoomAdditions.setForeground(Color.WHITE);
					lblRoomAdditions.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblRoomAdditions = new GridBagConstraints();
					gbc_lblRoomAdditions.anchor = GridBagConstraints.WEST;
					gbc_lblRoomAdditions.insets = new Insets(0, 0, 5, 5);
					gbc_lblRoomAdditions.gridx = 0;
					gbc_lblRoomAdditions.gridy = y;
					contentPanel.add(lblRoomAdditions, gbc_lblRoomAdditions);
				}
				{
					for (RoomAddition ra : RoomController.getRoomAdditions()) {
						JCheckBox cb = new JCheckBox(ra.getName());
						cb.setForeground(Color.WHITE);
						cb.setFont(new Font("Times New Roman", Font.PLAIN, 14));
						cb.setBackground(new Color(73, 73, 73));
						cb.setSelected(Filters.getRoomAdditions().contains(ra));
						roomAdditions.add(new Pair<>(cb, ra));
						GridBagConstraints gbc_cb = new GridBagConstraints();
						gbc_cb.fill = GridBagConstraints.HORIZONTAL;
						gbc_cb.insets = new Insets(0, 0, 5, 0);
						gbc_cb.gridx = 1;
						gbc_cb.gridy = y++;
						contentPanel.add(cb, gbc_cb);
					}
				}
				{
					Component verticalStrut = Box.createVerticalStrut(10);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 0;
					gbc_verticalStrut.gridy = y++;
					contentPanel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					JLabel lblReservatinAdditions = new JLabel("Reservation Additions:");
					lblReservatinAdditions.setHorizontalAlignment(SwingConstants.LEFT);
					lblReservatinAdditions.setForeground(Color.WHITE);
					lblReservatinAdditions.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblReservatinAdditions = new GridBagConstraints();
					gbc_lblReservatinAdditions.anchor = GridBagConstraints.WEST;
					gbc_lblReservatinAdditions.insets = new Insets(0, 0, 5, 5);
					gbc_lblReservatinAdditions.gridx = 0;
					gbc_lblReservatinAdditions.gridy = y;
					contentPanel.add(lblReservatinAdditions, gbc_lblReservatinAdditions);
				}
				{
					for (ReservationAddition ra : ReservationController.getReservationAdditions()) {
						JCheckBox cb = new JCheckBox(ra.getName());
						cb.setForeground(Color.WHITE);
						cb.setFont(new Font("Times New Roman", Font.PLAIN, 14));
						cb.setBackground(new Color(73, 73, 73));
						cb.setSelected(Filters.getReservationAdditions().contains(ra));
						reservationAdditions.add(new Pair<>(cb, ra));
						GridBagConstraints gbc_cb = new GridBagConstraints();
						gbc_cb.fill = GridBagConstraints.HORIZONTAL;
						gbc_cb.insets = new Insets(0, 0, 5, 0);
						gbc_cb.gridx = 1;
						gbc_cb.gridy = y++;
						contentPanel.add(cb, gbc_cb);
					}
				}
				{
					Component verticalStrut = Box.createVerticalStrut(10);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 0;
					gbc_verticalStrut.gridy = y++;
					contentPanel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					JLabel lblPrice = new JLabel("Price:");
					lblPrice.setHorizontalAlignment(SwingConstants.LEFT);
					lblPrice.setForeground(Color.WHITE);
					lblPrice.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblPrice = new GridBagConstraints();
					gbc_lblPrice.anchor = GridBagConstraints.WEST;
					gbc_lblPrice.insets = new Insets(0, 0, 5, 5);
					gbc_lblPrice.gridx = 0;
					gbc_lblPrice.gridy = y;
					contentPanel.add(lblPrice, gbc_lblPrice);
				}
				{
					enablePriceCb = new JCheckBox("use this filter");
					enablePriceCb.setForeground(Color.WHITE);
					enablePriceCb.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					enablePriceCb.setBackground(new Color(73, 73, 73));
					enablePriceCb.addItemListener(priceListener);
					enablePriceCb.setSelected(Filters.isPriceEnabled());
					GridBagConstraints gbc_enablePriceCb = new GridBagConstraints();
					gbc_enablePriceCb.fill = GridBagConstraints.HORIZONTAL;
					gbc_enablePriceCb.insets = new Insets(0, 0, 5, 0);
					gbc_enablePriceCb.gridx = 1;
					gbc_enablePriceCb.gridy = y++;
					contentPanel.add(enablePriceCb, gbc_enablePriceCb);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(10);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 0;
					gbc_verticalStrut.gridy = y++;
					contentPanel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					JLabel lblMinPrice = new JLabel("Min Price:");
					lblMinPrice.setHorizontalAlignment(SwingConstants.LEFT);
					lblMinPrice.setForeground(Color.WHITE);
					lblMinPrice.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblMinPrice = new GridBagConstraints();
					gbc_lblMinPrice.anchor = GridBagConstraints.WEST;
					gbc_lblMinPrice.insets = new Insets(0, 0, 5, 5);
					gbc_lblMinPrice.gridx = 0;
					gbc_lblMinPrice.gridy = y;
					contentPanel.add(lblMinPrice, gbc_lblMinPrice);
				}
				{
					minPriceSp = new JSpinner();
					minPriceSp.setEnabled(Filters.isPriceEnabled());
					minPriceSp.setModel(
							new SpinnerNumberModel(Integer.valueOf(0), Integer.valueOf(0), null, Integer.valueOf(100)));
					minPriceSp.setValue(Filters.getMinPrice());
					GridBagConstraints gbc_minPriceSp = new GridBagConstraints();
					gbc_minPriceSp.fill = GridBagConstraints.HORIZONTAL;
					gbc_minPriceSp.insets = new Insets(0, 0, 5, 0);
					gbc_minPriceSp.gridx = 1;
					gbc_minPriceSp.gridy = y++;
					contentPanel.add(minPriceSp, gbc_minPriceSp);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(10);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 0;
					gbc_verticalStrut.gridy = y++;
					contentPanel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					JLabel lblMaxPrice = new JLabel("Max Price:");
					lblMaxPrice.setHorizontalAlignment(SwingConstants.LEFT);
					lblMaxPrice.setForeground(Color.WHITE);
					lblMaxPrice.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblMaxPrice = new GridBagConstraints();
					gbc_lblMaxPrice.anchor = GridBagConstraints.WEST;
					gbc_lblMaxPrice.insets = new Insets(0, 0, 0, 5);
					gbc_lblMaxPrice.gridx = 0;
					gbc_lblMaxPrice.gridy = y;
					contentPanel.add(lblMaxPrice, gbc_lblMaxPrice);
				}
				{
					maxPriceSp = new JSpinner();
					maxPriceSp.setEnabled(Filters.isPriceEnabled());
					maxPriceSp.setModel(
							new SpinnerNumberModel(Integer.valueOf(0), Integer.valueOf(0), null, Integer.valueOf(100)));
					maxPriceSp.setValue(Filters.getMaxPrice());
					GridBagConstraints gbc_maxPriceSp = new GridBagConstraints();
					gbc_maxPriceSp.fill = GridBagConstraints.HORIZONTAL;
					gbc_maxPriceSp.gridx = 1;
					gbc_maxPriceSp.gridy = y++;
					contentPanel.add(maxPriceSp, gbc_maxPriceSp);
				}
			}
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
					okButton.addActionListener(new ActionListener() {
						@Override
						public void actionPerformed(ActionEvent e) {
							ArrayList<ReservationStatus> selectedStatuses = new ArrayList<>();
							for (Pair<JCheckBox, ReservationStatus> pair : statuses) {
								if (pair.getFirst().isSelected()) {
									selectedStatuses.add(pair.getSecond());
								}
							}
							ArrayList<RoomType> selectedRoomTypes = new ArrayList<>();
							for (Pair<JCheckBox, RoomType> pair : roomTypes) {
								if (pair.getFirst().isSelected()) {
									selectedRoomTypes.add(pair.getSecond());
								}
							}
							ArrayList<ReservationAddition> selectedReservationAdditions = new ArrayList<>();
							for (Pair<JCheckBox, ReservationAddition> pair : reservationAdditions) {
								if (pair.getFirst().isSelected()) {
									selectedReservationAdditions.add(pair.getSecond());
								}
							}
							ArrayList<RoomAddition> selectedRoomAdditions = new ArrayList<>();
							for (Pair<JCheckBox, RoomAddition> pair : roomAdditions) {
								if (pair.getFirst().isSelected()) {
									selectedRoomAdditions.add(pair.getSecond());
								}
							}
							int minPrice = (int) minPriceSp.getValue();
							int maxPrice = (int) maxPriceSp.getValue();
							boolean priceEnabled = enablePriceCb.isSelected();
							Filters.setPriceEnabled(priceEnabled);
							Filters.setMinPrice(minPrice);
							Filters.setMaxPrice(maxPrice);
							Filters.setStatuses(selectedStatuses);
							Filters.setRoomTypes(selectedRoomTypes);
							Filters.setReservationAdditions(selectedReservationAdditions);
							Filters.setRoomAdditions(selectedRoomAdditions);
							dispose();
						}
					});
					{
						JButton resetBtn = new JButton("Reset");
						resetBtn.setFont(new Font("Times New Roman", Font.PLAIN, 14));
						resetBtn.addActionListener(new ActionListener() {
							@Override
							public void actionPerformed(ActionEvent e) {
                                for (Pair<JCheckBox, ReservationStatus> pair : statuses) {
                                    pair.getFirst().setSelected(true);
                                }
                                for (Pair<JCheckBox, RoomType> pair : roomTypes) {
                                    pair.getFirst().setSelected(true);
                                }
                                for (Pair<JCheckBox, ReservationAddition> pair : reservationAdditions) {
                                    pair.getFirst().setSelected(true);
                                }
                                for (Pair<JCheckBox, RoomAddition> pair : roomAdditions) {
                                    pair.getFirst().setSelected(true);
                                }
                                minPriceSp.setValue(0);
                                maxPriceSp.setValue(0);
                                enablePriceCb.setSelected(false);
                                minPriceSp.setEnabled(false);
                                maxPriceSp.setEnabled(false);
                                Filters.reset();
                            }
						});
						buttonPane.add(resetBtn);
					}
					buttonPane.add(okButton);
					getRootPane().setDefaultButton(okButton);
				}
			}
		}
	}

}
