#include "tbb/concurrent_hash_map.h"
#include "tbb/blocked_range.h"
#include "tbb/parallel_for.h"
#include "tbb/tick_count.h"
#include <tbb/parallel_reduce.h>
#include <iostream>
#include <map>

using namespace std;
using namespace tbb;


const size_t N = 1000000;
int Data[N];

// TODO: Create a simple MyHashCompare structure
struct MyHashCompare {
	static size_t hash(int key) {
		return std::hash<int>()(key);
	}
	static bool equal(int a, int b) {
		return a == b;
	}
};

// A concurrent hash table that maps ints to ints
typedef concurrent_hash_map<int, int, MyHashCompare> IntTable;

// TODO: Create a simple Histogram class which will count the number of occurrences
struct Histogram {
	IntTable& table;
	Histogram(IntTable& t) : table(t) {}
	void operator()(const blocked_range<int>& r) const {
		for (int i = r.begin(); i != r.end(); ++i) {
			IntTable::accessor a;
			// Insert vraća true ako je ključ nov, što znači da je ovo prvo pojavljivanje
			table.insert(a, Data[i]);
			a->second++;
			a.release();
		}
	}
};


// Local histogram used in parallel_reduce
struct LocalHistogram {
	std::map<int, int> localMap;

	LocalHistogram() = default;

	// Split constructor
	LocalHistogram(LocalHistogram& other, split) {
	}

	// Processing a range
	void operator()(const blocked_range<int>& r) {
		for (int i = r.begin(); i < r.end(); ++i) {
			localMap[Data[i]]++;
		}
	}

	// Combine results from another thread
	void join(const LocalHistogram& rhs) {
		for (const auto& kv : rhs.localMap) {
			localMap[kv.first] += kv.second;
		}
	}
};

// Parallel for with local map
struct LocalHistogramFor {
	IntTable& table;
	LocalHistogramFor(IntTable& t) : table(t) {}
	void operator()(const blocked_range<int>& r) const {
		auto localMap = std::map<int, int>();
		for (int i = r.begin(); i != r.end(); ++i) {
			localMap[Data[i]]++;
		}
		for (const auto& kv : localMap) {
			IntTable::accessor a;
			// Insert returns true if the key is new, meaning this is the first occurrence
			table.insert(a, kv.first);
			a->second += kv.second;
			a.release();
		}
	}
};

// Count occurrences
std::tuple<double, double, double, double> run(int dataMod) {
	

	// Create some data to work with
	for (int i = 0; i < N; i++) {
		Data[i] = rand() % dataMod;
	}

	std::map<int, int> occurrences;
	auto start = tbb::tick_count::now();
	for (int i = 0; i < N; i++) {
		int value = Data[i];
		// Insert returns true if the key is new, meaning this is the first occurrence
		auto result = occurrences.insert({ value, 1 });
		if (!result.second) {
			result.first->second++;
		}
	}
	auto end = tbb::tick_count::now();
	std::cout << "Time taken (serial) with " << dataMod << " keys: " << (end - start).seconds() << " seconds" << std::endl;

	auto v1 = (end - start).seconds();

	// TODO: Put occurrences into the table using parallel_for
	// Construct empty table
	IntTable table;

	start = tbb::tick_count::now();
	parallel_for(blocked_range<int>(0, N), Histogram(table));
	end = tbb::tick_count::now();
	std::cout << "Time taken (parallel_for) with " << dataMod << " keys: " << (end - start).seconds() << " seconds" << std::endl;

	auto v2 = (end - start).seconds();

	// Construct empty table
	IntTable table2;

	start = tbb::tick_count::now();
	LocalHistogram finalHist = parallel_reduce(
		blocked_range<int>(0, N),
		LocalHistogram(),
		[](const blocked_range<int>& r, LocalHistogram init) -> LocalHistogram {
			init(r);
			return init;
		},
		[](LocalHistogram a, const LocalHistogram& b) -> LocalHistogram {
			a.join(b);
			return a;
		}
	);

	// Merge results into concurrent hash map

	for (auto it = finalHist.localMap.begin(); it != finalHist.localMap.end(); ++it) {
		IntTable::accessor a;
		table2.insert(a, it->first);
		a->second += it->second;
		// a.release() is optional here, destructor will release it
	}
	end = tbb::tick_count::now();
	std::cout << "Time taken (parallel_reduce) with " << dataMod << " keys: " << (end - start).seconds() << " seconds" << std::endl;

	auto v3 = (end - start).seconds();

	IntTable table3;
	start = tbb::tick_count::now();
	parallel_for(blocked_range<int>(0, N), LocalHistogramFor(table3));
	end = tbb::tick_count::now();
	std::cout << "Time taken (parallel_for with local map) with " << dataMod << " keys: " << (end - start).seconds() << " seconds" << std::endl;

	auto v4 = (end - start).seconds();

	return make_tuple(v1, v2, v3, v4);
}

