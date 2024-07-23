#include "MyString.h"

#include <cstring>

//-----------------------------------------------------------
// HELPER FUNCTIONS
//-----------------------------------------------------------
void copyString(char* dst, const char* src)
{
	strcpy(dst, src);
	dst[strlen(src)] = '\0';
}

bool compareString(const char* src1, const char* src2)
{
	if (strcmp(src1, src2) == 0)
		return true;
	return false;
}
//-----------------------------------------------------------
//-----------------------------------------------------------