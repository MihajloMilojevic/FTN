#include <iostream>

#include "tbb/task_group.h"
#include <tbb/tick_count.h>

#define MAXARRAY 100000
#define WAIT_PERIOD 1
using namespace std;
using namespace tbb;


void quicksort_serial(int arr[], int low, int high);
void quicksort_parallel(int arr[], int low, int high);
void busy_wait();


int main(void) {
	int array[MAXARRAY] = { 0 };
	int array_serial[MAXARRAY] = { 0 };
	int array_parallel[MAXARRAY] = { 0 };
	int i = 0;

	/* load some random values into the array */
	for (i = 0; i < MAXARRAY; i++)
	{
		array[i] = rand() % 10000;
		array_serial[i] = array[i];
		array_parallel[i] = array[i];
	}

	/* print the original array */
	/*cout << "Before quicksort: ";
	for (i = 0; i < MAXARRAY; i++)
	{
		cout << array[i] <<" ";
	}
	cout << endl << endl;*/
	
	/* SERIAL VERSION */
	cout << "Starting serial sort..." << endl;
	tick_count startTime = tick_count::now();
	quicksort_serial(array_serial, 0, (MAXARRAY - 1));
	tick_count endTime = tick_count::now();

	/* print the `quicksorted' array */
	/*cout << "After quicksort serial: ";
	for (i = 0; i < MAXARRAY; i++)
	{
		cout << array_serial[i] << " ";
	}
	cout << endl;*/
	cout << "Serial run time: " << (endTime - startTime).seconds() << " ms." << endl << endl;

	/* PARALLEL VERSION */
	cout << "Starting parallel sort..." << endl;
	startTime = tick_count::now();
	quicksort_parallel(array_parallel, 0, (MAXARRAY - 1));
	endTime = tick_count::now();

	/* print the `quicksorted' array */
	/*
	cout << "After quicksort parallel: ";
	for (i = 0; i < MAXARRAY; i++)
	{
		cout << array_parallel[i] << " ";
	}
	cout << endl;
	*/
	cout << "Parallel run time: " << (endTime - startTime).seconds() << " ms." << endl;

	for (i = 0; i < MAXARRAY; i++) {
		if (array_serial[i] != array_parallel[i]) {
			cout << "Results are NOT the same!" << endl;
			break;
			return 0;
		}
	}

	cout << "Results are the same!" << endl;

	return 0;
}


/* sort everything inbetween `low' <-> `high' */
void quicksort_serial(int arr[], int low, int high) {
	int i = low;
	int j = high;
	int y = 0;
	/* compare value */
	int z = arr[(low + high) / 2];

	/* partition */
	do
	{
		/* find member above ... */
		while (arr[i] < z)
		{
			i++;
		}

		/* find element below ... */
		while (arr[j] > z)
		{
			j--;
		}

		if (i <= j)
		{
			/* swap two elements */
			y = arr[i];
			arr[i] = arr[j];
			arr[j] = y;
			i++;
			j--;
		}
	} while (i <= j);

	busy_wait();
	/* recurse */
	if (low < j)
	{
		quicksort_serial(arr, low, j);
	}

	if (i < high)
	{
		quicksort_serial(arr, i, high);
	}
}

void quicksort_parallel(int arr[], int low, int high) {

	task_group g;

	int i = low;
	int j = high;
	int y = 0;
	/* compare value */
	int z = arr[(low + high) / 2];

	/* partition */
	do
	{
		/* find member above ... */
		while (arr[i] < z)
		{
			i++;
		}

		/* find element below ... */
		while (arr[j] > z)
		{
			j--;
		}

		if (i <= j)
		{
			/* swap two elements */
			y = arr[i];
			arr[i] = arr[j];
			arr[j] = y;
			i++;
			j--;
		}
	} while (i <= j);

	busy_wait();
	/* recurse */
	if (low < j)
	{
		g.run([&] {quicksort_parallel(arr, low, j); });
	}

	if (i < high)
	{
		g.run([&] {quicksort_parallel(arr, i, high); });
	}
	g.wait();
}

void busy_wait() {
	for (int i = 0; i < WAIT_PERIOD; i++){}
}

//Starting serial sort...
//Serial run time : 4.72e-05 ms.
//
//Starting parallel sort...
//Parallel run time : 0.0007924 ms.
//Results are the same!

//Starting serial sort...
//Serial run time : 0.0057131 ms.
//
//Starting parallel sort...
//Parallel run time : 0.0077285 ms.
//Results are the same!

//C:\MIHAJLO_MILOJEVIC\SKOLA\FTN - Pojedinacno\Paralelno_programiranje\vezbe\vezba05_2\primeri\primer 2\QuickSort\QuickSort\x64\Release\QuickSort.exe(process 2316) 
// exited with code - 1073741571 (0xc00000fd).

//Starting serial sort...
//Serial run time : 0.0056109 ms.
//
//Starting parallel sort...
//Parallel run time : 0.0046476 ms.
//Results are the same!