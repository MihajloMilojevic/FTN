package views.receptionist;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.time.LocalDate;

import javax.swing.Box;
import javax.swing.DefaultListModel;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.border.EmptyBorder;

import controllers.ReportsController;
import utils.WindowUtils;

public class DailyLogsDialog extends JDialog {

	private static final long serialVersionUID = 1L;
	private JList<String> checkedIn;
	private JList<String> checkout;
	private JList<String> notYet;

	public DailyLogsDialog() {
		setTitle("Daily Logs");
		setFont(new Font("Times New Roman", Font.PLAIN, 14));
		setModal(true);
		setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
		setBounds(100, 100, 484, 442);
		setLocationRelativeTo(null);
		setIconImage(WindowUtils.getIconImage());
		getContentPane().setLayout(new BorderLayout());
		{
			JScrollPane scrollPane = new JScrollPane();
			getContentPane().add(scrollPane, BorderLayout.CENTER);
			{
				JPanel panel = new JPanel();
				panel.setBorder(new EmptyBorder(10, 10, 10, 10));
				panel.setForeground(new Color(255, 255, 255));
				panel.setBackground(new Color(73, 73, 73));
				scrollPane.setViewportView(panel);
				GridBagLayout gbl_panel = new GridBagLayout();
				gbl_panel.columnWidths = new int[]{0, 0, 0};
				gbl_panel.rowHeights = new int[]{0, 0, 0, 0, 0, 0};
				gbl_panel.columnWeights = new double[]{0.0, 1.0, Double.MIN_VALUE};
				gbl_panel.rowWeights = new double[]{0.0, 0.0, 1.0, 1.0, 1.0, Double.MIN_VALUE};
				panel.setLayout(gbl_panel);
				{
					LocalDate today = LocalDate.now();
					JLabel titleLb = new JLabel(String.format("Daily Logs - %d.%d.%d.", today.getDayOfMonth(), today.getMonthValue(), today.getYear()));
					titleLb.setForeground(new Color(255, 255, 255));
					titleLb.setFont(new Font("Times New Roman", Font.PLAIN, 24));
					GridBagConstraints gbc_titleLb = new GridBagConstraints();
					gbc_titleLb.gridwidth = 2;
					gbc_titleLb.insets = new Insets(0, 0, 5, 0);
					gbc_titleLb.gridx = 0;
					gbc_titleLb.gridy = 0;
					panel.add(titleLb, gbc_titleLb);
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
					JLabel lblNewLabel_1 = new JLabel("Today's check ins:");
					lblNewLabel_1.setForeground(new Color(255, 255, 255));
					lblNewLabel_1.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_1 = new GridBagConstraints();
					gbc_lblNewLabel_1.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_1.anchor = GridBagConstraints.NORTHWEST;
					gbc_lblNewLabel_1.gridx = 0;
					gbc_lblNewLabel_1.gridy = 2;
					panel.add(lblNewLabel_1, gbc_lblNewLabel_1);
				}
				{
					checkedIn = new JList<>();
					GridBagConstraints gbc_checkedIn = new GridBagConstraints();
					gbc_checkedIn.insets = new Insets(0, 0, 5, 0);
					gbc_checkedIn.fill = GridBagConstraints.BOTH;
					gbc_checkedIn.gridx = 1;
					gbc_checkedIn.gridy = 2;
					panel.add(checkedIn, gbc_checkedIn);
				}
				{
					JLabel lblNewLabel_1 = new JLabel("Today's check outs:");
					lblNewLabel_1.setForeground(Color.WHITE);
					lblNewLabel_1.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_1 = new GridBagConstraints();
					gbc_lblNewLabel_1.insets = new Insets(0, 0, 5, 5);
					gbc_lblNewLabel_1.anchor = GridBagConstraints.NORTHWEST;
					gbc_lblNewLabel_1.gridx = 0;
					gbc_lblNewLabel_1.gridy = 3;
					panel.add(lblNewLabel_1, gbc_lblNewLabel_1);
				}
				{
					checkout = new JList<>();
					GridBagConstraints gbc_checkout = new GridBagConstraints();
					gbc_checkout.insets = new Insets(0, 0, 5, 0);
					gbc_checkout.fill = GridBagConstraints.BOTH;
					gbc_checkout.gridx = 1;
					gbc_checkout.gridy = 3;
					panel.add(checkout, gbc_checkout);
				}
				{
					JLabel lblNewLabel_1 = new JLabel("Not cheked in yet:");
					lblNewLabel_1.setForeground(Color.WHITE);
					lblNewLabel_1.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_1 = new GridBagConstraints();
					gbc_lblNewLabel_1.insets = new Insets(0, 0, 0, 5);
					gbc_lblNewLabel_1.anchor = GridBagConstraints.NORTHWEST;
					gbc_lblNewLabel_1.gridx = 0;
					gbc_lblNewLabel_1.gridy = 4;
					panel.add(lblNewLabel_1, gbc_lblNewLabel_1);
				}
				{
					notYet = new JList<>();
					GridBagConstraints gbc_notYet = new GridBagConstraints();
					gbc_notYet.fill = GridBagConstraints.BOTH;
					gbc_notYet.gridx = 1;
					gbc_notYet.gridy = 4;
					panel.add(notYet, gbc_notYet);
				}
			}
		}
		DefaultListModel<String> model = new DefaultListModel<String>();
		for (String guest : ReportsController.getDailyCheckins()) {
			model.addElement(guest);
			checkedIn.setModel(model);
		}
		model = new DefaultListModel<String>();
		for (String guest : ReportsController.getDailyCheckouts()) {
			model.addElement(guest);
		}
		checkout.setModel(model);
		model = new DefaultListModel<String>();
		for (String guest : ReportsController.getDailyNotYet()) {
			model.addElement(guest);
		}
		notYet.setModel(model);
	}

}
