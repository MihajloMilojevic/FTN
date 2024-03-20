package v02;

public class Zadatak4 {

	public static void main(String[] args) {
		int n = 10;
		int b[][] = new int[n][];
		for(int i = 0; i < b.length; i++) {
			b[i] = new int[i+1];
			int before = i*(i+1)/2;
			for(int j = 0; j < b[i].length; j++) {
				b[i][j] = before+j+1;
			}
		}
		for(int i = 0; i < b.length; i++) {
			for(int j = 0; j < b[i].length; j++) {
				System.out.printf("%5d ", b[i][j]);
			}
			System.out.println();
		}
	}

}
