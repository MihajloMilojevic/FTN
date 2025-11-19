#include <iostream>
#include "MyComplex.h" // write your own header file "myComplex.h"

using namespace std;

int main(int argc, char** argv) {

	MyComplex a(3.0, 4.0);
	MyComplex b;
	cout << "Enter a complex number :" << endl;
	cin >> b;
	cout << "a (" << a.getReal() << ", " << a.getImag() << "i) " << endl;
	cout << "b " << b << endl;
	cout << "Complex conjugate b is " << ~b <<
		endl; cout << "a + b is " << a + b << endl;
	cout << "a - b is " << a - b << endl;
	cout << "a * b is " << a * b << endl;
	cout << "2 * b is " << b * 2 << endl;
	cout << "b * 2 is " << 2 * b << endl;
	cout << "Done!" << endl;
	return 0;
	
}