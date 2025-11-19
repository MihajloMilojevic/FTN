#ifndef _GLOBALS_H_
#define _GLOBALS_H_

#include <queue>
#include <vector>
#include "defines.h"
#include <tbb/concurrent_vector.h>
#include <tbb/concurrent_hash_map.h>


using namespace std;

// globals
queue<unsigned char> in2HighPassQueue;
tbb::concurrent_vector<short> highPass2ClipVector;
tbb::concurrent_vector<unsigned char> clip2CounterVector;
tbb::concurrent_hash_map<unsigned char, unsigned int> counterMap;

#endif