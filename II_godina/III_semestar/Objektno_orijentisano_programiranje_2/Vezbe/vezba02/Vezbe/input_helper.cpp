#include "input_helper.h"
#include <iostream>
#include <sstream>

int readInt(std::string msg, bool positive, bool allowZero) {
	int n = 0;
	while (true)
	{
		std::cout << msg;
		std::cin >> n;
		if (!std::cin) {
			std::cin.clear(); //clear bad input flag
			std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); //discard input
			std::cout << "Morate uneti broj\n";
			continue;
		}
		if (n == 0 && !allowZero) {
			std::cout << "Broj ne moze biti 0\n";
			continue;
		}
		if (n < 0 && positive) {
			std::cout << "Broj mora biti pozitivan ceo broj\n";
			continue;
		}
		return n;
	}
}

int* readIntArray(int n) {
	int* arr = new int[n];
	std::stringstream ss;
	for (int i = 0; i < n; ++i) {
		ss.str("");
		ss << (i + 1);
		arr[i] = readInt("Unesite " + ss.str() + ". element niza: ");
	}
	return arr;
}


std::vector<int> readIntArrayV(int n) {
	std::vector<int> arr(n);
	std::stringstream ss;
	for (int i = 0; i < n; ++i) {
		ss.str("");
		ss << (i + 1);
		arr[i] = readInt("Unesite " + ss.str() + ". element niza: ");
	}
	return arr;
}

void clearConsole() {
	std::cout.clear();
	std::cin.clear();
	#if defined _WIN32
		system("cls");
		//clrscr(); // including header file : conio.h
	#elif defined (__LINUX__) || defined(__gnu_linux__) || defined(__linux__)
		system("clear");
		//std::cout<< u8"\033[2J\033[1;1H"; //Using ANSI Escape Sequences 
	#elif defined (__APPLE__)
		system("clear");
	#endif
}