package v02;

public class Zadatak9 {

	public static void main(String[] args) {
		int n = 7, m = 5;
		int mat[][] = new int[n][m];
		for(int i = 0; i < mat.length; i++) {
			for(int j = 0; j < mat[i].length; j++) {
				mat[i][j] = i+j;
			}
		}
		int sum = 0;
		System.out.println("Matrica je oblika:");
		for(int i = 0; i < mat.length; i++) {
			for(int j = 0; j < mat[i].length; j++) {
				System.out.printf("\t%-3d", mat[i][j]);
				if(i == j) {
					sum += mat[i][j];
				}
			}
			System.out.println();
		}
		System.out.printf("Zbir elemenata na glavnoj dijagonali je: %d", sum);
	}

}
