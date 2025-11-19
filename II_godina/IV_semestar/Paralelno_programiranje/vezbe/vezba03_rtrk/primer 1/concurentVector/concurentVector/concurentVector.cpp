#include <vector>
#include "tbb/concurrent_vector.h"
#include "tbb/blocked_range.h"
#include "tbb/parallel_for.h"
#include "tbb/tick_count.h"
#include <iostream>

using namespace std;
using namespace tbb;

const size_t N = 100000000;
int Data[N];

int main() {

	cout << "Preparing data..." << endl;

	for (int i = 0; i < N; i++) {
		Data[i] = rand() % 10;
	}


	cout << "Data prepared." << endl << endl << endl;

	/*
	* SEKVENCIJALNO
	*/
	// std vector
	vector<int> vect;
	tick_count start = tick_count::now();
	for (int i = 0; i < N; i++) {
		vect.push_back(Data[i]);
	}
	tick_count end = tick_count::now();

	cout << "Adding elements to the std vector lasted: " << (end - start).seconds() << " seconds." << endl << endl << endl;
	
	vector<int> vect2;
	vect2.reserve(N); // reserve memory for N elements
	start = tick_count::now();
	for (int i = 0; i < N; i++) {
		vect2.push_back(Data[i]);
	}
	end = tick_count::now();

	cout << "Adding elements to the std vector with reserve lasted: " << (end - start).seconds() << " seconds." << endl << endl << endl;


	vector<int> vect3;
	vect3.resize(N);
	start = tick_count::now();
	for (int i = 0; i < N; i++) {
		vect3[i] = Data[i];
	}
	end = tick_count::now();

	cout << "Adding elements to the std vector with resize lasted: " << (end - start).seconds() << " seconds." << endl << endl << endl;


	// tbb concurrent vector
	concurrent_vector<int> conVect;

	start = tick_count::now();
	for (int i = 0; i < N; i++) {
		conVect.push_back(Data[i]);
	}
	end = tick_count::now();

	cout << "Adding elements to the concurrent vector sequentially lasted: " << (end - start).seconds() << " seconds." << endl << endl << endl;
	

	// tbb concurrent vector with grow_by before loop
	concurrent_vector<int> conVect2;

	start = tick_count::now();
	auto dst1 = conVect2.grow_by(N);
	for (int i = 0; i < N; i++) {
		dst1[i] = Data[i];
	}
	end = tick_count::now();

	cout << "Adding elements to the concurrent vector with grow_by before sequentially lasted: " << (end - start).seconds() << " seconds." << endl << endl << endl;

	// PARALELNO


	concurrent_vector<int> conVect3;

	start = tick_count::now();
    parallel_for(blocked_range<size_t>(0, N),
		[&](const blocked_range<size_t>& r) {
			for (size_t i = r.begin(); i != r.end(); ++i) {
				conVect3.push_back(Data[i]);
			}
		}
    );
	end = tick_count::now();

	cout << "Adding elements to the concurrent vector in parallel lasted: " << (end - start).seconds() << " seconds." << endl << endl << endl;


	concurrent_vector<int> conVect4;
	start = tick_count::now();
	auto dst4 = conVect4.grow_by(N);
	parallel_for(blocked_range<size_t>(0, N),
		[&](const blocked_range<size_t>& r) {
			for (size_t i = r.begin(); i != r.end(); ++i) {
				dst4[i] = Data[i];
			}
		}
	);
	end = tick_count::now();

	cout << "Adding elements to the concurrent vector with grow_by before in parallel lasted: " << (end - start).seconds() << " seconds." << endl << endl << endl;



	concurrent_vector<int> conVect5;
	start = tick_count::now();
	parallel_for(blocked_range<size_t>(0, N),
		[&](const blocked_range<size_t>& r) {
			auto dst5 = conVect5.grow_by(r.size());
			auto begin = r.begin();
			for (size_t i = 0; i != r.size(); ++i) {
				dst5[i] = Data[i + begin];
			}
		}
	);
	end = tick_count::now();

	cout << "Adding elements to the concurrent vector with grow_by inside in parallel lasted: " << (end - start).seconds() << " seconds." << endl << endl << endl;


	concurrent_vector<int> conVect6;
	start = tick_count::now();
	conVect6.grow_by(N);
	parallel_for(blocked_range<size_t>(0, N),
		[&](const blocked_range<size_t>& r) {
			for (size_t i = r.begin(); i != r.end(); ++i) {
				conVect6[i] = Data[i];
			}

		}
	);
	end = tick_count::now();

	cout << "Adding elements to the concurrent vector in parallel KAO SA VEZBI lasted: " << (end - start).seconds() << " seconds." << endl << endl << endl;



	
	getchar();
	return 0;
}