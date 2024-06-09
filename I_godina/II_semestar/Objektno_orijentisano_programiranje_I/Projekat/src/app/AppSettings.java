package app;

import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;

public class AppSettings {

	private HashMap<String, HashMap<String, String>> settings;
	private File settingsFile;
	private static final String settingsFilePath = "settings.ini";
	
	private static AppSettings instance;
	
	private AppSettings() {
		settingsFile = new File(settingsFilePath);
		try {
			File parent = settingsFile.getParentFile();
			if(parent != null && parent.isDirectory() && !parent.exists()) {
				parent.mkdirs();
			}
			settingsFile.createNewFile();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		settings = new HashMap<String, HashMap<String, String>>();
		
	}
	
	public void updateSetting(String category, String key, String value) {
		HashMap<String, String> categorySettings = settings.get(category);
		
		if (categorySettings == null) {
			categorySettings = new HashMap<String, String>();
			settings.put(category, categorySettings);
		}
		categorySettings.put(key, value);
	}

	public void load() throws IOException {
		ArrayList<String> lines = (ArrayList<String>) Files.readAllLines(Path.of(settingsFile.getAbsolutePath()));
		HashMap<String, String> currentCategory = new HashMap<String, String>();
		String currentCategoryName = "defualt";
		settings.put(currentCategoryName, currentCategory);
		
		for (String line : lines) {
			line = line.trim();
			if (line.isBlank() || line.startsWith("#")) {
				continue;
			}
			if (line.startsWith("[")) {
				currentCategoryName = line.substring(1, line.length() - 1);
				currentCategory = new HashMap<String, String>();
				settings.put(currentCategoryName, currentCategory);
			} else {
				String[] parts = line.split("=");
				if (parts.length != 2) {
					continue;
				}
				currentCategory.put(parts[0].trim(), parts[1].trim());
			}
		}
	}
	
	public void save() throws IOException {
		ArrayList<String> lines = new ArrayList<String>();
		if(settings.containsKey("defualt")) {
			for (String key : settings.get("defualt").keySet()) {
				lines.add(key + " = " + settings.get("defualt").get(key));
			}
		}
		for (String category : settings.keySet()) {
			if (category.equals("defualt")) {
				continue;
			}
			lines.add("");
			lines.add("[" + category + "]");
			lines.add("");
			HashMap<String, String> categorySettings = settings.get(category);
			for (String key : categorySettings.keySet()) {
				lines.add(key + " = " + categorySettings.get(key));
			}
		}
		Files.write(Path.of(settingsFile.getAbsolutePath()), lines, StandardCharsets.UTF_8);
		System.out.println("Settings saved.");
	}
	
	public void clear() {
		settings.clear();
	}
	
	public String getSetting(String category, String key, String defaultValue) {
		HashMap<String, String> categorySettings = settings.get(category);
		if (categorySettings == null) {
			return defaultValue;
		}
		String value = categorySettings.get(key);
		if (value == null) {
			return defaultValue;
		}
		return value;
	}
	
	public static AppSettings getInstance() {
		if (instance == null) {
			instance = new AppSettings();
		}
		return instance;
	}

	public void test() {
        for (String category : settings.keySet()) {
            System.out.println("[" + category + "]");
            HashMap<String, String> categorySettings = settings.get(category);
            for (String key : categorySettings.keySet()) {
                System.out.println(key + " = " + categorySettings.get(key));
            }
        }
	}
	public int size() {
		return settings.size();
	}

	public ArrayList<String> getCategories() {
		ArrayList<String> categories = new ArrayList<String>();
		if(settings.containsKey("defualt")) categories.add("defualt");
		for (String category : settings.keySet()) {
			if (category.equals("defualt")) {
				continue;
			}
			categories.add(category);
		}
		return categories;
	}

	public HashMap<String, String> getCategory(String category) {
		return settings.get(category);
	}

	public int categorySize(String category) {
		HashMap<String, String> categorySettings = settings.get(category);
		if (categorySettings == null) {
			return 0;
		}
		return categorySettings.size();
	}
}
