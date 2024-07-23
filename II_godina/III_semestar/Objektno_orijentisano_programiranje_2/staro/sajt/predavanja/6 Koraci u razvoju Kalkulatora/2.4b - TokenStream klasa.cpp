#include "std_lib_facilities.h"


class Token {
public:
	Token(char ch, double val) : kind(ch), value(val) {}
	Token(char ch) : kind(ch), value(0) {}
	Token() : kind('x'), value(0) {}
	char kind;
	double value;
};


class TokenStream {
public:
	TokenStream() : buffer(), full(false) {}
	Token getToken();
	void putBack(Token token);
	
protected:
	Token buffer;
	bool full;
};


Token TokenStream::getToken()
{
	if (full) {
		full = false;
		return buffer;
	}

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


void TokenStream::putBack(Token token)
{
	buffer = token;
	full = true;
}


TokenStream ts;


double number()
{
	Token token = ts.getToken();
	if (token.kind != '8')
		error("Expected a number");
	return token.value;
}


double expression();


double primary()
{
	Token token = ts.getToken();
	if (token.kind == '(') {
		double lval = expression();
		token = ts.getToken();
		if (token.kind != ')')
			error("Unmatched '('");
		return lval;
	}
	else {
		ts.putBack(token);
		return number();
	}
}


double expression()
{
	double lval = primary();

	while (true) {
		Token token = ts.getToken();

		switch (token.kind) {
		case '+':
			lval += primary();
			break;
		case '-':
			lval -= primary();
			break;
		case '*':
			lval *= primary();
			break;
		case '/':
			lval /= primary();
			break;
		case ')':
		case ';':
			ts.putBack(token);
			return lval;
		default:
			error("Bad operator!");
		}
	}
}


int main()
{
	double lval = 0;

	cout << ">";

	lval = expression();

	cout << "=" << lval << endl;
	return 0;
}
