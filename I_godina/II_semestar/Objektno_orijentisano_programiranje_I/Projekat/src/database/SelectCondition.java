package database;

import models.Model;

public interface SelectCondition {
	public boolean check(Model row);
}
