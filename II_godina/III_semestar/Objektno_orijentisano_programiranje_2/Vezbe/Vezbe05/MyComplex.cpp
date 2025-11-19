#include "MyComplex.h"
#include <sstream>

MyComplex::MyComplex(): real(0.0), imag(0.0)
{
}

MyComplex::MyComplex(double x, double y): real(x), imag(y)
{
}

MyComplex::MyComplex(const MyComplex& c): real(c.real), imag(c.imag)
{
}

MyComplex::MyComplex(std::string& exp)
{
    if (exp[exp.length() - 1] != 'i') 
        throw std::invalid_argument("Invalid complex number format: " + exp);
    exp.pop_back();
    int pos = 1;
    while (std::isdigit(exp[pos])) ++pos;
    std::stringstream ss;
    ss << exp.substr(0, pos);
    ss >> real;
    ss.clear();
    ss << exp.substr(pos);
    ss >> imag;
    
}

MyComplex::~MyComplex()
{
}

double MyComplex::getReal()
{
    return real;
}

double MyComplex::getImag()
{
    return imag;
}

void MyComplex::setReal(double x)
{
    real = x;
}

void MyComplex::setImag(double x)
{
    imag = x;
}

MyComplex MyComplex::add(const MyComplex& c) const
{
    return MyComplex(real + c.real, imag + c.imag);
}

MyComplex MyComplex::sub(const MyComplex& c) const
{
    return MyComplex(real - c.real, imag - c.imag);
}

MyComplex MyComplex::mul(const MyComplex& c) const
{
    return MyComplex(real * c.real - imag * c.imag, real * c.imag + imag * c.real);
}

MyComplex MyComplex::mul(const double c) const
{
    return MyComplex(c * real, c * imag);
}

MyComplex MyComplex::conj() const
{
    return MyComplex(real, -imag);
}

MyComplex MyComplex::operator+(const MyComplex& c) const
{
    return add(c);
}

MyComplex MyComplex::operator-(const MyComplex& c) const
{
    return sub(c);
}

MyComplex MyComplex::operator*(const MyComplex& c) const
{
    return mul(c);
}

MyComplex MyComplex::operator*(const double c) const
{
    return mul(c);
}

MyComplex MyComplex::operator~() const
{
    return conj();
}


bool MyComplex::operator==(const MyComplex& c) const
{
    return real == c.real && imag == c.imag;
}

bool MyComplex::operator!=(const MyComplex& c) const
{
    return real != c.real || imag != c.imag;
}

MyComplex operator+(const double a, const MyComplex& b)
{
    return MyComplex(a, 0.0).add(b);
}

MyComplex operator-(const double a, const MyComplex& b)
{
    return MyComplex(a, 0.0).sub(b);
}

MyComplex operator*(const double a, const MyComplex& b)
{
    return MyComplex(a, 0.0).mul(b);
}

std::ostream& operator<<(std::ostream& _out, const MyComplex& c)
{
    _out << c.real;
    if (c.imag >= 0) _out << "+";
    _out << c.imag << "i";
    return _out;
}

std::istream& operator>>(std::istream& _in, MyComplex& _c)
{
    float real;
    float imag;
    char i;
    _in >> real;
    _in >> imag;
    _in >> i;
    _c.setReal(real);
    _c.setImag(imag);
    return _in;
}

