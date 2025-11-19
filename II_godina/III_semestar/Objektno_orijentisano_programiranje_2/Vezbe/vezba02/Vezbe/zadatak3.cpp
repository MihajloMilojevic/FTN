#include "zadatak3.h"
#include "input_helper.h"
#include <iostream>



void zadatak3() {
	int n = readInt("Unesite broj elemenata niza: ", true, false);
	int* arr = readIntArray(n);
	std::cout << "Unet je niz:\n";
	for (int i = 0; i < n; ++i) {
		std::cout << "arr[" << i << "] = " << arr[i] << std::endl;
	}
	int num[2] = { 0, 0 };
	for (int i = 0; i < n; i++) {
		++num[arr[i] % 2];
	}
	std::cout << "U nizu se nalazi " << num[0] << "parnih i " << num[1] << " neparnih elemenata\n";
	delete[] arr;
}