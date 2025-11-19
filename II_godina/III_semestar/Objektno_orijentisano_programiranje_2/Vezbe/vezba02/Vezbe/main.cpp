#include <iostream>
#include "zadatak1.h"
#include "zadatak2.h"
#include "zadatak3.h"
#include "input_helper.h";

int main()
{
	int op = 0;
	bool run = true;
	while (true)
	{
		std::cout << "0. Izlaz\n"
			<< "1. prvi zadatak\n"
			<< "2. drugi zadatak\n"
			<< "3. treci zadatak\n\n";
		op = readInt("Odaberi opciju: ", true, true);
		switch (op)
		{
		case 0:
			run = false;
			break;
		case 1:
			clearConsole();
			zadatak1();
			break;
		case 2:
			clearConsole();
			zadatak2();
			break;
		case 3:
			clearConsole();
			zadatak3();
			break;
		default:
			clearConsole();
			std::cout << "Nevalidna opcija\n\n";
		}
	}
}
