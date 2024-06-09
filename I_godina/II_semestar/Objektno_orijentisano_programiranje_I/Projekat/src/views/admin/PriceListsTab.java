package views.admin;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.time.LocalDate;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.table.TableColumnModel;

import controllers.ControllerActionStatus;
import controllers.PriceListController;
import models.PriceList;
import utils.CustomTableModel;
import utils.Pair;
import views.components.DataPanel;
import views.components.Tab;
import views.dialogs.price_lists.AddPriceListDialog;
import views.dialogs.price_lists.EditPriceListDialog;

public class PriceListsTab extends Tab<PriceList> {

	public PriceListsTab(JFrame parent) {
		super(parent);
	}

	@Override
	protected void addColumns() {
		columns.add(new Pair<String, String>("ID", "id"));
		columns.add(new Pair<String, String>("Start Date", "startDate"));
		columns.add(new Pair<String, String>("End Date", "endDate"));
	}

	@Override
	protected void addModel() {
		model = new CustomTableModel<PriceList>(this, columns, new CustomTableModel.TableDataManiplations<PriceList>() {

			@Override
			public ArrayList<PriceList> getData() {
				ArrayList<PriceList> prices = PriceListController.getPrices();
				prices.sort((p1, p2) -> p1.getStartDate().compareTo(p2.getStartDate()));
				return prices;
			}

			@Override
			public ControllerActionStatus add(PriceList model) {
				return PriceListController.addPriceList(model);
			}

			@Override
			public ControllerActionStatus edit(PriceList model) {
				return PriceListController.updatePriceList(model);
			}

			@Override
			public ControllerActionStatus remove(PriceList model) {
				return PriceListController.removePriceList(model);
			}

		}, new PriceList(LocalDate.now(), LocalDate.now()));
	}

	@Override
	protected void addDataPanel() {
		dataPanel = new DataPanel<PriceList>(model);
	}

	@Override
	protected void setColumnsSize() {
		TableColumnModel columnModel = dataPanel.getTable().getColumnModel();
		columnModel.getColumn(0).setMinWidth(150);
		columnModel.getColumn(1).setMinWidth(200);
		columnModel.getColumn(2).setMinWidth(200);
	}

	@Override
	protected void addRefreshButtonAction() {
		dataPanel.getRefreshBtn().addActionListener(new ActionListener() {
			@SuppressWarnings("unchecked")
			public void actionPerformed(ActionEvent e) {
				((CustomTableModel<PriceList>) dataPanel.getTable().getModel()).refresh();
				dataPanel.getTable().updateUI();
			}
		});
	}

	@Override
	protected void addAddButtonAction() {
		dataPanel.getAddBtn().setText("Add Price List");
		dataPanel.getAddBtn().addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				AddPriceListDialog dialog = new AddPriceListDialog();
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@Override
					public void windowClosed(WindowEvent windowEvent) {
						if (!dialog.isOk()) return;
						PriceList price = dialog.getPriceList();
						ControllerActionStatus status = model.add(price);
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(null, "Price list added successfully", "Success", JOptionPane.INFORMATION_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(null, "Unable to add the price list", "Error", JOptionPane.ERROR_MESSAGE);
							break;
						}
					}
				});
				dataPanel.getTable().updateUI();
			}
		});
	}

	@Override
	protected void addEditButtonAction() {
		dataPanel.getEditBtn().setText("Edit Price List");
		dataPanel.getEditBtn().addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				PriceList price = model.get(dataPanel.getTable().getSelectedRow());
				EditPriceListDialog dialog = new EditPriceListDialog(price);
				dialog.setVisible(true);
				dialog.addWindowListener(new WindowAdapter() {
					@Override
					public void windowClosed(WindowEvent windowEvent) {
						if (!dialog.isOk())
							return;
						PriceList newPrice = dialog.getPriceList();
						ControllerActionStatus status = model.edit(newPrice);
						switch (status) {
						case SUCCESS:
							JOptionPane.showMessageDialog(null, "Price list updated successfully", "Success",
									JOptionPane.INFORMATION_MESSAGE);
							break;
						default:
							JOptionPane.showMessageDialog(null, "Unable to update the price list", "Error",
									JOptionPane.ERROR_MESSAGE);
							break;
						}
					}
				});
				dataPanel.getTable().updateUI();
			}
		});
	}

	@Override
	protected void addRemoveButtonAction() {
		dataPanel.getDeleteBtn().setVisible(false);
	}

}
