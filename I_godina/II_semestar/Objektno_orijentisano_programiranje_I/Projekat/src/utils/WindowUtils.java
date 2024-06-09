package utils;

import java.awt.Image;
import java.awt.Toolkit;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowListener;

import javax.swing.ImageIcon;
import javax.swing.JOptionPane;

import app.AppState;

public class WindowUtils {
	public static WindowListener getWindowClosing() {
		return new WindowAdapter() {
			@Override
			public void windowClosing(java.awt.event.WindowEvent windowEvent) {
				int close = JOptionPane.showConfirmDialog(windowEvent.getComponent(), "Are you sure you want to exit?",
						"Exit", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);

				if (close != JOptionPane.YES_OPTION)
					return;

				try {
					AppState.getInstance().save();
				} catch (Exception e) {
					e.printStackTrace();
					JOptionPane.showMessageDialog(windowEvent.getComponent(), "Error saving data. Data might be lost.");
				}
				System.exit(0);
			}
		};
	}
	

	public static Image getIconImage() {
		return new ImageIcon(AppState.getInstance().getSettings().getSetting("window", "icon_file_path", ""))
				.getImage();
	}
	

	public static Toolkit getToolkit() {
		return Toolkit.getDefaultToolkit();
	}
}