int main() {
	double v1, v2, v3, v4;
	double s1 = 0, s2 = 0, s3 = 0, s4 = 0;
	int count = 0;
	for (int i = 10; i <= 1000000; i *= 10) {
		tie(v1, v2, v3, v4) = run(i);
		s1 += v1;
		s2 += v2;
		s3 += v3;
		s4 += v4;
		++count;
		std::cout << "\n\n\n";
	}
	std::cout << "Average time taken (serial): " << s1 / count << " seconds" << std::endl;
	std::cout << "Average time taken (parallel_for): " << s2 / count << " seconds" << std::endl;
	std::cout << "Average time taken (parallel_reduce): " << s3 / count << " seconds" << std::endl;
	std::cout << "Average time taken (parallel_for with local map): " << s4 / count << " seconds" << std::endl;
	return 0;
}


//Time taken(serial) with 10 keys: 0.0165383 seconds
//Time taken(parallel_for) with 10 keys : 0.0290592 seconds
//Time taken(parallel_reduce) with 10 keys : 0.0021135 seconds
//Time taken(parallel_for with local map) with 10 keys : 0.0026791 seconds
//
//
//
//Time taken(serial) with 100 keys : 0.0364378 seconds
//Time taken(parallel_for) with 100 keys : 0.0236317 seconds
//Time taken(parallel_reduce) with 100 keys : 0.0067002 seconds
//Time taken(parallel_for with local map) with 100 keys : 0.0077584 seconds
//
//
//
//Time taken(serial) with 1000 keys : 0.0591257 seconds
//Time taken(parallel_for) with 1000 keys : 0.0098696 seconds
//Time taken(parallel_reduce) with 1000 keys : 0.0098531 seconds
//Time taken(parallel_for with local map) with 1000 keys : 0.0182236 seconds
//
//
//
//Time taken(serial) with 10000 keys : 0.109883 seconds
//Time taken(parallel_for) with 10000 keys : 0.0215632 seconds
//Time taken(parallel_reduce) with 10000 keys : 0.0543706 seconds
//Time taken(parallel_for with local map) with 10000 keys : 0.0318565 seconds
//
//
//
//Time taken(serial) with 100000 keys : 0.19879 seconds
//Time taken(parallel_for) with 100000 keys : 0.0094088 seconds
//Time taken(parallel_reduce) with 100000 keys : 0.0949824 seconds
//Time taken(parallel_for with local map) with 100000 keys : 0.0227788 seconds
//
//
//
//Time taken(serial) with 1000000 keys : 0.179374 seconds
//Time taken(parallel_for) with 1000000 keys : 0.0106949 seconds
//Time taken(parallel_reduce) with 1000000 keys : 0.0738474 seconds
//Time taken(parallel_for with local map) with 1000000 keys : 0.0197706 seconds
//
//
//
//Average time taken(serial) : 0.100025 seconds
//Average time taken(parallel_for) : 0.0173712 seconds
//Average time taken(parallel_reduce) : 0.0403112 seconds
//Average time taken(parallel_for with local map) : 0.0171778 seconds