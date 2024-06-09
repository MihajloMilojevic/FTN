package utils;

import java.util.ArrayList;

import controllers.ControllerActionStatus;
import models.Model;
import views.components.Tab;

public class CustomTableModelWithInitialPrice<T extends Model> extends CustomTableModel<T> {
	/**
	 * 
	 */
	private static final long serialVersionUID = 4555320945612557171L;

	public CustomTableModelWithInitialPrice(ArrayList<Pair<String, String>> columns,
			TableDataManiplations<T> dataManipulations, T model) {
		super(null, columns, dataManipulations, model);
	}

	public CustomTableModelWithInitialPrice(Tab<T> tab, ArrayList<Pair<String, String>> columns,
			TableDataManiplations<T> dataManipulations, T model) {
		super(tab, columns, dataManipulations, model);
	}

	public ControllerActionStatus add(T model, double price) {
		ControllerActionStatus status = ((TableDataManiplationsWithPrice<T>) dataManipulations).add(model, price);
        refresh();
        if (tab != null)
            tab.notifyTabs();
        return status;
	}
	

	public static interface TableDataManiplationsWithPrice<T extends Model> extends TableDataManiplations<T> {
		public ControllerActionStatus add(T model, double price);
	}
}
