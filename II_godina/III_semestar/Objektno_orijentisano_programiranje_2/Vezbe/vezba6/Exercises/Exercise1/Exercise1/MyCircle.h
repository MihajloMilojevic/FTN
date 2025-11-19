#pragma once
#include "MyShape.h"
# define M_PIl          3.141592653589793238462643383279502884L /* pi */


class MyCircle :
    public MyShape
{
    public:
		MyCircle();
		MyCircle(double r);
		~MyCircle();
		double getArea() override;

		double getRadius();
		void setRadius(double r);
};

