package vezbe_01_csv.zadaci;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Zadatak4 {

	private static String resourcePath = "resources/vezbe_01_csv/";
	private static String tableName;
	private static int columnNumber;
	private static Scanner sc = new Scanner(System.in);
	private static String columnNames[];
	private static List<String[]> rows;
	
	public static void main(String[] args) {
		inputParameters();
		inputData();
		writeData();
	}

	private static void inputParameters() {
		System.out.println("Unesite ime tabele: ");
		tableName = sc.nextLine();
		System.out.println("Unesite broj kolona: ");
		columnNumber = sc.nextInt();
		columnNames = new String[columnNumber];
		rows = new ArrayList<String[]>();
		sc.nextLine();
		for (int i = 0; i < columnNumber; i++) {
			System.out.println("Unesite ime kolone " + (i + 1) + ": ");
			columnNames[i] = sc.nextLine();
		}
	}

	private static void inputData() {
		String choice = "";
		String row[];
		while(true) {
			System.out.println("Unesite \"row\" za novi red u tabeli ili \"quit\" za izlazak: ");
			choice = sc.nextLine();
			if(choice.equals("quit"))
				break;
			
			row = new String[columnNumber];
			for (int i = 0; i < columnNumber; i++) {
				System.out.println(columnNames[i] + ":");
				row[i] = sc.nextLine();
			}
			rows.add(row);
		}
	}
	
	private static void writeData() {
		
		PrintWriter writer;
		try {
			writer = new PrintWriter(new OutputStreamWriter(new FileOutputStream(new File(resourcePath + tableName + ".csv")), "utf8"));
			for (String row : columnNames) {
				writer.printf("%s \t", row);
			}
			writer.printf("\n");
			for (String row[] : rows) {
				for (int i = 0; i < row.length; i++) {
					writer.printf("%s", row[i]);
					if(i != row.length - 1)
						writer.printf(",");
					else
						writer.printf("\n");
				}
			}
			writer.close();
			
		} catch (UnsupportedEncodingException | FileNotFoundException e) {
			e.printStackTrace();
		}
		
		
	}
}
