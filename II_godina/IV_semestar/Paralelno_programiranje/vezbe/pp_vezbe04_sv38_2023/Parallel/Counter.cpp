#include "Counter.h"
#include "tbb/concurrent_vector.h"
#include "tbb/concurrent_hash_map.h"

extern tbb::concurrent_vector<unsigned char> clip2CounterCVector;
extern tbb::concurrent_hash_map<unsigned char, unsigned int> counterCMap;

// slicno kao na vezbama
struct Histogram {
	void operator()(tbb::blocked_range<int>& r) const
	{
		for (int i = r.begin(); i != r.end(); ++i)
		{
			unsigned char data = clip2CounterCVector[i];
			tbb::concurrent_hash_map<unsigned char, unsigned int>::accessor accessor;
			counterCMap.insert(accessor, data);
			accessor->second++;
			accessor.release(); //to allow other threads to access the map
		}
	}
	};

RetVal Counter()
{
    unsigned char data;

    tbb::parallel_for(tbb::blocked_range<int>(0, clip2CounterCVector.size()), 
					  Histogram());

    return RET_OK;
}
