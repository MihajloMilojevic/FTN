package database;

import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import app.AppSettings;
import exceptions.DuplicateIndexException;
import exceptions.NoElementException;
import models.Model;
import utils.FileChecker;

public class Table<T extends Model> {
	private String settingName;
	private HashMap<String, T> rows;
	public HashMap<String, HashMap<String, T>> indecies;
	private T object;
	private CustomTableParser customParser;
	
	public Table(String settingName, T object) {
		this.settingName = settingName;
		this.object = object;
		this.rows = new HashMap<String, T>();
		this.indecies = new HashMap<String, HashMap<String, T>>();
		
		addIndex("id");
	}

	public Table(String settingName, CustomTableParser customParser) {
		this(settingName, (T)null);
		this.customParser = customParser;
		
	}
	public void addIndex(String indexName) {
		HashMap<String, T> newIndex = new HashMap<String, T>();
		for (T row : this.rows.values()) {
			if(row.isDeleted()) continue;
			newIndex.put(String.valueOf(row.get(indexName)), row);
		}
		this.indecies.put(indexName, newIndex);
	}
	public void removeIndex(String indexName) {
		this.indecies.remove(indexName);
	}

	@SuppressWarnings("unchecked")
	public ArrayList<T> getRows() {
		ArrayList<T> result = new ArrayList<T>();
		for (T row : this.rows.values()) {
        	try {
    			result.add((T)row.clone());
			} catch (CloneNotSupportedException e) {
				System.err.println(e.getMessage());
				e.printStackTrace();
			}
        }
		return result;
	}
	public void insert(T row) throws DuplicateIndexException {
		if(!isUnique(row)) throw new DuplicateIndexException("Duplicate key");
		this.rows.put(row.getId(), row);
		if(row.isDeleted()) return;
        for (String indexName : this.indecies.keySet()) {
            this.indecies.get(indexName).put(row.get(indexName).toString(), row);
        }
	}
	public void delete(T row) {
		T dbRow = this.rows.get(row.getId());
		if(dbRow != null) dbRow.delete();
		regenerateIndecies();
	}
	public void delete(SelectCondition condition) {
		for (T row : this.rows.values()) {
			if (condition.check(row)) {
				T dbRow = this.rows.get(row.getId());
				if(dbRow != null) dbRow.delete();
			}
		}
		regenerateIndecies();
	}

	public void deleteById(String id) {
		T dbRow = this.rows.get(id);
		if(dbRow != null) dbRow.delete();
		regenerateIndecies();
	}
	public void deleteByIndex(String indexName, String indexValue) {
		if(!this.indecies.containsKey(indexName)) return;
		T row = this.indecies.get(indexName).get(indexValue);
		if(row == null) return;
		T dbRow = this.rows.get(row.getId());
		if(dbRow != null) dbRow.delete();
		regenerateIndecies();
	}

 	@SuppressWarnings("unchecked")
	public ArrayList<T> select(SelectCondition condition) {
		ArrayList<T> result = new ArrayList<T>();
		for (T row : this.rows.values()) {
            if (condition.check(row)) {
            	try {
					result.add((T) row.clone());
				} catch (CloneNotSupportedException e) {
					System.err.println(e.getMessage());
					e.printStackTrace();
				}
            }
        }
		return result;
	}
 	
 	@SuppressWarnings("unchecked")
	public T selectById(String id) {
		T row = this.rows.get(id);
		if (row == null)
			return null;
		try {
			return (T) row.clone();
		} catch (CloneNotSupportedException e) {
			System.err.println(e.getMessage());
			e.printStackTrace();
			return null;
		}
 	}


	@SuppressWarnings("unchecked")
	public T selectByIndex(String indexName, String indexValue) {
		if (!this.indecies.containsKey(indexName)) return null;
		T row = this.indecies.get(indexName).get(indexValue);
		if (row == null)
			return null;
		try {
			return (T)row.clone();
		} catch (CloneNotSupportedException e) {
			System.err.println(e.getMessage());
			e.printStackTrace();
			return null;
		}
	}
	
	public void update(T row, boolean checkIfUnique) throws NoElementException {
		if(row == null) return;
		if(checkIfUnique && isUnique(row)) throw new NoElementException("There is no element to update");
		T dbRow = this.rows.get(row.getId());
		if(dbRow == null) throw new NoElementException("There is no element to update");
		dbRow.update(row);
		regenerateIndecies();
	}
	
	public void update(T row) throws NoElementException {
		update(row, true);
	}

	
	public void clear() {
		this.rows.clear();
		this.indecies.clear();
	}
	
	private void regenerateIndecies() {
		String[] keys = this.indecies.keySet().toArray(String[]::new);
		this.indecies.clear();
		for (String indexName : keys) {
			this.addIndex(indexName);
		}
	}
	
	private boolean isUnique(T model) {
		if(this.rows.containsKey(model.getId()) && !this.rows.get(model.getId()).isDeleted()) return false;
		for (String indexName : this.indecies.keySet()) {
			if (this.indecies.get(indexName).containsKey(model.get(indexName).toString()))
				return false;
		}
		return true;
	}
	
	@SuppressWarnings("unchecked")
	public void load() throws IOException {
		File file = FileChecker.getFile(AppSettings.getInstance().getSetting("database", this.settingName, "./data/" + this.settingName + ".csv"));
		List<String> lines = Files.readAllLines(Path.of(file.getAbsolutePath()), StandardCharsets.UTF_8);
		for (String line : lines) {
			T row;
			try {
				if (this.customParser != null) {
					row = (T) this.customParser.parse(line);
				} else {
					row = (T) ((T) this.object.clone()).fromCSV(line);
				}
				this.insert(row);
			} catch (Exception e) {
				System.err.println(e.getMessage());
				e.printStackTrace();
			}
		}
	}

	public void save() throws IOException {
		File file = FileChecker.getFile(AppSettings.getInstance().getSetting("database", this.settingName, "./data/" + this.settingName + ".csv"));
		List<String> lines = new ArrayList<String>();
		for (T row : this.rows.values()) {
			try {
				if (this.customParser != null) {
					lines.add(this.customParser.stringify(row));
				} else {            	
					lines.add(row.toString());
				}
			} catch (ParseException e) {
				System.err.println(e.getMessage());
				e.printStackTrace();
			}
		}
		Files.write(Path.of(file.getAbsolutePath()), lines, StandardCharsets.UTF_8);
	}

	public String getSettingName() {
		return settingName;
	}
}
