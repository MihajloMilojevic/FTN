package database;

import java.text.ParseException;

import models.Model;

public interface CustomTableParser {
	public Model parse(String csvString) throws ParseException;
	public String stringify(Model model) throws ParseException;
}
