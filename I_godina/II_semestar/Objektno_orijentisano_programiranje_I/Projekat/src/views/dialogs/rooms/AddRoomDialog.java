package views.dialogs.rooms;

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
import java.util.ArrayList;

import javax.swing.Box;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSpinner;
import javax.swing.JTextField;
import javax.swing.ListCellRenderer;
import javax.swing.SpinnerNumberModel;
import javax.swing.SwingConstants;
import javax.swing.border.EmptyBorder;

import controllers.RoomController;
import models.Model;
import models.Room;
import models.RoomAddition;
import models.RoomType;


public class AddRoomDialog extends JDialog {

	/**
	 * @return the ok
	 */
	public boolean isOk() {
		return ok;
	}

	/**
	 * @return the guest
	 */
	public Room getRoom() {
		return room;
	}

	private static final long serialVersionUID = 1L;
	private final JPanel contentPanel = new JPanel();
	private JComboBox<RoomType> typeCb;
	private JLabel lblNewLabel_3;
	private JLabel lblNewLabel_4;
	private JLabel lblNewLabel_5;
	private JTextField idTf;
	private JLabel lblNewLabel_2_1;
	private ArrayList<JCheckBox> additionsCbs;
	
	private Room room;
	private boolean ok = false;
	private JSpinner numberSb;

	/**
	 * Create the dialog.
	 */
	public AddRoomDialog() {
		room = new Room();
		setTitle("Add New Room");
		setModal(true);
		setIconImage(new ImageIcon("./assets/icons/rooms.png").getImage());
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
				gbl_panel.rowHeights = new int[] {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
				gbl_panel.columnWeights = new double[]{0.0, 0.0, 1.0};
				gbl_panel.rowWeights = new double[]{0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, Double.MIN_VALUE};
				panel.setLayout(gbl_panel);
				{
					JLabel lblNewLabel = new JLabel("Add Room");
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
					lblNewLabel_3 = new JLabel("Room Number:");
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
					numberSb = new JSpinner();
					lblNewLabel_3.setLabelFor(numberSb);
					numberSb.setModel(new SpinnerNumberModel(Integer.valueOf(100), Integer.valueOf(100), null, Integer.valueOf(1)));
					GridBagConstraints gbc_numberSb = new GridBagConstraints();
					gbc_numberSb.fill = GridBagConstraints.HORIZONTAL;
					gbc_numberSb.insets = new Insets(0, 0, 5, 0);
					gbc_numberSb.gridx = 2;
					gbc_numberSb.gridy = 4;
					panel.add(numberSb, gbc_numberSb);
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
					lblNewLabel_4 = new JLabel("Room Type");
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
					typeCb = new JComboBox<RoomType>();
					lblNewLabel_4.setLabelFor(typeCb);
					typeCb.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_typeCb = new GridBagConstraints();
					gbc_typeCb.insets = new Insets(0, 0, 5, 0);
					gbc_typeCb.fill = GridBagConstraints.HORIZONTAL;
					gbc_typeCb.gridx = 2;
					gbc_typeCb.gridy = 6;
					panel.add(typeCb, gbc_typeCb);
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
					lblNewLabel_5 = new JLabel("Additions:");
					lblNewLabel_5.setForeground(Color.WHITE);
					lblNewLabel_5.setFont(new Font("Times New Roman", Font.PLAIN, 14));
					GridBagConstraints gbc_lblNewLabel_5 = new GridBagConstraints();
					gbc_lblNewLabel_5.anchor = GridBagConstraints.WEST;
					gbc_lblNewLabel_5.insets = new Insets(0, 0, 0, 5);
					gbc_lblNewLabel_5.gridx = 1;
					gbc_lblNewLabel_5.gridy = 8;
					panel.add(lblNewLabel_5, gbc_lblNewLabel_5);
				}
				{
					additionsCbs = new ArrayList<JCheckBox>();
					int y = 8;
					for (RoomAddition ra : RoomController.getRoomAdditions()) {
						JCheckBox cb = new JCheckBox(ra.getName());
						additionsCbs.add(cb);
						cb.setFont(new Font("Times New Roman", Font.PLAIN, 14));
						GridBagConstraints constrains = new GridBagConstraints();
						constrains.fill = GridBagConstraints.HORIZONTAL;
						constrains.gridwidth = 1;
						constrains.insets = new Insets(0, 0, 5, 0);
						constrains.gridx = 2;
						constrains.gridy = y;
						y += 1;
						panel.add(cb, constrains);
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
						String id = idTf.getText().trim();
						int number = (int) numberSb.getValue();
						RoomType type = (RoomType) typeCb.getSelectedItem();
						ArrayList<RoomAddition> additions = new ArrayList<RoomAddition>();
						for (JCheckBox cb : additionsCbs) {
							if (cb.isSelected()) {
								additions.add(RoomController.getRoomAdditionByName(cb.getText()));
							}
						}
						room = new Room(id, number, type);
						room.setRoomAdditions(additions);
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
		
		typeCb.setRenderer(new ListCellRenderer<RoomType>() {
            @Override
            public Component getListCellRendererComponent(JList<? extends RoomType> list, RoomType value, int index,
                    boolean isSelected, boolean cellHasFocus) {
                JLabel label = new JLabel(value.getName());
                label.setOpaque(true);
                label.setBackground(isSelected ? new Color(51, 153, 255) : new Color(73, 73, 73));
                label.setForeground(Color.WHITE);
                label.setFont(new Font("Times New Roman", Font.PLAIN, 14));
                return label;
            }
        });
		RoomController.getRoomTypes().forEach(typeCb::addItem);
		
		idTf.setText(Model.generateId());
		
	}

}
