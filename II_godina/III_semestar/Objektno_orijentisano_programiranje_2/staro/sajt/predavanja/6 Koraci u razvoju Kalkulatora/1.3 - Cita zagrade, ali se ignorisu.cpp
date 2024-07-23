#include "std_lib_facilities.h"


int main()
{
	double lval = 0;
	double rval;
	char op;

	cout << ">";

	// читава ова конструкција да би се прескочиле заграде и да би се видело да ли је на улазу литерал реалног броја или нешто друго
	// да се ово не би понављало на свим местима где се учитава са улаза ваљало би га сместити у функцију
	char tmp;
	cin >> tmp;
	while (tmp == '(' || tmp == ')')
		cin >> tmp;
	switch (tmp) {
	case '0': case '1': case '2': case '3':
	case '4': case '5': case '6': case '7':
	case '8': case '9':
		cin.putback(tmp); // << !!!
		cin >> lval;
		break;
	default:
		cout << "Bad first operand" << endl;
		break;
	}

	while (true) {
		// овде се мора поновити све ово као од горе
		cin >> op;

		if (op == ';') {
			cout << "=" << lval << endl;
			return 0;
		}

		// овде се мора поновити све ово као од горе
		cin >> rval;

		switch (op) {
		case '+':
			lval += rval;
			break;
		case '-':
			lval -= rval;
			break;
		case '*':
			lval *= rval;
			break;
		case '/':
			lval /= rval;
			break;
		default:
			cout << "Bad operator!" << endl;
			return 1;
		}
	}
}
