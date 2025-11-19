#include "MyRectangle.h"

MyRectangle::MyRectangle(): MyShape(0, 0) {}

MyRectangle::MyRectangle(double x, double y) : MyShape(x, y) {}

MyRectangle::~MyRectangle() {}

double MyRectangle::getArea()
{
    return x * y;
}

double MyRectangle::getLength()
{
    return x;
}

double MyRectangle::getWidth()
{
    return y;
}

void MyRectangle::setLength(double x)
{
    this->x = x;
}

void MyRectangle::setWidth(double y)
{
    this->y = y;
}
