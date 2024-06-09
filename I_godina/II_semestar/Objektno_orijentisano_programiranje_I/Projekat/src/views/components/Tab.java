package views.components;

import java.util.ArrayList;

import javax.swing.JFrame;

import models.Model;
import utils.CustomTableModel;
import utils.Pair;

public abstract class Tab<T extends Model> {
	protected ArrayList<Tab<?>> tabs;
	protected ArrayList<Pair<String, String>> columns;
	protected CustomTableModel<T> model;
	protected DataPanel<T> dataPanel;
	protected JFrame parent;
	
	public Tab(JFrame parent) {
		this.parent = parent;
		tabs = new ArrayList<Tab<?>>();
        columns = new ArrayList<Pair<String, String>>();
        addComponents();
	}
	
	
	/* ********************** TEMPLATE PATTERN ********************** */
	
	protected abstract void addColumns();
	protected abstract void addModel();
	protected abstract void addDataPanel();
	protected abstract void setColumnsSize();
	protected abstract void addRefreshButtonAction();
	protected abstract void addAddButtonAction();
	protected abstract void addEditButtonAction();
	protected abstract void addRemoveButtonAction();
	protected void addNewButton() {}

	public void addComponents() {
		addColumns();
		addModel();
		addDataPanel();
		setColumnsSize();
		addRefreshButtonAction();
		addAddButtonAction();
		addEditButtonAction();
		addRemoveButtonAction();
		addNewButton();
	}
	
	/* ********************** OBSEVER PATTERN ********************** */
	
	public void addTab(Tab<?> tab) {
		tabs.add(tab);
	}
	
	public void removeTab(Tab<?> tab) {
		tabs.remove(tab);
	}
	
	public ArrayList<Tab<?>> getTabs() {
		return tabs;
	}
	
	public void setTabs(ArrayList<Tab<?>> tabs) {
		this.tabs = tabs;
	}
	
	public void notifyTabs() {
		for (Tab<?> tab : tabs) {
			tab.getModel().refresh();
		}
	}
	
	/* ********************* GETTERS AND SETTERS ********************* */
	
	/**
	 * @return the columns
	 */
	public ArrayList<Pair<String, String>> getColumns() {
		return columns;
	}
	/**
	 * @param columns the columns to set
	 */
	public void setColumns(ArrayList<Pair<String, String>> columns) {
		this.columns = columns;
	}
	/**
	 * @return the model
	 */
	public CustomTableModel<T> getModel() {
		return model;
	}
	/**
	 * @param model the model to set
	 */
	public void setModel(CustomTableModel<T> model) {
		this.model = model;
	}
	/**
	 * @return the dataPanel
	 */
	public DataPanel<T> getDataPanel() {
		return dataPanel;
	}
	/**
	 * @param dataPanel the dataPanel to set
	 */
	public void setDataPanel(DataPanel<T> dataPanel) {
		this.dataPanel = dataPanel;
	}
}
