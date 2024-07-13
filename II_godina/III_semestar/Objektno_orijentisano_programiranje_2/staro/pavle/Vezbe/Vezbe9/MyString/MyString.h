#pragma once

#include <iostream>
using namespace std;

class MyString
{
private:
	int m_len;
	char* m_buffer;
public:
	MyString();
	MyString(char* stryng);
	MyString(const MyString& other);
	~MyString();

	int length();

	MyString& operator= (const char c);
	MyString& operator= (const char* c);
	MyString& operator= (const MyString& ms);
	char& operator[] (int index);

	friend ostream& operator<<(ostream& out, const MyString& ms);
	friend istream& operator>>(istream& in, MyString& ms);

	friend bool operator==(const MyString& ms, const MyString& ms2);
	friend bool operator!=(const MyString& ms, const MyString& ms2);

	friend MyString operator+(const MyString& ms, const MyString& ms2);
	friend MyString operator+(const MyString& ms, const char* c);
	friend MyString operator+(const MyString& ms, const char c);
	friend MyString operator+(const char* c, const MyString& ms);
	friend MyString operator+(const char c, const MyString& ms);


	friend MyString operator+=(MyString& ms, const MyString& ms2);
	friend MyString operator+=(MyString& ms, const char* c);
	friend MyString operator+=(MyString& ms, const char c);





};

