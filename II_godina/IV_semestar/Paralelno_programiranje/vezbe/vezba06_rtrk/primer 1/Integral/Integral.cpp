#include <iostream>
#include <vector>
#include <math.h>

#include "tbb/task_group.h"
#include <tbb/tick_count.h>


using namespace std;
using namespace tbb;

#define LOWER 0
#define UPPER 3.14
double delta = 0.000001;
double cutOff = 0.001;

//wolfram alfa formula: (integrate exp(-1/x) cos(x) from x = 0 to 3.14)
//result -0.495667

double calculation(double x);
double incremental(double lowerBound, double upperBound);
double serial_integration(double lowerBound, double upperBound);
double parallel_integration(double lowerBound, double upperBound);
void run();


int main() {
	double deltas[] = { 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001 };
	for (double d : deltas) {
		delta = d;
		cout << "Delta: " << delta << endl;
		run();
		cout << "----------------------------------------" << endl;
	}
}

void run() {
	double serialResult = 0;
	double parallelResult = 0;
	cout << "Serial integral function..." << endl;
	tick_count startTime = tick_count::now();
	serialResult = serial_integration(LOWER, UPPER);
	tick_count endTime = tick_count::now();
	cout << "Serial result: " << serialResult << endl;
	cout << "Calcualtions took " << (endTime - startTime).seconds() << " seconds." << endl << endl;

	cout << "Paralel integral function..." << endl;
	startTime = tick_count::now();
	parallelResult = parallel_integration(LOWER, UPPER);
	endTime = tick_count::now();
	cout << "Paralel result: " << parallelResult << endl;
	cout << "Calcualtions took " << (endTime - startTime).seconds() << " seconds." << endl;

}

double calculation(double x) {
    return exp(-1 / x) * delta * cos(x);
}

double incremental(double lowerBound, double upperBound) {
	double res = 0;
	for (double iter = lowerBound; iter <= upperBound; iter += delta)
	{
		res += calculation(iter);
	}
	return res;
}

double serial_integration(double lowerBound, double upperBound) {
	if (upperBound - lowerBound <= cutOff) {
		return incremental(lowerBound, upperBound);
	}
	double mid = (lowerBound + upperBound) / 2.0;
	double leftResult = serial_integration(lowerBound, mid);
	double rightResult = serial_integration(mid, upperBound);
	return leftResult + rightResult;
}

double parallel_integration(double lowerBound, double upperBound) {
	if (upperBound - lowerBound <= cutOff) {
		return incremental(lowerBound, upperBound);
	}
	double mid = (lowerBound + upperBound) / 2;
	double left = 0.0, right = 0.0;

	task_group g;
	g.run([&] {
		left = parallel_integration(lowerBound, mid);
		});
	g.run([&] {
		right = parallel_integration(mid, upperBound);
		});
	g.wait();

	return left + right;
	
}


//Delta: 0.1
//Serial integral function...
//Serial result : -64.6213
//Calcualtions took 0.0001253 seconds.
//
//Paralel integral function...
//Paralel result : -64.6213
//Calcualtions took 0.0021266 seconds.
//----------------------------------------
//Delta : 0.01
//Serial integral function...
//Serial result : -6.46213
//Calcualtions took 0.0001942 seconds.
//
//Paralel integral function...
//Paralel result : -6.46213
//Calcualtions took 0.0026813 seconds.
//----------------------------------------
//Delta : 0.001
//Serial integral function...
//Serial result : -0.646213
//Calcualtions took 0.0001146 seconds.
//
//Paralel integral function...
//Paralel result : -0.646213
//Calcualtions took 0.0003837 seconds.
//----------------------------------------
//Delta : 0.0001
//Serial integral function...
//Serial result : -0.517236
//Calcualtions took 0.0003706 seconds.
//
//Paralel integral function...
//Paralel result : -0.517236
//Calcualtions took 0.0003419 seconds.
//----------------------------------------
//Delta : 1e-05
//Serial integral function...
//Serial result : -0.497862
//Calcualtions took 0.0050066 seconds.
//
//Paralel integral function...
//Paralel result : -0.497862
//Calcualtions took 0.0009283 seconds.
//----------------------------------------
//Delta : 1e-06
//Serial integral function...
//Serial result : -0.495924
//Calcualtions took 0.0341286 seconds.
//
//Paralel integral function...
//Paralel result : -0.495924
//Calcualtions took 0.0052721 seconds.
//----------------------------------------
//Delta : 1e-07
//Serial integral function...
//Serial result : -0.49573
//Calcualtions took 0.36154 seconds.
//
//Paralel integral function...
//Paralel result : -0.49573
//Calcualtions took 0.0500752 seconds.
//----------------------------------------