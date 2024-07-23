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


int main()
{
	double lval = 0;

	cout << ">";

	Token token = getToken();
	while (token.kind == '(' || token.kind == ')') // прескачемо заграде - за сада
		token = getToken();
	if (token.kind != '8')
		error("Wrong operand");

	lval = token.value;

	while (true) {
		token = getToken();
		while (token.kind == '(' || token.kind == ')') // прескачемо заграде - за сада
			token = getToken();
		if (token.kind == ';') {
			cout << "=" << lval << endl;
			return 0;
		}
		char op = token.kind;

		token = getToken();
		while (token.kind == '(' || token.kind == ')') // прескачемо заграде - за сада
			token = getToken();
		if (token.kind != '8')
			error("Wrong operand");

		switch (op) {
		case '+':
			lval += token.value;
			break;
		case '-':
			lval -= token.value;
			break;
		case '*':
			lval *= token.value;
			break;
		case '/':
			lval /= token.value;
			break;
		default:
			error("Bad operator!");
		}
	}
}
