#include <stdio.h>
#include <float.h>

#include "tbb\tbb.h"
#include "tbb\parallel_reduce.h"

using namespace tbb;

float Foo(float a) {
	return a;
}

   //TODO: Create a class called MinIndexFoo with constructors, operator() and the join method


   //TODO: Create a function for parallel minimum

int main () {
	float a[100];

	for (int i=0; i<100; ++i) {
		a[i] = -i;
	}
	
	long ind = ParallelMinIndexFoo(a, 100);
	printf("%d\n", ind);

	return 0;
}