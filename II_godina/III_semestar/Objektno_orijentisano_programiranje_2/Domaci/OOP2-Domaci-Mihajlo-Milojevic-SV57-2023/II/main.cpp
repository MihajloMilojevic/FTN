#include <iostream>

#include "converter.h"

int main()
{
	try
	{
		// Test the conversion functions
		// Valid test cases

		// Test the dec to hex conversion
		std::cout << "Test 1: " << uintToHex(0) << std::endl;
		std::cout << "Test 2: " << uintToHex(1) << std::endl;
		std::cout << "Test 3: " << uintToHex(15) << std::endl;
		std::cout << "Test 4: " << uintToHex(16) << std::endl;
		std::cout << "Test 5: " << uintToHex(255) << std::endl;
		std::cout << "Test 6: " << uintToHex(256) << std::endl;
		std::cout << "Test 7: " << uintToHex(65535) << std::endl;
		std::cout << "Test 8: " << uintToHex(65536) << std::endl;
		std::cout << "Test 9: " << uintToHex(4294967295) << std::endl;
		// Test the addition function
		std::cout << "Test 10: " << addHex("0", "0") << std::endl;
		std::cout << "Test 11: " << addHex("1", "1") << std::endl;
		std::cout << "Test 12: " << addHex("F", "1") << std::endl;
		std::cout << "Test 13: " << addHex("F", "F") << std::endl;
		std::cout << "Test 14: " << addHex("FF", "1") << std::endl;
		std::cout << "Test 15: " << addHex("FF", "FF") << std::endl;
		std::cout << "Test 16: " << addHex("FFFF", "1") << std::endl;
		std::cout << "Test 17: " << addHex("FFFF", "FFFF") << std::endl;
		std::cout << "Test 18: " << addHex("2F8", "359A") << std::endl;
		// test the hex to dec conversion
		std::cout << "Test 19: " << hexToUint("0") << std::endl;
		std::cout << "Test 20: " << hexToUint("1") << std::endl;
		std::cout << "Test 21: " << hexToUint("F") << std::endl;
		std::cout << "Test 22: " << hexToUint("10") << std::endl;
		std::cout << "Test 23: " << hexToUint("FF") << std::endl;
		std::cout << "Test 24: " << hexToUint("100") << std::endl;
		std::cout << "Test 25: " << hexToUint("9A8") << std::endl;

		// test the invalid cases
		// Test the dec to hex conversion
		std::cout << "Test 26: " << uintToHex(4294967296) << std::endl;
		// Test the addition function
		std::cout << "Test 27: " << addHex("FFFFFFFF", "FFFFFFFF") << std::endl;
		// test the hex to dec conversion
		std::cout << "Test 28: " << hexToUint("A58F6B308A") << std::endl;

		// Test the empty string
		std::cout << "Test 29: " << hexToUint("") << std::endl;
		std::cout << "Test 30: " << addHex("", "1") << std::endl;

		return 0;

	}
	catch (const std::exception& e)
	{
		std::cerr << e.what() << std::endl;
		return 1;
	}
}
