package utils;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class CSVDateParser {
	private static DateTimeFormatter formater = DateTimeFormatter.ofPattern("uuuu-MM-dd");
	public static LocalDate parseString(String date) {
		try {
			if (date == null || date.isEmpty()) {
				return null;
			}
			return LocalDate.parse(date, formater);
		} catch (Exception e) {
			return null;
		}
	}

	public static String formatDate(LocalDate date) {
		if (date == null) {
			return "";
		}
		return date.format(formater);
	}
}
