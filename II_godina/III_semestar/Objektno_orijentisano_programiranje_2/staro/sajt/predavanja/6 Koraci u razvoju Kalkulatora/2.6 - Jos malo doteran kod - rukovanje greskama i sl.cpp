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
	case '8': case '9': case '.': {
		cin.putback(tmp);

		double val;
		cin >> val;
		return Token('8', val);
	}
	case '(':
	case ')':
	case ';':
	case 'q':
	case '+':
	case '*':
	case '-':
	case '/':
		return Token(tmp);
	default:
		error("Bad token");
		return Token();
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
	switch (token.kind) {
	case '(': {
		double lval = expression();
		token = ts.getToken();
		if (token.kind != ')')
			error("Unmatched '('");
		return lval;
	}
	default:
		ts.putBack(token);
		return number();
	}
}


double term()
{
	double lval = primary();

	while (true) {
		Token token = ts.getToken();

		switch (token.kind) {
		case '*':
			lval *= primary();
			break;
		case '/':
			lval /= primary();
			break;
		default:
			ts.putBack(token);
			return lval;
		}
	}
}


double expression()
{
	double lval = term();

	while (true) {
		Token token = ts.getToken();

		switch (token.kind) {
		case '+':
			lval += term();
			break;
		case '-':
			lval -= term();
			break;
		default:
			ts.putBack(token);
			return lval;
		}
	}
}


int main()
{
	try {
		while (true) {
			double lval = 0;
			cout << ">";
			Token token = ts.getToken();
			if (token.kind == 'q')
				break;
			ts.putBack(token);

			lval = expression();

			token = ts.getToken();
			if (token.kind != ';')
				error("Badly terminated expression");
			cout << "=" << lval << endl;
		}
	}
	catch (runtime_error& e) {
		cerr << e.what() << endl;
		return 1;
	}
	
	return 0;
}
