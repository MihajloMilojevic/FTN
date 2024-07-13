#include "MyString.h"

#include <cstring>
#include <iostream>

using namespace std;

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

MyString::MyString(): m_len(0), m_buffer(NULL) {}
MyString::MyString(char *stryng) : m_len(strlen(stryng)), m_buffer(new char[m_len+1])
{
	copyString(m_buffer, stryng);
}
MyString::MyString(const MyString& other) : m_len(other.m_len), m_buffer(new char[m_len + 1])
{
	cout << "Kopiran string!" << endl;
	copyString(m_buffer, other.m_buffer);
}
MyString::~MyString() 
{
	delete[] m_buffer;
}
int MyString::length()
{
	return m_len;
}
MyString& MyString::operator=(const char c)
{
	delete[] m_buffer;
	m_buffer = new char[2];
	m_len = 1;
	m_buffer[0] = c;
	m_buffer[1] = '\0';
	return *this;
}
MyString& MyString::operator=(const char *c)
{
	delete[] m_buffer;
	m_len = strlen(c);
	m_buffer = new char[m_len + 1];
	copyString(m_buffer, c);
	return *this;
}
MyString& MyString::operator=(const MyString& ms)
{
	delete[] m_buffer;
	m_len = strlen(ms.m_buffer);
	m_buffer = new char[m_len + 1];
	copyString(m_buffer, ms.m_buffer);
	return *this;
}
ostream& operator<<(ostream& out, const MyString& ms)
{
	out << ms.m_buffer;
	return out;
}
istream& operator>>(istream& in, MyString& ms)
{
	delete[] ms.m_buffer;
	char *temp = new char[256];
	in >> temp;
	ms.m_len = strlen(temp);
	ms.m_buffer = new char[ms.m_len + 1];
	copyString(ms.m_buffer, temp);
	delete[] temp;
	return in;
}
bool operator==(const MyString& ms, const MyString& ms2)
{
	return compareString(ms.m_buffer, ms2.m_buffer);
}
bool operator!=(const MyString& ms, const MyString& ms2)
{
	return !compareString(ms.m_buffer, ms2.m_buffer);
}
char& MyString::operator[] (int index)
{
	if (index >= m_len || index < 0) {
		cerr << "IndexOutOfBoundsException";
		exit(-1);
	}
	return m_buffer[index];
}

MyString operator+(const MyString& ms, const MyString& ms2)
{
	MyString m;
	m.m_len = ms.m_len + ms2.m_len;
	m.m_buffer = new char[m.m_len + 1];
	copyString(m.m_buffer, ms.m_buffer);
	copyString(m.m_buffer + ms.m_len, ms2.m_buffer);
	return m;
}

MyString operator+(const MyString& ms, const char* c)
{
	MyString m;
	m.m_len = ms.m_len + strlen(c);
	m.m_buffer = new char[m.m_len + 1];
	copyString(m.m_buffer, ms.m_buffer);
	copyString(m.m_buffer + ms.m_len, c);
	return m;
}

MyString operator+(const MyString& ms, const char c)
{
	MyString m;
	m.m_len = ms.m_len + 1;
	m.m_buffer = new char[m.m_len + 1];
	copyString(m.m_buffer, ms.m_buffer);
	m.m_buffer[ms.m_len] = c;
	m.m_buffer[ms.m_len+1] = '\0';
	return m;
}

MyString operator+(const char* c, const MyString& ms)
{
	MyString m;
	m.m_len = ms.m_len + strlen(c);
	m.m_buffer = new char[m.m_len + 1];
	copyString(m.m_buffer, c);
	copyString(m.m_buffer + strlen(c), ms.m_buffer);
	return m;
}

MyString operator+(const char c, const MyString& ms)
{
	MyString m;
	m.m_len = ms.m_len + 1;
	m.m_buffer = new char[m.m_len + 1];
	m.m_buffer[0] = c;
	copyString(m.m_buffer + 1, ms.m_buffer);
	return m;
}

MyString operator+=(MyString& ms, const MyString& ms2)
{
	ms = ms + ms2;
	return ms;
}

MyString operator+=(MyString& ms, const char* c)
{
	ms = ms + c;
	return ms;
}

MyString operator+=(MyString& ms, const char c)
{
	ms = ms + c;
	return ms;
}