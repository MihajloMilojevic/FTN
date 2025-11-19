#include "Clip.h"
#include <tbb/concurrent_vector.h>
#include <tbb/parallel_for.h>


extern tbb::concurrent_vector<short> highPass2ClipVector;
extern tbb::concurrent_vector<unsigned char> clip2CounterVector;

struct ClipClass {
    char lowerValue;
    char upperValue;
    ClipClass(char lower, char upper) : lowerValue(lower), upperValue(upper) {}
    void operator()(const tbb::blocked_range<int>& range) const {
		auto dest = clip2CounterVector.grow_by(range.size());
        for (int i = 0; i < range.size(); ++i) {
            short data = highPass2ClipVector[range.begin() + i];
            if (data < lowerValue) {
                data = lowerValue;
            } else if (data > upperValue) {
                data = upperValue;
            }
            dest[i] = data;
		}
	}
};


RetVal Clip(char lowerValue, char upperValue)
{
    tbb:parallel_for(
        tbb::blocked_range<int>(0, highPass2ClipVector.size()), 
        ClipClass(lowerValue, upperValue)
    );
    return RET_OK;
}
