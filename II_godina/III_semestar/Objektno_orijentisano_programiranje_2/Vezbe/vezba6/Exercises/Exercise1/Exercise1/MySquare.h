#pragma once
#include "MyRectangle.h"
class MySquare : public MyRectangle
{
	public:
	MySquare();
	MySquare(double x);
	~MySquare();
	double getArea() override;
	double getLength();
	double getWidth();
	void setLength(double x);
	void setWidth(double y);
	void setSide(double x);
};

