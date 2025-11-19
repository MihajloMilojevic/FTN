
#include <iostream>
#include "fib.h"

int main()
{
	int lastInt = 0;
	long lastLong = 0;
	long long lastLongLong = 0;
	int countInt = fib(lastInt);
	int countLong = fib(lastLong);
	int countLongLong = fib(lastLongLong);
	std::cout << "Int: " << sizeof(int) <<"B n: " << countInt << " fib(n): " << lastInt << std::endl;
	std::cout << "Long: " << sizeof(long) << "B n: " << countLong << " fib(n): " << lastLong << std::endl;
	std::cout << "Long Long: " << sizeof(long long) << "B n: " << countLongLong << " fib(n): " << lastLongLong << std::endl;
	return 0;
}