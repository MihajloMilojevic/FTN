package views.dialogs.profile;

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
import java.time.ZoneId;

import javax.swing.Box;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.border.EmptyBorder;

import com.toedter.calendar.JDateChooser;

import models.User;
import models.enums.Gender;


public class UserProfileDialog extends JDialog {

	/**
	 * @return the ok
	 */
	public boolean isOk() {
		return ok;
	}

	/**
	 * @return the guest
	 */
	public User getUser() {
		return user;
	}

	private static final long serialVersionUID = 1L;
	private final JPanel contentPanel = new JPanel();
	private JComboBox<Gender> genderCb;
	private JTextField nameTf;
	private JTextField surnameTf;
	private JTextField usernameTf;
	private JDateChooser birthdateDP;
	private JTextField addressTf;
	private JTextField phoneTf;
	private JLabel lblNewLabel_3;
	private JLabel lblNewLabel_4;
	private JLabel lblNewLabel_5;
	private JLabel lblNewLabel_6;
	private JLabel lblNewLabel_7;
	private JLabel lblNewLabel_8;
	private JLabel lblNewLabel_9;
	private JTextField idTf;
	private JLabel lblNewLabel_2_1;
	
	private User user;
	private boolean ok = false;
	private JPasswordField passwordFl;
	private JLabel lblNewLabel_10;
	private Component verticalStrut_1;

