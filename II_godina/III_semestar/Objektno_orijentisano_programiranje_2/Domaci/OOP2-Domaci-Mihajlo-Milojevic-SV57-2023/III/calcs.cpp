#include "calcs.h"
#include <iostream>

void calcShort()
{
	short val1, val2;
	std::cout << "Input first number: ";
	std::cin >> val1;
	std::cout << "Input second number: ";
	std::cin >> val2;
	std::cout << "Sum: " << val1 + val2 << std::endl;
	std::cout << "Difference: " << val1 - val2 << std::endl;
	std::cout << "Product: " << val1 * val2 << std::endl;
	if (val2 != 0)
		std::cout << "Quotient: " << val1 / val2 << std::endl;
	else
		std::cout << "Cannot divide by zero." << std::endl;
	std::cout << "Min: " << (val1 < val2 ? val1 : val2) << std::endl;
}

void calcInt()
{
	int val1, val2;
	std::cout << "Input first number: ";
	std::cin >> val1;
	std::cout << "Input second number: ";
	std::cin >> val2;
	std::cout << "Sum: " << val1 + val2 << std::endl;
	std::cout << "Difference: " << val1 - val2 << std::endl;
	std::cout << "Product: " << val1 * val2 << std::endl;
	if (val2 != 0)
		std::cout << "Quotient: " << val1 / val2 << std::endl;
	else
		std::cout << "Cannot divide by zero." << std::endl;
	std::cout << "Min: " << (val1 < val2 ? val1 : val2) << std::endl;
}

void calcDouble()
{
	double val1, val2;
	std::cout << "Input first number: ";
	std::cin >> val1;
	std::cout << "Input second number: ";
	std::cin >> val2;
	std::cout << "Sum: " << val1 + val2 << std::endl;
	std::cout << "Difference: " << val1 - val2 << std::endl;
	std::cout << "Product: " << val1 * val2 << std::endl;
	if (val2 != 0)
		std::cout << "Quotient: " << val1 / val2 << std::endl;
	else
		std::cout << "Cannot divide by zero." << std::endl;
	std::cout << "Min: " << (val1 < val2 ? val1 : val2) << std::endl;
}
