package test;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class TestMain {

	static List<String[]> dataLines = new ArrayList<>();
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			givenDataArray_whenConvertToCSV_thenOutputCreated();
			System.out.println("KRAJ");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	public static void givenDataArray_whenConvertToCSV_thenOutputCreated() throws IOException {
	    File csvOutputFile = new File("test.csv");
	    PrintWriter pw = new PrintWriter(csvOutputFile);
	    pw.println("Hello;World;Mi;Name;Es;Mihajlo;55;3.5");
	    pw.println("Hello;World;Mi;Name;Es;Mihajlo;55;3.5");
	    pw.println("Hello;World;Mi;Name;Es;Mihajlo;55;3.5");
	    pw.close();
	}
}