	/**
	 * Create the dialog.
	 */
	public UserProfileDialog(User user) {
		this.user = user;
		setTitle("User Profile");
		setModal(true);
		setIconImage(new ImageIcon("./assets/icons/user.png").getImage());
		setFont(new Font("Times New Roman", Font.PLAIN, 14));
		setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
		getContentPane().setBackground(new Color(73, 73, 73));
		setBackground(new Color(73, 73, 73));
		getContentPane().setForeground(new Color(255, 255, 255));
		setForeground(new Color(255, 255, 255));
		setBounds(100, 100, 600, 500);
		setLocationRelativeTo(null);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBackground(new Color(73, 73, 73));
		contentPanel.setForeground(new Color(255, 255, 255));
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
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
				gbl_panel.columnWidths = new int[]{0, 0, 0, 0};
				gbl_panel.rowHeights = new int[]{0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
				gbl_panel.columnWeights = new double[]{0.0, 0.0, 1.0, Double.MIN_VALUE};
				gbl_panel.rowWeights = new double[]{0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, Double.MIN_VALUE};
				panel.setLayout(gbl_panel);
				{
					JLabel lblNewLabel = new JLabel("User Profile");
					lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
					lblNewLabel.setForeground(new Color(255, 255, 255));
					lblNewLabel.setFont(new Font("Times New Roman", Font.PLAIN, 24));
					GridBagConstraints gbc_lblNewLabel = new GridBagConstraints();
					gbc_lblNewLabel.insets = new Insets(0, 0, 5, 0);
					gbc_lblNewLabel.gridwidth = 3;
					gbc_lblNewLabel.fill = GridBagConstraints.BOTH;
					gbc_lblNewLabel.gridx = 0;
					gbc_lblNewLabel.gridy = 0;
					panel.add(lblNewLabel, gbc_lblNewLabel);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(15);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 0;
					gbc_verticalStrut.gridy = 1;
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
					gbc_lblNewLabel_2_1.gridy = 2;
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
					gbc_idTf.gridy = 2;
					panel.add(idTf, gbc_idTf);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(5);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = 3;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					lblNewLabel_3 = new JLabel("Name:");
					lblNewLabel_3.setForeground(Color.WHITE);
					lblNewLabel_3.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_3 = new GridBagConstraints();
					gbc_lblNewLabel_3.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_3.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_3.gridx = 1;
					gbc_lblNewLabel_3.gridy = 4;
					panel.add(lblNewLabel_3, gbc_lblNewLabel_3);
				}
				{
					nameTf = new JTextField();
					lblNewLabel_3.setLabelFor(nameTf);
					nameTf.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_nameTf = new GridBagConstraints();
					gbc_nameTf.insets = new Insets(0, 0, 5, 0);
					gbc_nameTf.fill = GridBagConstraints.HORIZONTAL;
					gbc_nameTf.gridx = 2;
					gbc_nameTf.gridy = 4;
					panel.add(nameTf, gbc_nameTf);
					nameTf.setColumns(10);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(5);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = 5;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					lblNewLabel_4 = new JLabel("Surname:");
					lblNewLabel_4.setForeground(Color.WHITE);
					lblNewLabel_4.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_4 = new GridBagConstraints();
					gbc_lblNewLabel_4.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_4.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_4.gridx = 1;
					gbc_lblNewLabel_4.gridy = 6;
					panel.add(lblNewLabel_4, gbc_lblNewLabel_4);
				}
				{
					surnameTf = new JTextField();
					lblNewLabel_4.setLabelFor(surnameTf);
					surnameTf.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					surnameTf.setColumns(10);
					GridBagConstraints gbc_surnameTf = new GridBagConstraints();
					gbc_surnameTf.insets = new Insets(0, 0, 5, 0);
					gbc_surnameTf.fill = GridBagConstraints.HORIZONTAL;
					gbc_surnameTf.gridx = 2;
					gbc_surnameTf.gridy = 6;
					panel.add(surnameTf, gbc_surnameTf);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(5);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = 7;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					lblNewLabel_5 = new JLabel("Username:");
					lblNewLabel_5.setForeground(Color.WHITE);
					lblNewLabel_5.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_5 = new GridBagConstraints();
					gbc_lblNewLabel_5.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_5.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_5.gridx = 1;
					gbc_lblNewLabel_5.gridy = 8;
					panel.add(lblNewLabel_5, gbc_lblNewLabel_5);
				}
				{
					usernameTf = new JTextField();
					lblNewLabel_5.setLabelFor(usernameTf);
					usernameTf.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					usernameTf.setColumns(10);
					GridBagConstraints gbc_usernameTf = new GridBagConstraints();
					gbc_usernameTf.insets = new Insets(0, 0, 5, 0);
					gbc_usernameTf.fill = GridBagConstraints.HORIZONTAL;
					gbc_usernameTf.gridx = 2;
					gbc_usernameTf.gridy = 8;
					panel.add(usernameTf, gbc_usernameTf);
				}
				{
					verticalStrut_1 = Box.createVerticalStrut(5);
					GridBagConstraints gbc_verticalStrut_1 = new GridBagConstraints();
					gbc_verticalStrut_1.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut_1.gridx = 1;
					gbc_verticalStrut_1.gridy = 9;
					panel.add(verticalStrut_1, gbc_verticalStrut_1);
				}
				{
					lblNewLabel_10 = new JLabel("Password:");
					lblNewLabel_10.setForeground(Color.WHITE);
					lblNewLabel_10.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_10 = new GridBagConstraints();
					gbc_lblNewLabel_10.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_10.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_10.gridx = 1;
					gbc_lblNewLabel_10.gridy = 10;
					panel.add(lblNewLabel_10, gbc_lblNewLabel_10);
				}
				{
					passwordFl = new JPasswordField();
					passwordFl.setFont(new Font("Tahoma", Font.PLAIN, 14));
					GridBagConstraints gbc_passwordFl = new GridBagConstraints();
					gbc_passwordFl.insets = new Insets(0, 0, 5, 0);
					gbc_passwordFl.fill = GridBagConstraints.HORIZONTAL;
					gbc_passwordFl.gridx = 2;
					gbc_passwordFl.gridy = 10;
					panel.add(passwordFl, gbc_passwordFl);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(5);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = 11;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					lblNewLabel_6 = new JLabel("Gender:");
					lblNewLabel_6.setForeground(Color.WHITE);
					lblNewLabel_6.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_6 = new GridBagConstraints();
					gbc_lblNewLabel_6.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_6.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_6.gridx = 1;
					gbc_lblNewLabel_6.gridy = 12;
					panel.add(lblNewLabel_6, gbc_lblNewLabel_6);
				}
				{
					genderCb = new JComboBox<Gender>();
					lblNewLabel_6.setLabelFor(genderCb);
					genderCb.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_genderCb = new GridBagConstraints();
					gbc_genderCb.insets = new Insets(0, 0, 5, 0);
					gbc_genderCb.fill = GridBagConstraints.HORIZONTAL;
					gbc_genderCb.gridx = 2;
					gbc_genderCb.gridy = 12;
					panel.add(genderCb, gbc_genderCb);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(5);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = 13;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					lblNewLabel_7 = new JLabel("Date of birth:");
					lblNewLabel_7.setForeground(Color.WHITE);
					lblNewLabel_7.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_7 = new GridBagConstraints();
					gbc_lblNewLabel_7.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_7.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_7.gridx = 1;
					gbc_lblNewLabel_7.gridy = 14;
					panel.add(lblNewLabel_7, gbc_lblNewLabel_7);
				}
				{
					birthdateDP = new JDateChooser();
					lblNewLabel_7.setLabelFor(birthdateDP);
					birthdateDP.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_textField = new GridBagConstraints();
					gbc_textField.insets = new Insets(0, 0, 5, 0);
					gbc_textField.fill = GridBagConstraints.HORIZONTAL;
					gbc_textField.gridx = 2;
					gbc_textField.gridy = 14;
					panel.add(birthdateDP, gbc_textField);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(5);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = 15;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					lblNewLabel_8 = new JLabel("Address:");
					lblNewLabel_8.setForeground(Color.WHITE);
					lblNewLabel_8.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_8 = new GridBagConstraints();
					gbc_lblNewLabel_8.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_8.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_8.gridx = 1;
					gbc_lblNewLabel_8.gridy = 16;
					panel.add(lblNewLabel_8, gbc_lblNewLabel_8);
				}
				{
					addressTf = new JTextField();
					lblNewLabel_8.setLabelFor(addressTf);
					addressTf.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					addressTf.setColumns(10);
					GridBagConstraints gbc_addressTf = new GridBagConstraints();
					gbc_addressTf.insets = new Insets(0, 0, 5, 0);
					gbc_addressTf.fill = GridBagConstraints.HORIZONTAL;
					gbc_addressTf.gridx = 2;
					gbc_addressTf.gridy = 16;
					panel.add(addressTf, gbc_addressTf);
				}
				{
					Component verticalStrut = Box.createVerticalStrut(5);
					GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
					gbc_verticalStrut.insets = new Insets(0, 0, 5, 5);
					gbc_verticalStrut.gridx = 1;
					gbc_verticalStrut.gridy = 17;
					panel.add(verticalStrut, gbc_verticalStrut);
				}
				{
					lblNewLabel_9 = new JLabel("Phone:");
					lblNewLabel_9.setForeground(Color.WHITE);
					lblNewLabel_9.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_9 = new GridBagConstraints();
					gbc_lblNewLabel_9.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_9.insets = new Insets(0, 0, 0, 5);
					gbc_lblNewLabel_9.gridx = 1;
					gbc_lblNewLabel_9.gridy = 18;
					panel.add(lblNewLabel_9, gbc_lblNewLabel_9);
				}
				{
					phoneTf = new JTextField();
					lblNewLabel_9.setLabelFor(phoneTf);
					phoneTf.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					phoneTf.setColumns(10);
					GridBagConstraints gbc_phoneTf = new GridBagConstraints();
					gbc_phoneTf.fill = GridBagConstraints.HORIZONTAL;
					gbc_phoneTf.gridx = 2;
					gbc_phoneTf.gridy = 18;
					panel.add(phoneTf, gbc_phoneTf);
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
						String name = nameTf.getText().trim();
						String surname = surnameTf.getText().trim();
						String username = usernameTf.getText().trim();
						String password = new String(passwordFl.getPassword());
						Gender gender = (Gender) genderCb.getSelectedItem();
						String address = addressTf.getText().trim();
						String phone = phoneTf.getText().trim();
						
						if (name.isBlank()) {
							JOptionPane.showMessageDialog(UserProfileDialog.this, "Name is required", "Error", JOptionPane.ERROR_MESSAGE);
							return;
						}
						if (surname.isBlank()) {
							JOptionPane.showMessageDialog(UserProfileDialog.this, "Surname is required", "Error",
									JOptionPane.ERROR_MESSAGE);
							return;
						}
						if (username.isBlank()) {
							JOptionPane.showMessageDialog(UserProfileDialog.this, "Username is required", "Error",
									JOptionPane.ERROR_MESSAGE);
							return;
						}
						if (password.isBlank()) {
							JOptionPane.showMessageDialog(UserProfileDialog.this, "Password is required", "Error",
									JOptionPane.ERROR_MESSAGE);
							return;
						}
						
						if (birthdateDP.getDate() == null) {
							JOptionPane.showMessageDialog(UserProfileDialog.this, "Date of birth is required", "Error",
									JOptionPane.ERROR_MESSAGE);
							return;
						}
						if (address.isBlank()) {
							JOptionPane.showMessageDialog(UserProfileDialog.this, "Address is required", "Error",
									JOptionPane.ERROR_MESSAGE);
							return;
						}
						if (phone.isBlank()) {
							JOptionPane.showMessageDialog(UserProfileDialog.this, "Phone is required", "Error",
									JOptionPane.ERROR_MESSAGE);
							return;
						}
						

						LocalDate birthdate = birthdateDP.getDate().toInstant().atZone(ZoneId.systemDefault()).toLocalDate(); // under all validations since it can throw exception
						user.setName(name);
						user.setSurname(surname);
						user.setUsername(username);
						user.setPassword(password);
						user.setGender(gender);
						user.setBirthdate(birthdate);
						user.setAddress(address);
						user.setPhone(phone);
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
		
		genderCb.addItem(Gender.MALE);
		genderCb.addItem(Gender.FEMALE);
		
		idTf.setText(user.getId());
		nameTf.setText(user.getName());
		surnameTf.setText(user.getSurname());
		usernameTf.setText(user.getUsername());
		passwordFl.setText(user.getPassword());
		genderCb.setSelectedItem(user.getGender());
		birthdateDP.setDate(java.util.Date.from(user.getBirthdate().atStartOfDay(ZoneId.systemDefault()).toInstant()));
		addressTf.setText(user.getAddress());
		phoneTf.setText(user.getPhone());
		
	}

}
