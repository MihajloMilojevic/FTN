#include <iostream>
#include <float.h>

#include "tbb\tbb.h"
#include "tbb\parallel_reduce.h"

using namespace tbb;

float Foo(float a) {
	return a;
}

//TODO: Create a class called MinIndexFoo with constructors, operator() and the join method
class MinIndexFoo {
	public:
		long index = -1;
		float minValue = FLT_MAX;
		float* a = nullptr;
		MinIndexFoo(float *a) :a(a) {}
		MinIndexFoo(MinIndexFoo& other, split) : a(other.a) {}
		void operator()(const blocked_range<long>& r) {
			for (long i = r.begin(); i != r.end(); ++i) {
				if (a[i] < minValue) {
					minValue = a[i];
					index = i;
				}
			}
		}
		void join(const MinIndexFoo& other) {
			if (other.minValue < minValue) {
				minValue = other.minValue;
				index = other.index;
			}
		}
};

//TODO: Create a function for parallel minimum
long ParallelMinIndexFoo(float* a, long n) {
	MinIndexFoo minIndexFoo(a);
	parallel_reduce(
		blocked_range<long>(0, n),
		minIndexFoo
	);
	return minIndexFoo.index;
}

int main() {
	float a[100];

	for (int i = 0; i < 100; ++i) {
		a[i] = -i;
	}

	long ind = ParallelMinIndexFoo(a, 100);
	printf("%d\n", ind);

	return 0;
}