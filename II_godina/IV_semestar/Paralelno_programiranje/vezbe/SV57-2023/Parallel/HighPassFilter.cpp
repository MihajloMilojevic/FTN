#include "HighPassFilter.h"
#include <tbb/concurrent_vector.h>

extern queue<unsigned char> in2HighPassQueue;
extern tbb::concurrent_vector<short> highPass2ClipVector;

RetVal HighPassFilter(float alpha)
{
    // input data
    static short xCurr = 0;
    static short xPrev = 0;

    // output data
    static short yCurr = 0;
    static short yPrev = 0;

    auto dst = highPass2ClipVector.grow_by(in2HighPassQueue.size()); 
	int i = 0;
    // filterring
    while (!in2HighPassQueue.empty())
    {
        xPrev = xCurr;
        xCurr = in2HighPassQueue.front();
        in2HighPassQueue.pop();

        yPrev = yCurr;
        yCurr = alpha * (yPrev + xCurr - xPrev);

        dst[i++] = yCurr;
    }

    return RET_OK;
}
