#include "WriteOutFile.h"
#include "tbb/concurrent_hash_map.h"
#include <vector>
#include <algorithm>

extern tbb::concurrent_hash_map<unsigned char, unsigned int> counterCMap;

RetVal WriteOutFile(std::string fileName)
{
    std::ofstream outputFile(fileName.c_str());

    if (!outputFile.is_open())
    {
        std::cout << "WriteOutFile: Output file " << fileName << " could not be opened." << std::endl;
        return RET_ERROR;
    }

    // This is the old code where data from concurrent hash map is just loaded in no particular order
    // for (auto i = counterCMap.cbegin(); i != counterCMap.cend(); ++i)
    //{
    //    outputFile << static_cast<int>(i->first) << ":\t " << i->second << endl;
    //}


    // To keep the same order as in the serial output file, a vector will be used to sort all entries for the parallel output file

    // First I will copy everything to a vector
    std::vector<std::pair<unsigned char, unsigned int>> entries;
    entries.reserve(counterCMap.size()); // optional, but avoids reallocations
    for (auto i = counterCMap.cbegin(); i != counterCMap.cend(); ++i)
    {
        entries.emplace_back(i->first, i->second);
    }

    // Then sort the vector by the first element of the pair (the key)
    std::sort(entries.begin(), entries.end(),
        [](const auto& a, const auto& b) {
            return a.first < b.first;
        });
   
    // After sorting, write all key-value pairs to the output file
    for (const auto& p : entries)
    {
        outputFile << static_cast<int>(p.first) << ":\t " << p.second << "\n";
    }

    outputFile.close();
    return RET_OK;
}
