#include "MyCircle.h"

MyCircle::MyCircle(): MyShape() {}

MyCircle::MyCircle(double r): MyShape(r, 0) {}

MyCircle::~MyCircle() {}

double MyCircle::getArea() {
    return x * x * M_PIl;
}

double MyCircle::getRadius()
{
    return x;
}

void MyCircle::setRadius(double r)
{
	x = r;
}
