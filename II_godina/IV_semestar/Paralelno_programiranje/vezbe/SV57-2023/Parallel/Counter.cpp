#include "Counter.h"
#include <tbb/parallel_for.h>
#include <tbb/concurrent_vector.h>
#include <tbb/concurrent_hash_map.h>
#include <tbb/parallel_reduce.h>
#include <map>

extern tbb::concurrent_vector<unsigned char> clip2CounterVector;
extern tbb::concurrent_hash_map<unsigned char, unsigned int> counter;

struct LocalHistogram {
	std::map<unsigned char, unsigned int> localMap;
   
	LocalHistogram() = default;

	// Split constructor
	LocalHistogram(LocalHistogram& other, tbb:: split) {
	}

	// Processing a range
	void operator()(const tbb::blocked_range<int>& r) {
		for (int i = r.begin(); i < r.end(); ++i) {
			localMap[clip2CounterVector[i]]++;
		}
	}

	// Combine results from another thread
	void join(const LocalHistogram& rhs) {
		for (const auto& kv : rhs.localMap) {
			localMap[kv.first] += kv.second;
		}
	}
};


struct LocalHistogramFor {
	void operator()(const tbb::blocked_range<int>& r) const {
		auto localMap = std::map<int, int>();
		for (int i = r.begin(); i != r.end(); ++i) {
			localMap[clip2CounterVector[i]]++;
		}
		for (const auto& kv : localMap) {
			tbb::concurrent_hash_map<unsigned char, unsigned int>::accessor a;
			// Insert returns true if the key is new, meaning this is the first occurrence
			counter.insert(a, kv.first);
			a->second += kv.second;
			a.release();
		}
	}
};



RetVal Counter()
{

	//LocalHistogram finalHist = tbb::parallel_reduce(
	//	tbb::blocked_range<int>(0, clip2CounterVector.size()),
	//	LocalHistogram(),
	//	[](const tbb::blocked_range<int>& r, LocalHistogram init) -> LocalHistogram {
	//		init(r);
	//		return init;
	//	},
	//	[](LocalHistogram a, const LocalHistogram& b) -> LocalHistogram {
	//		a.join(b);
	//		return a;
	//	}
	//);

	//// Merge results into concurrent hash map

	//for (auto it = finalHist.localMap.cbegin(); it != finalHist.localMap.cend(); ++it) {
	//	tbb::concurrent_hash_map<unsigned char, unsigned int>::accessor a;
	//	counter.insert(a, it->first);
	//	a->second += it->second;
	//	// a.release() is optional here, destructor will release it
	//}

	tbb::parallel_for(tbb::blocked_range<int>(0, clip2CounterVector.size(), 10000), LocalHistogramFor());

	return RET_OK;
}
