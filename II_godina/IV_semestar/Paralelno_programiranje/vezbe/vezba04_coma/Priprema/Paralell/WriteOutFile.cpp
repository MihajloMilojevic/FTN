#include "WriteOutFile.h"
#include <tbb/concurrent_hash_map.h>

extern tbb::concurrent_hash_map<unsigned char, unsigned int> counterMap;
;

RetVal WriteOutFile(string fileName)
{
    ofstream outputFile(fileName.c_str());

    if (outputFile.is_open() == false)
    {
        cout << "WriteOutFile: Output file " << fileName << " could not be opened." << endl;
        return RET_ERROR;
    }


    for (auto it = counterMap.cbegin(); it != counterMap.cend(); ++it)
    {
        outputFile << static_cast<int>(it->first) << ":\t" << it->second << endl;
	}
    outputFile.close();

    return RET_OK;
}
