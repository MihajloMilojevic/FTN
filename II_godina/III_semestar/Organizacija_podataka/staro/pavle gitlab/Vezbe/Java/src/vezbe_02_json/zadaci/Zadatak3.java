package vezbe_02_json.zadaci;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.MapperFeature;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Zadatak3 {

	private static HashMap<String, List<Tweet>> userTweets;
	private static HashMap<String, Integer> words;
	static int positive = 0, negative = 0;
	public static void main(String[] args) throws JsonParseException, JsonMappingException, IOException {
		userTweets = new HashMap<String, List<Tweet>>();
		words = new HashMap<String, Integer>();
		readWords();
		readTweets();
		getUserFeel();
		System.out.println("Positive: " + positive + " negative: " + negative);
	}

	private static void getUserFeel() {
		for(String user: userTweets.keySet()) {
			int total = 0;
			for (Tweet tweet : userTweets.get(user)) {
				total += tweet.getFeel();
			}
			if(total != 0)
				System.out.println("User: " + user + " total feel: " + total);
		}
		
	}

	private static void readWords() throws IOException {
		File fajl = new File("resources/vezbe_02_json/AFINN-111.txt");
		BufferedReader citac = new BufferedReader(new InputStreamReader(new FileInputStream(fajl), "utf-8"));
		String linija;
		while ((linija = citac.readLine()) != null) {
			String[] reci = linija.split("\\t");
			words.putIfAbsent(reci[0], Integer.valueOf(reci[1]));
		}
		citac.close();
	}

	private static void readTweets() throws JsonParseException, JsonMappingException, IOException {
		ObjectMapper mapper = new ObjectMapper();
		mapper.configure(MapperFeature.ACCEPT_CASE_INSENSITIVE_PROPERTIES, true);
		File fajl = new File("resources/vezbe_02_json/output_1.txt");
		BufferedReader citac = new BufferedReader(new InputStreamReader(new FileInputStream(fajl), "utf-8"));
		String linija;
		while ((linija = citac.readLine()) != null) {
			try {
				Tweet tweets = mapper.readValue(linija, Tweet.class);
				calculate(tweets);
				userTweets.putIfAbsent(tweets.getId_str(), new ArrayList<Tweet>());
				userTweets.get(tweets.getId_str()).add(tweets);
				System.out.println(tweets);
			} catch(Exception e) {
			}

		}
		citac.close();

	}

	private static void calculate(Tweet tweets) {
		int total = 0;
		for(String rec: tweets.getText().split("\\s+")) {
			if(words.containsKey(rec))
				total += words.get(rec);
		}
		tweets.setFeel(total);
		if(total > 0)
			positive++;
		else
			negative++;
	}

}
