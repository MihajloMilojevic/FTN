#pragma once
#include<string>
#include<vector>

int readInt(std::string msg, bool positive = false, bool allowZero = true);
int* readIntArray(int n);
std::vector<int> readIntArrayV(int n);

void clearConsole();