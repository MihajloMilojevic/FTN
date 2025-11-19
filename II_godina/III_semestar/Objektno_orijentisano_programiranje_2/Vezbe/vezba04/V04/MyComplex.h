#pragma once
#include <iostream>

class MyComplex
{
private:
	double real;
	double imag;
public:
	MyComplex();
	MyComplex(double, double);
	MyComplex(const MyComplex&);
	~MyComplex();
	double getReal();
	double getImag();
	void setReal(double);
	void setImag(double);
	MyComplex add(const MyComplex&) const;
	MyComplex sub(const MyComplex&) const;
	MyComplex mul(const MyComplex&) const;
	MyComplex mul(const double) const;
	MyComplex conj() const;

	MyComplex operator+(const MyComplex&) const;
	MyComplex operator-(const MyComplex&) const;
	MyComplex operator*(const MyComplex&) const;
	MyComplex operator*(const double) const;
	MyComplex operator~() const;
	bool operator==(const MyComplex&) const;
	bool operator!=(const MyComplex&) const;

	friend MyComplex operator+(const double, const MyComplex&);
	friend MyComplex operator-(const double, const MyComplex&);
	friend MyComplex operator*(const double, const MyComplex&);
	friend MyComplex operator*(const double, const MyComplex&);

	friend std::ostream& operator<<(std::ostream&, const MyComplex&);
	friend std::istream& operator>>(std::istream&, MyComplex&);
};

