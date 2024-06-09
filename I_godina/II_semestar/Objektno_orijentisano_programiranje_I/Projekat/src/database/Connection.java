package database;

import java.io.File;
import java.io.IOException;
import java.text.ParseException;

import exceptions.NoElementException;
import models.Model;

public class Connection<T extends Model, U extends Model> {
	private Table<T> table1;
	private Table<U> table2;
	private File file;
	private ConnectionActions<T, U> connectionActions;

	public Connection(Table<T> table1, Table<U> table2, File file, ConnectionActions<T, U> connectionActions) {
		this.table1 = table1;
		this.table2 = table2;
		this.file = file;
		if(!file.exists()) {
			try {
				File parent = file.getParentFile();
				if(parent != null && !parent.exists()) {
					parent.mkdirs();
				}
				file.createNewFile();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		this.connectionActions = connectionActions;
	}

	public void load() throws IOException, ParseException, NoElementException {
        connectionActions.load(table1, table2, file.getAbsolutePath());
    }

	public void save() throws IOException, ParseException {
        connectionActions.save(table1, table2, file.getAbsolutePath());
    }
}