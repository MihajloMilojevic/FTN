#include "Clip.h"
#include "tbb/concurrent_vector.h"
#include "tbb/parallel_for.h"

extern tbb::concurrent_vector<short> highPass2ClipCVector;
extern tbb::concurrent_vector<unsigned char> clip2CounterCVector;

struct ClipStruct // struct so everything is public
{
	char lowerValue;
	char upperValue;

	ClipStruct(char lower, char upper) : lowerValue(lower), upperValue(upper) {}

    void operator() (const tbb::blocked_range<int>& r) const
	{
		auto destination = clip2CounterCVector.grow_by(r.size()); // grow the vector to fit the range
		for (int i = r.begin(); i != r.end(); ++i)
		{
			short data = highPass2ClipCVector[i];
			if (data < lowerValue)
			{
				data = lowerValue;
			}
			else if (data > upperValue)
			{
				data = upperValue;
			}
			destination[i - r.begin()] = static_cast<unsigned char>(data);
		}
	}

};

RetVal Clip(char lowerValue, char upperValue)
{
    tbb::parallel_for( tbb::blocked_range<int>(0, highPass2ClipCVector.size()), 
		ClipStruct(lowerValue, upperValue)
	);
    return RET_OK;
}
