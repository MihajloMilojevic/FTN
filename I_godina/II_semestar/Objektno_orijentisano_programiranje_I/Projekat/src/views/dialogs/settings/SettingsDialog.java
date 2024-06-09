package views.dialogs.settings;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTree;
import javax.swing.border.EmptyBorder;
import javax.swing.event.TreeModelListener;
import javax.swing.event.TreeSelectionEvent;
import javax.swing.event.TreeSelectionListener;
import javax.swing.tree.TreeCellRenderer;
import javax.swing.tree.TreeModel;
import javax.swing.tree.TreePath;

import app.AppSettings;

public class SettingsDialog extends JDialog {

	private static final long serialVersionUID = 1L;
	private final JPanel contentPanel = new JPanel();
	
	private JButton editBtn;
	private JTree tree;
	

	/**
	 * Create the dialog.
	 */
	public SettingsDialog() {
		setResizable(true);
		setModal(true);
		setIconImage(new ImageIcon("./assets/icons/settings.png").getImage());
		getContentPane().setBackground(new Color(73, 73, 73));
		setBackground(new Color(73, 73, 73));
		setTitle("Settings");
		setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
		setBounds(100, 100, 500, 500);
		setLocationRelativeTo(null);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBackground(new Color(73, 73, 73));
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		contentPanel.setLayout(new BorderLayout(0, 0));
		{
			JScrollPane scrollPane = new JScrollPane();
			contentPanel.add(scrollPane, BorderLayout.CENTER);
			{
				tree = new JTree();
				tree.setForeground(Color.WHITE);
				tree.setFont(new Font("Times New Roman", Font.PLAIN, 14));
				tree.setEditable(false);
				tree.setModel(new CustomTreeModel());
				tree.setBackground(new Color(73, 73, 73));
				tree.setCellRenderer(new CustomTreeCellRenderer());
				
				tree.addTreeSelectionListener(new TreeSelectionListener() {
					
					@Override
					public void valueChanged(TreeSelectionEvent e) {
						editBtn.setEnabled(e.getPath().getPath().length == 3);
					}
				});
				
				scrollPane.setViewportView(tree);
			}
		}
		{
			JPanel panel = new JPanel();
			FlowLayout flowLayout = (FlowLayout) panel.getLayout();
			flowLayout.setAlignment(FlowLayout.LEFT);
			panel.setBackground(new Color(73, 73, 73));
			contentPanel.add(panel, BorderLayout.NORTH);
			{
				editBtn = new JButton("Edit Selected Setting");
				editBtn.setIcon(new ImageIcon("./assets/icons/edit.png"));
				editBtn.setFont(new Font("Times New Roman", Font.PLAIN, 14));
				editBtn.setEnabled(false);
				editBtn.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						TreePath path = tree.getSelectionPath();
						if(path == null) { 
							JOptionPane.showMessageDialog(null, "Please select a setting to edit.", "Error", JOptionPane.ERROR_MESSAGE);
							return;
						}
						if (path.getPath().length != 3) {
							JOptionPane.showMessageDialog(null, "Please select a setting to edit.", "Error",
									JOptionPane.ERROR_MESSAGE);
							return;
						}
						String category = path.getPath()[1].toString();
						String setting = path.getPath()[2].toString();
						String value = AppSettings.getInstance().getSetting(category, setting, "");

						EditSettingsDialog dialog = new EditSettingsDialog(category+ "." + setting, value);
						
						dialog.setVisible(true);

						if (dialog.isOk()) {
							((CustomTreeModel) tree.getModel()).editSetting(category, setting, dialog.getValue());
							tree.updateUI();
							JOptionPane.showMessageDialog(null, "Setting updated successfully.\nYou may need to restart the app to see the changes", "Success",
									JOptionPane.INFORMATION_MESSAGE);
						}
					}
				});
				panel.add(editBtn);
			}
		}
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setBackground(new Color(73, 73, 73));
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				JButton okButton = new JButton("OK");
				okButton.setFont(new Font("Times New Roman", Font.PLAIN, 14));
				okButton.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						dispose();
					}
				});
				okButton.setActionCommand("OK");
				buttonPane.add(okButton);
				getRootPane().setDefaultButton(okButton);
			}
		}
	}

	private class CustomTreeModel implements TreeModel {
		private AppSettings settings;
		private String root = "App Settings";
		
		public CustomTreeModel() {
			settings = AppSettings.getInstance();
		}
		
		public Object getRoot() {
			return root;
		}

		public int getChildCount(Object parent) {
			if (parent.equals(root)) return settings.size();
			return settings.categorySize(parent.toString());
		}

		public Object getChild(Object parent, int index) {
			if (parent.equals(root))
				return settings.getCategories().get(index);
			return settings.getCategory(parent.toString()).keySet().toArray()[index].toString();
		}

		public int getIndexOfChild(Object parent, Object child) {
			if (parent.equals(root))
                return settings.getCategories().indexOf(child);
            Object[] settingsInCategory = settings.getCategory(parent.toString()).keySet().toArray();
			for (int i = 0; i < settingsInCategory.length; i++) {
				if (settingsInCategory[i].equals(child)) {
					return i;
				}
			}
			return -1;
        }

		public boolean isLeaf(Object node) {
			if (node.equals(root)) return false;
            if (settings.getCategory(node.toString()) == null) return true;
            return false;
		}
		
		public void editSetting(String category, String setting, String value) {
			settings.updateSetting(category, setting, value);
		}
		
		@Override
		public void valueForPathChanged(TreePath path, Object newValue) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void addTreeModelListener(TreeModelListener l) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void removeTreeModelListener(TreeModelListener l) {
			
		}		
	}

	private class CustomTreeCellRenderer implements TreeCellRenderer {
		
		@Override
		public Component getTreeCellRendererComponent(JTree tree, Object value, boolean selected, boolean expanded,
				boolean leaf, int row, boolean hasFocus) {
			JLabel label = new JLabel();
			
			
			label.addMouseMotionListener(new MouseAdapter() {
				@Override
				public void mousePressed(MouseEvent e) {
					JOptionPane.showMessageDialog(null, "CLIKKK");
				}
			});
			
			label.setText(value.toString());
			label.setForeground(Color.WHITE);
			label.setOpaque(true);
			label.setBackground(new Color(73, 73, 73));
			label.setFont(new Font("Times New Roman", Font.PLAIN, 14));
			if (selected) {
                label.setBackground(new Color(150, 150, 150));
            } 
			if(leaf) {
                label.setIcon(new ImageIcon("./assets/icons/setting.png"));
            } else {
                label.setIcon(new ImageIcon("./assets/icons/settings.png"));
            }
			
			return label;
		}
	}
}


