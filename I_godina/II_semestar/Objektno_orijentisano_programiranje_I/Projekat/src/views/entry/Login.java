package views.entry;

import java.awt.Color;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.Box;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.border.EmptyBorder;

import app.AppState;
import controllers.ControllerActionStatus;
import controllers.UserController;
import models.User;
import utils.WindowUtils;
import views.admin.MainAdmin;
import views.guests.MainGuest;
import views.maid.MainMaid;
import views.receptionist.MainReceptionist;

public class Login extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private JTextField textField;
	private JPasswordField passwordField;


	/**
	 * Create the frame.
	 */
	public Login() {
		setIconImage(WindowUtils.getIconImage());
		setForeground(new Color(255, 255, 255));
		setBackground(new Color(73, 73, 73));
		setBounds(100, 100, 500, 450);
		setResizable(false);
		setLocationRelativeTo(null);
		contentPane = new JPanel();
		contentPane.setBackground(new Color(73, 73, 73));
		contentPane.setBorder(new EmptyBorder(15, 15, 15, 15));
		setTitle("MHotelify | Login");
		setContentPane(contentPane);
		GridBagLayout gbl_contentPane = new GridBagLayout();
		gbl_contentPane.columnWidths = new int[] { 0, 0, 0 };
		gbl_contentPane.rowHeights = new int[] { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
		gbl_contentPane.columnWeights = new double[] { 0.0, 1.0, Double.MIN_VALUE };
		gbl_contentPane.rowWeights = new double[] { 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, Double.MIN_VALUE };
		contentPane.setLayout(gbl_contentPane);

		JLabel lblNewLabel_2 = new JLabel("");
		lblNewLabel_2.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_2.setIcon(
				new ImageIcon("./assets/logo/main_small.png"));
		lblNewLabel_2.setMaximumSize(new Dimension(100, 100));
		GridBagConstraints gbc_lblNewLabel_2 = new GridBagConstraints();
		gbc_lblNewLabel_2.gridwidth = 2;
		gbc_lblNewLabel_2.insets = new Insets(0, 0, 5, 0);
		gbc_lblNewLabel_2.gridx = 0;
		gbc_lblNewLabel_2.gridy = 0;
		contentPane.add(lblNewLabel_2, gbc_lblNewLabel_2);

		JLabel lblNewLabel = new JLabel("Welcome Back");
		lblNewLabel.setForeground(new Color(255, 255, 255));
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setFont(new Font("Times New Roman", Font.BOLD, 24));
		GridBagConstraints gbc_lblNewLabel = new GridBagConstraints();
		gbc_lblNewLabel.fill = GridBagConstraints.HORIZONTAL;
		gbc_lblNewLabel.gridwidth = 2;
		gbc_lblNewLabel.insets = new Insets(0, 0, 5, 0);
		gbc_lblNewLabel.gridx = 0;
		gbc_lblNewLabel.gridy = 2;
		contentPane.add(lblNewLabel, gbc_lblNewLabel);

		Component verticalStrut_1_1 = Box.createVerticalStrut(10);
		GridBagConstraints gbc_verticalStrut_1_1 = new GridBagConstraints();
		gbc_verticalStrut_1_1.gridwidth = 2;
		gbc_verticalStrut_1_1.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_1_1.gridx = 0;
		gbc_verticalStrut_1_1.gridy = 3;
		contentPane.add(verticalStrut_1_1, gbc_verticalStrut_1_1);

		JLabel lblNewLabel_1 = new JLabel("Username: ");
		lblNewLabel_1.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		lblNewLabel_1.setForeground(new Color(255, 255, 255));
		GridBagConstraints gbc_lblNewLabel_1 = new GridBagConstraints();
		gbc_lblNewLabel_1.insets = new Insets(0, 0, 5, 5);
		gbc_lblNewLabel_1.anchor = GridBagConstraints.EAST;
		gbc_lblNewLabel_1.gridx = 0;
		gbc_lblNewLabel_1.gridy = 5;
		contentPane.add(lblNewLabel_1, gbc_lblNewLabel_1);

		textField = new JTextField();
		textField.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_textField = new GridBagConstraints();
		gbc_textField.insets = new Insets(0, 0, 5, 0);
		gbc_textField.fill = GridBagConstraints.HORIZONTAL;
		gbc_textField.gridx = 1;
		gbc_textField.gridy = 5;
		contentPane.add(textField, gbc_textField);
		textField.setColumns(10);

		Component verticalStrut_1 = Box.createVerticalStrut(10);
		GridBagConstraints gbc_verticalStrut_1 = new GridBagConstraints();
		gbc_verticalStrut_1.gridwidth = 2;
		gbc_verticalStrut_1.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_1.gridx = 0;
		gbc_verticalStrut_1.gridy = 6;
		contentPane.add(verticalStrut_1, gbc_verticalStrut_1);

		JLabel lblNewLabel_1_1 = new JLabel("Password:");
		lblNewLabel_1_1.setForeground(Color.WHITE);
		lblNewLabel_1_1.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblNewLabel_1_1 = new GridBagConstraints();
		gbc_lblNewLabel_1_1.anchor = GridBagConstraints.EAST;
		gbc_lblNewLabel_1_1.insets = new Insets(0, 0, 5, 5);
		gbc_lblNewLabel_1_1.gridx = 0;
		gbc_lblNewLabel_1_1.gridy = 7;
		contentPane.add(lblNewLabel_1_1, gbc_lblNewLabel_1_1);

		passwordField = new JPasswordField();
		passwordField.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_passwordField = new GridBagConstraints();
		gbc_passwordField.insets = new Insets(0, 0, 5, 0);
		gbc_passwordField.fill = GridBagConstraints.HORIZONTAL;
		gbc_passwordField.gridx = 1;
		gbc_passwordField.gridy = 7;
		contentPane.add(passwordField, gbc_passwordField);

		Component verticalStrut_2 = Box.createVerticalStrut(10);
		GridBagConstraints gbc_verticalStrut_2 = new GridBagConstraints();
		gbc_verticalStrut_2.gridwidth = 2;
		gbc_verticalStrut_2.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_2.gridx = 0;
		gbc_verticalStrut_2.gridy = 8;
		contentPane.add(verticalStrut_2, gbc_verticalStrut_2);

		JButton btnNewButton = new JButton("Login");
		btnNewButton.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_btnNewButton = new GridBagConstraints();
		gbc_btnNewButton.gridwidth = 2;
		gbc_btnNewButton.gridx = 0;
		gbc_btnNewButton.gridy = 9;
		contentPane.add(btnNewButton, gbc_btnNewButton);
		setDefaultCloseOperation(DO_NOTHING_ON_CLOSE);
		addWindowListener(WindowUtils.getWindowClosing());
		ActionListener loginListener = new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String username = textField.getText().trim();
				String password = new String(passwordField.getPassword()).trim();

				if (username.isBlank()) {
					JOptionPane.showMessageDialog(contentPane, "Please enter a username.");
					return;
				}
				if (password.isBlank()) {
					JOptionPane.showMessageDialog(contentPane, "Please enter a password.");
					return;
				}
				
				ControllerActionStatus loginStatus = UserController.login(username, password);

				switch (loginStatus) {
					case NO_RECORD:
						JOptionPane.showMessageDialog(contentPane, "User with username '" + username + "' does not exist.");
						break;
					case WRONG_PASSWORD:
						JOptionPane.showMessageDialog(contentPane, "Incorrect password.");
						break;
					case SUCCESS:
						User user = AppState.getInstance().getUser();
						switch (user.getRole()) {
						case ADMIN:
							dispose();
							new MainAdmin().setVisible(true);
							break;
						case RECEPTIONIST:
							dispose();
							new MainReceptionist().setVisible(true);
							break;
						case MAID:
							dispose();
							new MainMaid().setVisible(true);
							break;
						case GUEST:
	                        dispose();
	                        new MainGuest().setVisible(true);
	                        break;
						}
						break;
					case INCOPLETE_DATA:
						JOptionPane.showMessageDialog(contentPane, "Please enter a username and password.");
						break;
					default:
						JOptionPane.showMessageDialog(contentPane, "An error occurred. Please try again.");
				}
			}
		};
		
		btnNewButton.addActionListener(loginListener);
		textField.addActionListener(loginListener);
		passwordField.addActionListener(loginListener);
	}

}
