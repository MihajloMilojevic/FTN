#include "converter.h"
#include <vector>
#include <stdexcept>

// This is a string that contains all the hex digits in order such that 
// its index corresponds to the value of the digit
const std::string HEX_DIGITS = "0123456789ABCDEF";

unsigned int findHexDigit(char digit) {
	for (unsigned int i = 0; i < HEX_DIGITS.length(); i++)
		if (HEX_DIGITS[i] == digit)
			return i;
	// the digit is not found
	return -1;
}

char findHexChar(int digit)
{
	// Check if the digit is in the valid range
	if (digit >= 0 && digit < HEX_DIGITS.length())
		return HEX_DIGITS[digit];
	// Digit not found
	return 0;
}

std::string uintToHex(unsigned int value)
{
	// special case for 0
	if (value == 0)	
		return "0";
	std::vector<char> hexDigits;
	// convert to hex, digit by digit
	while (value != 0)
	{
		hexDigits.push_back(findHexChar(value % 16));
		value /= 16;
	}
	// Combining the digits in reverse order
	// Note: This is not the most efficient way to build a string, but we cannot use
	// more advanced techniques like std::stringstream
	std::string result = "";
	for (int i = hexDigits.size() - 1; i >= 0; i--)
	{
		result += hexDigits[i];
	}
	return result;
}

std::string addHex(const std::string& firstValue, const std::string& secondValue) {
	unsigned int first = hexToUint(firstValue);
	unsigned int second = hexToUint(secondValue);
	unsigned int result = first + second;
	if (result < first || result < second)
		throw std::overflow_error("Addition overflow: Adding " + firstValue + " and " +
			secondValue + " results in a value that cannot be stored in type unsigned int"
		);
	return uintToHex(result);
}
unsigned int hexToUint(const std::string& value) {
	if (value.length() == 0)
		throw std::invalid_argument("Empty string is not a valid hex value");
	unsigned int result = 0;		// acumulator for the result
	unsigned int power = 1;			// power of 16

	// the next two variables are used to detect overflow
	unsigned int previousPower = 1;	// power of 16 in the previous iteration
	unsigned int previousResult = 0;	// result in the previous iteration

	for (int i = value.length() - 1; i >= 0; i--)
	{
		unsigned int index = findHexDigit(value[i]);
		if (index == -1)
			throw std::invalid_argument(value[i] + " is not a valid hex digit");	// invalid hex digit
		previousResult = result;
		previousPower = power;
		result += index * power;
		power *= 16;
		// Check for overflow
		if (result < previousResult)
			throw std::overflow_error("Result overflow: the value of the " + value + 
				" cannot be stored in type unsigned int");
		if (power < previousPower) 
			throw std::overflow_error("Power overflow: the power of 16 required to calculate " + 
				value + " cannot be stored in type unsigned int"
			);
	}
	return result;
}