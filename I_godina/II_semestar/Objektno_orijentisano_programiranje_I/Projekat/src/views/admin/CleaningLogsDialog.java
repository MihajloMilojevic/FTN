package views.admin;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.util.ArrayList;

import javax.swing.DefaultListModel;
import javax.swing.JDialog;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;

import controllers.RoomController;
import models.Room;
import utils.WindowUtils;

public class CleaningLogsDialog extends JDialog {

	private static final long serialVersionUID = 1L;

	public CleaningLogsDialog(Room room) {
		setTitle("Room " + room.getNumber() + " Cleaning Logs");
		setModal(true);
		setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
		setIconImage(WindowUtils.getIconImage());
		setFont(new Font("Times New Roman", Font.PLAIN, 14));
		setBounds(100, 100, 500, 500);
		setLocationRelativeTo(null);
		getContentPane().setLayout(new BorderLayout());
		
		JScrollPane scrollPane = new JScrollPane();
		getContentPane().add(scrollPane, BorderLayout.CENTER);
		
		JPanel panel = new JPanel();
		panel.setForeground(new Color(255, 255, 255));
		panel.setBackground(new Color(73, 73, 73));
		scrollPane.setViewportView(panel);
		panel.setLayout(new BorderLayout(0, 0));
		
		JList<String> list = new JList<>();
		list.setForeground(new Color(255, 255, 255));
		list.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		list.setBackground(new Color(73, 73, 73));
		panel.add(list, BorderLayout.CENTER);
		
		ArrayList<String> cleaningLogs = RoomController.getCleaningLogs(room);
		DefaultListModel<String> model = new DefaultListModel<String>();
		for (String log : cleaningLogs) {
            model.addElement(log);
        }
		list.setModel(model);
		
	}

}
