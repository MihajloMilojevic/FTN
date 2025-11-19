#include "zadatak1.h"
#include "input_helper.h"
#include <iostream>



void zadatak1() {
	int n = readInt("Unesite broj elemenata niza: ", true, false);
	int* arr = readIntArray(n);
	std::cout << "Unet je niz:\n";
	for (int i = 0; i < n; ++i) {
		std::cout << "arr[" << i << "] = " << arr[i] << std::endl;
	}
	std::cout << "Niz u obrnutom redosledu:\n";
	for (int i = n - 1; i >= 0; --i) {
		std::cout << "arr[" << i << "] = " << arr[i] << std::endl;
	}
	delete[] arr;
}