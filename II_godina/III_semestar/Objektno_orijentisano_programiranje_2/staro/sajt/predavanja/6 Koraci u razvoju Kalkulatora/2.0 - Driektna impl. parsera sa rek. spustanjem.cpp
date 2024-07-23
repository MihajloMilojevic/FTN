#include "std_lib_facilities.h"


class Token {
public:
	Token(char ch, double val) : kind(ch), value(val) {}
	Token(char ch) : kind(ch), value(0) {}
	Token() : kind('x'), value(0) {}
	char kind;
	double value;
};


Token getToken()
{
	char tmp;
	cin >> tmp;

	switch (tmp) {
	case '0': case '1': case '2': case '3':
	case '4': case '5': case '6': case '7':
	case '8': case '9':
	{
		cin.putback(tmp);

		double val;
		cin >> val;
		return Token('8', val);
	}
	default:
		return Token(tmp);
	}
}


double number()
{
	Token token = getToken();
	if (token.kind != '8')
		error("Expected a number");
	return token.value;
}


double expression()
{
	double lval = expression();

	Token token = getToken();

	switch (token.kind) {
	case '+':
		lval += number();
		break;
	case '-':
		lval -= number();
		break;
	case '*':
		lval *= number();
		break;
	case '/':
		lval /= number();
		break;
	case ';':
		return lval;
	default:
		error("Bad operator!");
	}

	return lval;
}


int main()
{
	double lval = 0;

	cout << ">";

	lval = expression();

	cout << "=" << lval << endl;
	return 0;
}
