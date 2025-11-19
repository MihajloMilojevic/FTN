#include "tbb/blocked_range.h"
#include "tbb/parallel_for.h"
#include <iostream>

using namespace tbb;
using namespace std;

//TODO: Create a class/structure for paralelization

// Note: The input must be padded such that input[-1] and 
// input[n] can be used to calculate the first and last 
// output values.

//TODO: Create a funcion for paralelization

// Sets output[i] to the average of input[i-1], input[i] and input[i+1]
int main() {
	double input[1002], output_serial[1000], output_parallel[1000];
	int test = 0;

	input[0] = 0;
	input[1001] = 0;
	for (int i = 1; i < 1001; i++) {
		input[i] = i * 3.14;
	}

	for (int i = 0; i < 1000; i++) {
		output_serial[i] = (input[i] + input[i + 1] + input[i + 2])*(1 / 3.0f);
	}

	//TODO: Paralell average
	//TODO: Check if the results are equal

	return 0;
}
