#include <iostream>
#include <fstream>
#include <string>
#include "defines.h"
#include "ReadInFile.h"
#include "HighPassFilter.h"
#include "Clip.h"
#include "Counter.h"
#include "WriteOutFile.h"
#include "Globals.h"
#include "tbb/tick_count.h"

using namespace std;
using namespace tbb;

int main(int argc, char* argv[])
{
    cout << endl << "Filterring started." << endl;

    tick_count startTime = tick_count::now();

    tick_count readInFileStartTime = tick_count::now();
    if (ReadInFile(_D_IN_FILE_NAME) == RET_ERROR)
    {
        cout << endl << "Error during reading input file." << endl;
        return RET_ERROR;
    }
    tick_count readInFileEndTime = tick_count::now();
    cout << endl << "\tRead in file finished. Took: " << (readInFileEndTime - readInFileStartTime).seconds() * 1000 << "ms." << endl << endl;

    tick_count highPassFilterStartTime = tick_count::now();
    if (HighPassFilter(_D_ALPHA) == RET_ERROR)
    {
        cout << endl << "Error in high-pass filter." << endl;
        return RET_ERROR;
    }
    tick_count highPassFilterEndTime = tick_count::now();
    cout << endl << "\tHigh-pass filter finished. Took: " << (highPassFilterEndTime - highPassFilterStartTime).seconds() * 1000 << "ms." << endl << endl;

    tick_count clipStartTime = tick_count::now();
    if (Clip(_D_CLIP_LOWER_VALUE, _D_CLIP_UPPER_VALUE) == RET_ERROR)
    {
        cout << endl << "Clip error." << endl;
        return RET_ERROR;
    }
    tick_count clipEndTime = tick_count::now();
    cout << endl << "\tClipping finished. Took: " << (clipEndTime - clipStartTime).seconds() * 1000 << "ms." << endl << endl;

    tick_count counterStartTime = tick_count::now();
    if (Counter() == RET_ERROR)
    {
        cout << endl << "Error in counter." << endl;
        return RET_ERROR;
    }
    tick_count counterEndTime = tick_count::now();
    cout << endl << "\tCounting finished. Took: " << (counterEndTime - counterStartTime).seconds() * 1000 << "ms." << endl << endl;

    tick_count writeOutFileStartTime = tick_count::now();
    if (WriteOutFile(_D_OUT_FILE_NAME) == RET_ERROR)
    {
        cout << endl << "Error during writing output file." << endl;
        return RET_ERROR;
    }
    tick_count writeOutFileEndTime = tick_count::now();
    cout << endl << "\tWriting out file finished. Took: " << (writeOutFileEndTime - writeOutFileStartTime).seconds() * 1000 << "ms." << endl << endl;

    tick_count endTime = tick_count::now();
    cout << endl << "Filterring finished. Took: " << (endTime - startTime).seconds() * 1000 << "ms." << endl << endl;

    return RET_OK;
}
