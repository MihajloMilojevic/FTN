#pragma once
class MyShape
{
protected:
	double x;
	double y;
public:
	MyShape();
	MyShape(double x, double y);
	~MyShape();
	virtual double getArea() = 0;
};

