#include <iostream>

using namespace std;

class Complex
{
public:
	Complex();
	Complex(double real, double imaginary);
	double getReal();
	double getImag();
	void setReal(double real);
	void setImag(double imaginary);
	Complex add(Complex rhs);
	Complex sub(Complex rhs);
	Complex mul(Complex rhs);
	Complex conj();


	// Friend so that we can access private members from non - member method
	friend Complex operator + (Complex& lhs, Complex& rhs);
	friend Complex operator - (Complex& lhs, Complex& rhs);
	friend Complex operator * (Complex& lhs, Complex& rhs);
	friend Complex operator * (Complex& lhs, double rhs);
	friend Complex operator * (double rhs, Complex& lhs);

	friend istream& operator >> (istream& in, Complex& c);
	friend ostream& operator << (ostream& out, const Complex& c);

private:
	double real, imaginary;
};

Complex::Complex() : real(0), imaginary(0) {}
Complex::Complex(double real, double imaginary) : real(real), imaginary(imaginary) {}


double Complex::getReal()
{
	return real;
}

double Complex::getImag()
{
	return imaginary;
}

void Complex::setReal(double r)
{
	real = r;
}

void Complex::setImag(double i)
{
	imaginary = i;
}

Complex Complex::add(Complex rhs)
{
	return Complex(real + rhs.getReal(), imaginary + rhs.getImag());
}


Complex Complex::sub(Complex rhs)
{
	return Complex(real - rhs.getReal(), imaginary - rhs.getImag());
}


Complex Complex::mul(Complex rhs)
{
	return Complex(real * rhs.getReal() - imaginary * rhs.getImag(), real * rhs.getImag() + imaginary * rhs.getReal());
}


Complex Complex::conj()
{
	return Complex(real, -imaginary);
}

// It is generally recommended to use non-member functions for overloaded operators
// lhs - left hand side, rhs - right hand side

istream& operator >> (istream& in, Complex& c) {
	double real, imaginary;
	in >> real >> imaginary;
	c.setReal(real);
	c.setImag(imaginary);
	return in;
}

ostream& operator << (ostream& out, const Complex& c) {
	out << "(" << c.real << ", " << c.imaginary << "i)";
	return out;
}

Complex operator ~ (Complex& c) {
	return c.conj();
}

Complex operator + (Complex& lhs, Complex& rhs) {
	return lhs.add(rhs);
}

Complex operator - (Complex& lhs, Complex& rhs) {
	return lhs.sub(rhs);
}

Complex operator * (Complex& lhs, Complex& rhs) {
	return lhs.mul(rhs);
}

Complex operator * (Complex& lhs, double rhs) {
	return Complex(lhs.getReal() * rhs, lhs.getImag() * rhs);
}

Complex operator * (double lhs, Complex& rhs) {
	return Complex(rhs.getReal() * lhs, rhs.getImag() * lhs);
}