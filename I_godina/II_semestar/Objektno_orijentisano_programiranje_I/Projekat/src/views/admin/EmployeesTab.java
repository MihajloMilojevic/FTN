package views.admin;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.table.TableColumnModel;

import controllers.ControllerActionStatus;
import controllers.UserController;
import models.Admin;
import models.Employee;
import utils.CustomTableModel;
import utils.Pair;
import views.components.DataPanel;
import views.components.Tab;
import views.dialogs.employees.AddEmployeeDialog;
import views.dialogs.employees.EditEmployeeDialog;

public class EmployeesTab extends Tab<Employee> {

	public EmployeesTab(JFrame parent) {
		super(parent);
	}

	@Override
	protected void addColumns() {
		columns.add(new Pair<String, String>("ID", "id")); // 0
		columns.add(new Pair<String, String>("Role", "role")); // 1
		columns.add(new Pair<String, String>("Name", "name")); // 2
		columns.add(new Pair<String, String>("Surname", "surname")); // 3
		columns.add(new Pair<String, String>("Username", "username")); // 4
		columns.add(new Pair<String, String>("Gender", "gender")); // 5
		columns.add(new Pair<String, String>("Date of birth", "birthdate")); // 6
		columns.add(new Pair<String, String>("Address", "address")); // 7
		columns.add(new Pair<String, String>("Phone", "phone")); // 8
		columns.add(new Pair<String, String>("Level of professional education", "levelOfProfessionalEducation")); // 9
		columns.add(new Pair<String, String>("Years of work experience", "yearsOfWorkExperience")); // 10
		columns.add(new Pair<String, String>("Salary", "salary")); // 11
	}

	@Override
	protected void addModel() {
		model = new CustomTableModel<Employee>(this, columns, new CustomTableModel.TableDataManiplations<Employee>() {

			@Override
			public ArrayList<Employee> getData() {
				return UserController.getEmployees();
			}

			@Override
			public ControllerActionStatus edit(Employee model) {
				return UserController.updateUser(model);
			}

			@Override
			public ControllerActionStatus remove(Employee model) {
				return UserController.deleteUser(model);
			}

			@Override
			public ControllerActionStatus add(Employee model) {
				return UserController.addUser(model);
			}

		}, new Admin());
	}

	@Override
	protected void addDataPanel() {
		dataPanel = new DataPanel<Employee>(model);
	}

	@Override
	protected void setColumnsSize() {
		TableColumnModel columnModel = dataPanel.getTable().getColumnModel();
		columnModel.getColumn(0).setMinWidth(150);
		columnModel.getColumn(1).setMinWidth(150);
		columnModel.getColumn(2).setMinWidth(100);
		columnModel.getColumn(3).setMinWidth(100);
		columnModel.getColumn(4).setMinWidth(100);
		columnModel.getColumn(5).setMinWidth(100);
		columnModel.getColumn(6).setMinWidth(100);
		columnModel.getColumn(7).setMinWidth(300);
		columnModel.getColumn(8).setMinWidth(150);
		columnModel.getColumn(9).setMinWidth(200);
		columnModel.getColumn(10).setMinWidth(150);
		columnModel.getColumn(11).setMinWidth(100);
	}

	@Override
	protected void addRefreshButtonAction() {
		dataPanel.getRefreshBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				((CustomTableModel<Employee>) dataPanel.getTable().getModel()).refresh();
				dataPanel.getTable().updateUI();
			}
		});
	}

	@Override
	protected void addAddButtonAction() {
		dataPanel.getAddBtn().setText("Hire Employee");
		dataPanel.getAddBtn().addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				AddEmployeeDialog dialog = new AddEmployeeDialog();
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@SuppressWarnings("unchecked")
					@Override
					public void windowClosed(WindowEvent e) {
						if (!dialog.isOk())
							return;
						ControllerActionStatus status = ((CustomTableModel<Employee>) dataPanel.getTable().getModel())
								.add(dialog.getEmployee());
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Employee hired successfully",
									"Success", JOptionPane.INFORMATION_MESSAGE);
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(parent.getContentPane(),
									"User with this username already exists", "Error", JOptionPane.ERROR_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(parent.getContentPane(), "An error occured", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						}
						dataPanel.getTable().updateUI();
					}
				});

			}
		});
	}

	@Override
	protected void addEditButtonAction() {
		dataPanel.getEditBtn().setText("Edit Employee");
		dataPanel.getEditBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {

				CustomTableModel<Employee> customTableModel = (CustomTableModel<Employee>) dataPanel.getTable()
						.getModel();
				Employee employee = (Employee) customTableModel.get(dataPanel.getTable().getSelectedRow());
				EditEmployeeDialog dialog = new EditEmployeeDialog(employee);
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@SuppressWarnings("rawtypes")
					@Override
					public void windowClosed(WindowEvent e) {
						if (!dialog.isOk())
							return;
						ControllerActionStatus status = ((CustomTableModel) dataPanel.getTable().getModel())
								.edit(employee);
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Employee updated successfully",
									"Success", JOptionPane.INFORMATION_MESSAGE);
							break;
						case NO_RECORD:
							JOptionPane.showMessageDialog(parent.getContentPane(), "Employee not found", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						case DUPLICATE_INDEX:
							JOptionPane.showMessageDialog(parent.getContentPane(),
									"User with this username already exists", "Error", JOptionPane.ERROR_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(parent.getContentPane(), "An error occured", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						}
						dataPanel.getTable().updateUI();
					}
				});

			}
		});
	}

	@Override
	protected void addRemoveButtonAction() {
		dataPanel.getDeleteBtn().setText("Fire Employee");
		dataPanel.getDeleteBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				CustomTableModel<Employee> customTableModel = (CustomTableModel<Employee>) dataPanel.getTable()
						.getModel();
				int res = JOptionPane.showConfirmDialog(parent.getContentPane(),
						"Are you sure you want to delete this user?", "Delete user", JOptionPane.YES_NO_OPTION,
						JOptionPane.QUESTION_MESSAGE);
				if (res != JOptionPane.YES_OPTION)
					return;
				ControllerActionStatus status = customTableModel.remove(dataPanel.getTable().getSelectedRow());
				switch (status) {
				case SUCCESS:
					JOptionPane.showMessageDialog(parent.getContentPane(), "Employee fired successfully", "Success",
							JOptionPane.INFORMATION_MESSAGE);
					break;
				case NO_RECORD:
					JOptionPane.showMessageDialog(parent.getContentPane(), "Employee not found", "Error",
							JOptionPane.ERROR_MESSAGE);
					break;
				default:
					JOptionPane.showMessageDialog(parent.getContentPane(), "An error occured", "Error",
							JOptionPane.ERROR_MESSAGE);
					break;
				}
				dataPanel.getTable().updateUI();
			}
		});
	}
}
