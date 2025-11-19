#include "zadatak2.h"
#include "input_helper.h"
#include <iostream>



void zadatak2() {
	int n = readInt("Unesite broj elemenata niza: ", true, false);
	int* arr = readIntArray(n);
	std::cout << "Unet je niz:\n";
	for (int i = 0; i < n; ++i) {
		std::cout << "arr[" << i << "] = " << arr[i] << std::endl;
	}
	std::cout << "Elementi niza na parnim pozicijama:\n";
	for (int i = 0; i < n; i += 2) {
		std::cout << "arr[" << i << "] = " << arr[i] << std::endl;
	}
	std::cout << "Elementi niza na neparnim pozicijama:\n";
	for (int i = 1; i < n; i += 2) {
		std::cout << "arr[" << i << "] = " << arr[i] << std::endl;
	}
	delete[] arr;
}