package views.dialogs.price_lists;

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
import java.time.LocalDate;
import java.util.ArrayList;

import javax.swing.Box;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSpinner;
import javax.swing.JTextField;
import javax.swing.SpinnerNumberModel;
import javax.swing.SwingConstants;
import javax.swing.border.EmptyBorder;

import com.toedter.calendar.JDateChooser;

import controllers.ReservationController;
import controllers.RoomController;
import models.Model;
import models.PriceList;
import models.ReservationAddition;
import models.RoomType;
import utils.Pair;


public class AddPriceListDialog extends JDialog {

	/**
	 * @return the ok
	 */
	public boolean isOk() {
		return ok;
	}

	/**
	 * @return the guest
	 */
	public PriceList getPriceList() {
		return priceList;
	}

	private static final long serialVersionUID = 1L;
	private final JPanel contentPanel = new JPanel();
	private JLabel lblNewLabel_5;
	private JLabel lblNewLabel_2_1;
	private JTextField idTf;
	private JDateChooser startDateCh;
	private JDateChooser endDateCh;
	private ArrayList<Pair<RoomType, JSpinner>> roomTypes;
	private ArrayList<Pair<ReservationAddition, JSpinner>> reservationAdditions;
	
	private PriceList priceList;
	private boolean ok = false;

	/**
	 * Create the dialog.
	 */
	public AddPriceListDialog() {
		priceList = new PriceList();
		setTitle("Add New Price List");
		setModal(true);
		setIconImage(new ImageIcon("./assets/icons/price_lists.png").getImage());
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
					JLabel lblNewLabel = new JLabel("Add Price List:");
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
					JLabel lblNewLabel_5_1 = new JLabel("Room types prices:");
					lblNewLabel_5_1.setForeground(Color.WHITE);
					lblNewLabel_5_1.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_5_1 = new GridBagConstraints();
					gbc_lblNewLabel_5_1.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_5_1.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_5_1.gridx = 1;
					gbc_lblNewLabel_5_1.gridwidth = 2;
					gbc_lblNewLabel_5_1.gridy = y++;
					panel.add(lblNewLabel_5_1, gbc_lblNewLabel_5_1);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(10);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = y++;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					roomTypes = new ArrayList<Pair<RoomType, JSpinner>>();
					for (RoomType rt : RoomController.getRoomTypes()) {
						JLabel lblNewLabel_5_1 = new JLabel(rt.getName() + ":");
						lblNewLabel_5_1.setForeground(Color.WHITE);
						lblNewLabel_5_1.setFont(new Font("Times New Roman", Font.PLAIN, 14));
						GridBagConstraints gbc_lblNewLabel_5_1 = new GridBagConstraints();
						gbc_lblNewLabel_5_1.anchor = GridBagConstraints.WEST;
						gbc_lblNewLabel_5_1.insets = new Insets(0, 0, 5, 5);
						gbc_lblNewLabel_5_1.gridx = 1;
						gbc_lblNewLabel_5_1.gridy = y;
						panel.add(lblNewLabel_5_1, gbc_lblNewLabel_5_1);
						JSpinner spinner = new JSpinner();
						spinner.setModel(new SpinnerNumberModel(Double.valueOf(0), Double.valueOf(0), null, Double.valueOf(50)));
						spinner.setFont(new Font("Times New Roman", Font.PLAIN, 14));
						GridBagConstraints gbc_spinner = new GridBagConstraints();
						gbc_spinner.fill = GridBagConstraints.HORIZONTAL;
						gbc_spinner.insets = new Insets(0, 0, 5, 0);
						gbc_spinner.gridx = 2;
						gbc_spinner.gridy = y++;
						panel.add(spinner, gbc_spinner);
						roomTypes.add(new Pair<RoomType, JSpinner>(rt, spinner));
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
					JLabel lblNewLabel_5_1 = new JLabel("Reservation additions prices:");
					lblNewLabel_5_1.setForeground(Color.WHITE);
					lblNewLabel_5_1.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_5_1 = new GridBagConstraints();
					gbc_lblNewLabel_5_1.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_5_1.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_5_1.gridx = 1;
					gbc_lblNewLabel_5_1.gridy = y++;
					gbc_lblNewLabel_5_1.gridwidth = 2;
					panel.add(lblNewLabel_5_1, gbc_lblNewLabel_5_1);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(10);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = y++;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					reservationAdditions = new ArrayList<Pair<ReservationAddition, JSpinner>>();
					for (ReservationAddition ra : ReservationController.getReservationAdditions()) {
						JLabel lblNewLabel_5_1 = new JLabel(ra.getName() + ":");
						lblNewLabel_5_1.setForeground(Color.WHITE);
						lblNewLabel_5_1.setFont(new Font("Times New Roman", Font.PLAIN, 14));
						GridBagConstraints gbc_lblNewLabel_5_1 = new GridBagConstraints();
						gbc_lblNewLabel_5_1.anchor = GridBagConstraints.WEST;
						gbc_lblNewLabel_5_1.insets = new Insets(0, 0, 5, 5);
						gbc_lblNewLabel_5_1.gridx = 1;
						gbc_lblNewLabel_5_1.gridy = y;
						panel.add(lblNewLabel_5_1, gbc_lblNewLabel_5_1);
						JSpinner spinner = new JSpinner();
						spinner.setModel(new SpinnerNumberModel(Double.valueOf(0), Double.valueOf(0), null, Double.valueOf(50)));
						spinner.setFont(new Font("Times New Roman", Font.PLAIN, 14));
						GridBagConstraints gbc_spinner = new GridBagConstraints();
						gbc_spinner.fill = GridBagConstraints.HORIZONTAL;
						gbc_spinner.insets = new Insets(0, 0, 5, 0);
						gbc_spinner.gridx = 2;
						gbc_spinner.gridy = y++;
						panel.add(spinner, gbc_spinner);
						reservationAdditions.add(new Pair<ReservationAddition, JSpinner>(ra, spinner));
					}
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
						String id = idTf.getText();
						if (startDateCh.getDate() == null) {
							JOptionPane.showMessageDialog(getContentPane(), "Start date is required", "Error", JOptionPane.ERROR_MESSAGE);
							startDateCh.requestFocus();
							return;
						}
						LocalDate startDate = startDateCh.getDate().toInstant().atZone(java.time.ZoneId.systemDefault()).toLocalDate();
						LocalDate endDate = null;
						if (endDateCh.getDate() != null) {
							endDate = endDateCh.getDate().toInstant().atZone(java.time.ZoneId.systemDefault()).toLocalDate();
							if (startDate.isAfter(endDate)) {
								JOptionPane.showMessageDialog(getContentPane(), "Start date must be before end date",
										"Error", JOptionPane.ERROR_MESSAGE);
								startDateCh.requestFocus();
								return;
							}
						}
						priceList.setId(id);
						priceList.setStartDate(startDate);
						priceList.setEndDate(endDate);
						for (Pair<RoomType, JSpinner> rt : roomTypes) {
							priceList.setPrice(rt.getFirst(), (double) rt.getSecond().getValue());
						}
						for (Pair<ReservationAddition, JSpinner> ra : reservationAdditions) {
							priceList.setPrice(ra.getFirst(), (double) ra.getSecond().getValue());
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
		
		idTf.setText(Model.generateId());
	}
}
