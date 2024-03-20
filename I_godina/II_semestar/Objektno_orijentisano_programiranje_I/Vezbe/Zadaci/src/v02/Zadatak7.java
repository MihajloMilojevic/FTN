package v02;

public class Zadatak7 {

	public static void main(String[] args) {
		int A[] = { -10, 3, 16, 1, 4, -2};
		int min = A[0], max=A[0], S = 0;
		for(int num: A) {
			min = Math.min(min, num);
			max = Math.max(max, num);
			S += num;
		}
		System.out.printf("Najmanji element je %d, najveci %d, a srednja vrednost je %.2f", min, max, (double)S/A.length);
	}

}
