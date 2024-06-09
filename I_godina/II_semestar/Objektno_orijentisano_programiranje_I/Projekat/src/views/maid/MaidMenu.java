package views.maid;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.KeyStroke;

import app.AppState;
import controllers.ControllerActionStatus;
import controllers.UserController;
import models.User;
import views.dialogs.profile.UserProfileDialog;
import views.entry.Login;

public class MaidMenu extends JMenuBar {

	private static final long serialVersionUID = 8197696832664778633L;

	public MaidMenu(JFrame parent) {

		JMenu menu;
		JMenuItem item;

		menu = new JMenu("User");
		menu.setMnemonic(KeyEvent.VK_U);
		add(menu);

		item = new JMenuItem("Profile");
		item.setMnemonic(KeyEvent.VK_P);
		item.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_P, ActionEvent.CTRL_MASK));
		item.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				UserProfileDialog dialog = new UserProfileDialog(AppState.getInstance().getUser());
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@Override
					public void windowClosed(WindowEvent windowEvent) {
						if (!dialog.isOk())
							return;
						User updatedUser = dialog.getUser();
						ControllerActionStatus status = UserController.updateUser(updatedUser);
						switch (status) {
						case SUCCESS:
							AppState.getInstance().setUser(updatedUser);
							JOptionPane.showMessageDialog(parent.getContentPane(), "Profile updated successfully",
									"Success", JOptionPane.INFORMATION_MESSAGE);
							break;
						case NO_RECORD:
							JOptionPane.showMessageDialog(parent.getContentPane(), "User not found", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						case ERROR:
							JOptionPane.showMessageDialog(parent.getContentPane(), "An error occured", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(parent.getContentPane(), "An error occured", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						}
					}
				});
			}
		});
		menu.add(item);

		item = new JMenuItem("Logout");
		item.setMnemonic(KeyEvent.VK_L);
		item.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_L, ActionEvent.CTRL_MASK));
		item.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				int res = JOptionPane.showConfirmDialog(parent.getContentPane(), "Are you sure you want to logout?",
						"Logout", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
				if (res != JOptionPane.YES_OPTION)
					return;
				UserController.logout();
				parent.dispose();
				new Login().setVisible(true);
			}
		});
		menu.add(item);
	}

}
