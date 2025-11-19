#include "WriteOutFile.h"
#include <tbb/concurrent_hash_map.h>

extern tbb::concurrent_hash_map<unsigned char, unsigned int> counter;
;

RetVal WriteOutFile(string fileName, int lower = 0, int upper = 0)
{
    ofstream outputFile(fileName.c_str());

    if (outputFile.is_open() == false)
    {
        cout << "WriteOutFile: Output file " << fileName << " could not be opened." << endl;
        return RET_ERROR;
    }


    // Not sorted
    /*for (auto it = counter.cbegin(); it != counter.cend(); ++it)
    {
        outputFile << static_cast<int>(it->first) << ":\t" << it->second << endl;
    }*/

	// Sorted
    while (lower <= upper)
    {
		tbb::concurrent_hash_map<unsigned char, unsigned int>::const_accessor accessor;
        if (counter.find(accessor, static_cast<unsigned char>(lower)))
        {
            outputFile << static_cast<int>(lower) << ":\t" << accessor->second << endl;
        }
		++lower;
	}

    outputFile.close();

    return RET_OK;
}
