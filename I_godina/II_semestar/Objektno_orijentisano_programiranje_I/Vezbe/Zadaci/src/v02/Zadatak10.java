package v02;

public class Zadatak10 {

	public static void main(String[] args) {
		int n = 3;
		int a[][] = new int[n][n];
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				a[i][j] = i*n+j+1;
			}
		}
		System.out.println("Pre");
		for(int i = 0; i < a.length; i++) {
			for(int j = 0; j < a[i].length; j++) {
				System.out.printf("\t%-3d", a[i][j]);
			}
			System.out.println();
		}

		for(int i = 0; i < n; i++) {
			int t = a[i][i];
			a[i][i] = a[i][n-i-1];
			a[i][n-i-1] = t;
		}
		
		System.out.println("Posle");
		for(int i = 0; i < a.length; i++) {
			for(int j = 0; j < a[i].length; j++) {
				System.out.printf("\t%-3d", a[i][j]);
			}
			System.out.println();
		}
	}

}
