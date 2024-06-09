	package views.components;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.util.ArrayList;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.ListSelectionModel;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

import models.Model;
import utils.CustomTableModel;

public class DataPanel<T extends Model> extends JPanel {

	private static final long serialVersionUID = 1L;

	private JTable table;
	private JPanel panel;
	private JButton refreshBtn;
	private JButton addBtn;
	private JButton editBtn;
	private JButton deleteBtn;
	
	private ArrayList<JButton> addedSelectiveButtons;
	
	
	/**
	 * Create the panel.
	 */
	public DataPanel(CustomTableModel<T> model) {
		setBackground(new Color(73, 73, 73));
		setLayout(new BorderLayout(0, 0));
		
		panel = new JPanel();
		FlowLayout flowLayout = (FlowLayout) panel.getLayout();
		flowLayout.setAlignment(FlowLayout.LEFT);
		panel.setBackground(new Color(73, 73, 73));
		add(panel, BorderLayout.NORTH);
		
		refreshBtn = new JButton("Refresh");
		refreshBtn.setMnemonic(KeyEvent.VK_R);
		refreshBtn.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		refreshBtn.setIcon(new ImageIcon("./assets/icons/refresh.png"));
		panel.add(refreshBtn);
		
		addBtn = new JButton("Add");
		addBtn.setMnemonic(KeyEvent.VK_A);
		addBtn.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		addBtn.setIcon(new ImageIcon("./assets/icons/plus.png"));
		panel.add(addBtn);
		
		editBtn = new JButton("Edit");
		editBtn.setEnabled(false);
		editBtn.setMnemonic(KeyEvent.VK_E);
		editBtn.setIcon(new ImageIcon("./assets/icons/edit.png"));
		editBtn.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		panel.add(editBtn);
		
		deleteBtn = new JButton("Delete");
		deleteBtn.setEnabled(false);
		deleteBtn.setMnemonic(KeyEvent.VK_D);
		deleteBtn.setIcon(new ImageIcon("./assets/icons/delete.png"));
		deleteBtn.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		panel.add(deleteBtn);
		
		JScrollPane scrollPane = new JScrollPane();
		scrollPane.getViewport().setBackground(new Color(73, 73, 73));
		add(scrollPane, BorderLayout.CENTER);
		
		table = new JTable(model);
		table.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
		table.setRowHeight(30);
		table.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
		table.setForeground(Color.WHITE);
		table.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		table.setBackground(new Color(73, 73, 73));
		table.getTableHeader().setFont(new Font("Times New Roman", Font.BOLD, 14));
		//table.setAutoCreateRowSorter(true);
		table.getSelectionModel().addListSelectionListener(new ListSelectionListener() {
			
			@Override
			public void valueChanged(ListSelectionEvent e) {
				editBtn.setEnabled(table.getSelectedRow() != -1);
				deleteBtn.setEnabled(table.getSelectedRow() != -1);
				for (JButton button : addedSelectiveButtons) {
					button.setEnabled(table.getSelectedRow() != -1);
				}
			}
		});
		
		scrollPane.setViewportView(table);
		
		addedSelectiveButtons = new ArrayList<JButton>();
	}

	public JButton addButton(String text, String iconPath, ActionListener actionListener) {
		return addButton(text, iconPath, actionListener, false);
	}
	
	public JButton addButton(String text, String iconPath, ActionListener actionListener, boolean folowsSelections) {
		JButton button = new JButton(text);
		button.setIcon(new ImageIcon(iconPath));
		button.addActionListener(actionListener);
		panel.add(button);
		if (folowsSelections) {
			addedSelectiveButtons.add(button);
			button.setEnabled(false);
		}
		return button;
	}
	
	public JTable getTable() {
		return table;
	}
	
	public JButton getRefreshBtn() {
		return refreshBtn;
	}
	
	public JButton getAddBtn() {
		return addBtn;
	}
	
	public JButton getEditBtn() {
		return editBtn;
	}
	
	public JButton getDeleteBtn() {
		return deleteBtn;
	}
}
	
	
