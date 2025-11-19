#ifndef _GLOBALS_H_
#define _GLOBALS_H_

#include <queue>
#include <vector>
#include "defines.h"

using namespace std;

// globals
queue<unsigned char> in2HighPassQueue;
queue<short> highPass2ClipVector;
vector<unsigned char> clip2CounterVector;
unsigned int couterValues[256];

#endif