package v02;

public class Zadatak3 {

	public static void main(String[] args) {
		int n = 10;
		int arr[] = new int[n];
		arr[0] = 1;
		for(int i = 1; i < n; i++) {
			arr[i] = arr[i-1] + 10;
		}
		System.out.println("Niz je: ");
		for (int item : arr) {
			System.out.printf("%d ", item);
		}
		System.out.println();
	}

}
