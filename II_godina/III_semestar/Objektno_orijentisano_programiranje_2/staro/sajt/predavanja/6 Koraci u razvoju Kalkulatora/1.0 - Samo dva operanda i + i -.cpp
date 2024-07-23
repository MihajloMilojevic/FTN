#include "std_lib_facilities.h"


int main()
{
	double lval;
	double rval;
	double res;
	char op;

	cout << ">";

	cin >> lval >> op >> rval;

	if (op == '+')
		res = lval + rval;
	else
		res = lval - rval;

	cout << "=" << res << endl;

	return 0;
}
