#pragma once
#include "MyShape.h"
class MyRectangle : public MyShape
{
public:
	MyRectangle();
	MyRectangle(double x, double y);
	~MyRectangle();
	double getArea() override;
	double getLength();
	double getWidth();
	void setLength(double x);
	void setWidth(double y);
};

