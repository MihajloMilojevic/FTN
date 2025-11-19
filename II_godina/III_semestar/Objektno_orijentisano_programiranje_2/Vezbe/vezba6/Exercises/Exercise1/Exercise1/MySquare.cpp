#include "MySquare.h"

MySquare::MySquare(): MyRectangle(0, 0) {}

MySquare::MySquare(double x) : MyRectangle(x, x) {}

MySquare::~MySquare() {}

double MySquare::getArea()
{
    return x * x;
}

double MySquare::getLength()
{
    return x;
}

double MySquare::getWidth()
{
    return x;
}

void MySquare::setLength(double x)
{
    this->x = x;
    this->y = x;
}

void MySquare::setWidth(double y)
{
    this->x = y;
    this->y = x;
}

void MySquare::setSide(double x)
{
    this->x = x;
	this->y = x;
}
