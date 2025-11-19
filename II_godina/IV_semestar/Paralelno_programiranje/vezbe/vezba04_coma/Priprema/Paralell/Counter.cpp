#include "Counter.h"
#include <tbb/parallel_for.h>
#include <tbb/concurrent_vector.h>
#include <tbb/concurrent_hash_map.h>

extern tbb::concurrent_vector<unsigned char> clip2CounterVector;
extern tbb::concurrent_hash_map<unsigned char, unsigned int> counterMap;

struct Histogram {
    void operator()(tbb::blocked_range<int>& range) const {
        for (auto it = range.begin(); it != range.end(); ++it) {
			unsigned char data = clip2CounterVector[it];
			tbb::concurrent_hash_map<unsigned char, unsigned int>::accessor accessor;
			counterMap.insert(accessor, data);
			accessor->second++;
			accessor.release();
        }
	}
};


RetVal Counter()
{
    unsigned char data;

	tbb::parallel_for(tbb::blocked_range<int>(0, clip2CounterVector.size()), Histogram());

    return RET_OK;
}
