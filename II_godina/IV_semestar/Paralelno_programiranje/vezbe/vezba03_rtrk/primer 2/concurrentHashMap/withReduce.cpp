//#include "tbb/concurrent_hash_map.h"
//#include "tbb/blocked_range.h"
//#include "tbb/parallel_reduce.h"
//#include "tbb/tick_count.h"
//#include <iostream>
//#include <map>
//
//using namespace std;
//using namespace tbb;
//
//const size_t N = 1000000;
//int Data[N];
//
//// Custom hash comparator
//struct MyHashCompare {
//	static size_t hash(int key) {
//		return std::hash<int>()(key);
//	}
//	static bool equal(int a, int b) {
//		return a == b;
//	}
//};
//
//// A concurrent hash table that maps ints to ints
//typedef concurrent_hash_map<int, int, MyHashCompare> IntTable;
//
//// Local histogram used in parallel_reduce
//struct LocalHistogram {
//	std::map<int, int> localMap;
//
//	LocalHistogram() = default;
//
//	// Split constructor
//	LocalHistogram(LocalHistogram& other, split) {
//	}
//
//	// Processing a range
//	void operator()(const blocked_range<int>& r) {
//		for (int i = r.begin(); i < r.end(); ++i) {
//			localMap[Data[i]]++;
//		}
//	}
//
//	// Combine results from another thread
//	void join(const LocalHistogram& rhs) {
//		for (const auto& kv : rhs.localMap) {
//			localMap[kv.first] += kv.second;
//		}
//	}
//};
//
//int main() {
//	// Construct empty table
//	IntTable table;
//
//	// Create some data to work with
//	for (int i = 0; i < N; i++) {
//		Data[i] = rand() % 1000;
//	}
//
//	// Serial version for comparison
//	std::map<int, int> occurrences;
//	auto start = tbb::tick_count::now();
//	for (int i = 0; i < N; i++) {
//		int value = Data[i];
//		auto result = occurrences.insert({ value, 1 });
//		if (!result.second) {
//			result.first->second++;
//		}
//	}
//	auto end = tbb::tick_count::now();
//	std::cout << "Time taken (serial): " << (end - start).seconds() << " seconds" << std::endl;
//
//	// Parallel_reduce version
//	start = tbb::tick_count::now();
//	LocalHistogram finalHist = parallel_reduce(
//		blocked_range<int>(0, N),
//		LocalHistogram(),
//		[](const blocked_range<int>& r, LocalHistogram init) -> LocalHistogram {
//			init(r);
//			return init;
//		},
//		[](LocalHistogram a, const LocalHistogram& b) -> LocalHistogram {
//			a.join(b);
//			return a;
//		}
//	);
//
//	// Merge results into concurrent hash map
//	for (const auto& kv : finalHist.localMap) {
//		IntTable::accessor a;
//		table.insert(a, kv.first);
//		a->second += kv.second;
//		a.release();
//	}
//	end = tbb::tick_count::now();
//	std::cout << "Time taken (parallel_reduce): " << (end - start).seconds() << " seconds" << std::endl;
//
//	// Uncomment to print occurrences
//	// for (IntTable::const_iterator it = table.begin(); it != table.end(); ++it) {
//	// 	cout << "Value: " << it->first << ", Count: " << it->second << endl;
//	// }
//
//	return 0;
//}
