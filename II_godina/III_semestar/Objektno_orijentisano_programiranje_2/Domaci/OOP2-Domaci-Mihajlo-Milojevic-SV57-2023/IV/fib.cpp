#include "fib.h"
#include <iostream>s


int fib(int& last)
{
	int count = 1;
	int prev = 1;
	int current = 1;
	int temp = 0;
	while (prev <= current)
	{
		++count;
		temp = prev;
		prev = current;
		current = temp + prev;
	}
	--count;
	last = prev;
	return count;
}

int fib(long& last)
{
	int count = 1;
	long prev = 1;
	long current = 1;
	long temp = 0;
	while (prev <= current)
	{
		++count;
		temp = prev;
		prev = current;
		current = temp + prev;
	}
	--count;
	last = prev;
	return count;
}

int fib(long long& last)
{
	int count = 1;
	long long prev = 1;
	long long current = 1;
	long long temp = 0;
	while (prev <= current)
	{
		++count;
		temp = prev;
		prev = current;
		current = temp + prev;
	}
	--count;
	last = prev;
	return count;
}
