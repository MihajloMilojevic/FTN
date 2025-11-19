#include "ReadInFile.h"

extern queue<unsigned char> in2HighPassQueue;

RetVal ReadInFile(string fileName)
{
    unsigned char data;
    FILE* inputFile;
    errno_t err = fopen_s(&inputFile, fileName.c_str(), "rb");

	if (err != 0)
    {
        cout << "ReadInFile: Input file " << fileName << " could not be opened." << endl;
		return RET_ERROR;
	}
	
    while(fread(&data, sizeof(unsigned char), 1, inputFile))
    {
        in2HighPassQueue.push(data);		
    }

    fclose(inputFile);

    return RET_OK;
}
