#include "HighPassFilter.h"

extern queue<unsigned char> in2HighPassQueue;
extern queue<short> highPass2ClipQueue;

RetVal HighPassFilter(float alpha)
{
    // input data
    static short xCurr = 0;
    static short xPrev = 0;

    // output data
    static short yCurr = 0;
    static short yPrev = 0;

    // filterring
    while (!in2HighPassQueue.empty())
    {
        xPrev = xCurr;
        xCurr = in2HighPassQueue.front();
        in2HighPassQueue.pop();

        yPrev = yCurr;
        yCurr = alpha * (yPrev + xCurr - xPrev);

        highPass2ClipQueue.push(yCurr);
    }

    return RET_OK;
}
