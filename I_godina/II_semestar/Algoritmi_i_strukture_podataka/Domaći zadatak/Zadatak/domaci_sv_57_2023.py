# OVE TRI METODE ĆE BITI POZIVANE KROZ AUTOMATSKE TESTOVE. NEMOJTE MENJATI NAZIV, PARAMETRE I POVRATNU VREDNOST.
#Dozvoljeno je implementirati dodatne, pomoćne metode, ali isključivo u okviru ovog modula.

import re
from abc import ABC, abstractmethod
import math
import unittest

def infix_to_postfix(expression):
    """Funkcija konvertuje izraz iz infiksne u postfiksnu notaciju

    Args:
        expression (string): Izraz koji se parsira. Izraz može da sadrži cifre, zagrade, znakove računskih operacija.
        U slučaju da postoji problem sa formatom ili sadržajem izraza, potrebno je baciti odgovarajući izuzetak.

    Returns:
        list: Lista tokena koji predstavljaju izraz expression zapisan u postfiksnoj notaciji.
    Primer:
        ulaz '6.11 – 74 * 2' se pretvara u izlaz [6.11, 74, 2, '*', '-']
    """
    return MathExpression.postfix_split(expression)

def calculate_postfix(token_list):
    """Funkcija izračunava vrednost izraza zapisanog u postfiksnoj notaciji

    Args:
        token_list (list): Lista tokena koja reprezentuje izraz koji se izračunava. Izraz može da sadrži cifre, zagrade,
         znakove računskih operacija.
        U slučaju da postoji problem sa brojem parametara, potrebno je baciti odgovarajući izuzetak.

    Returns:
        result: Broj koji reprezentuje konačnu vrednost izraza

    Primer:
        Ulaz [6.11, 74, 2, '*', '-'] se pretvara u izlaz -141.89
    """
    return MathExpression.evaluate(tokens = token_list)


def calculate_infix(expression):
    """Funkcija izračunava vrednost izraza zapisanog u infiksnoj notaciji

    Args:
        expression (string): Izraz koji se parsira. Izraz može da sadrži cifre, zagrade, znakove računskih operacija.
        U slučaju da postoji problem sa formatom ili sadržajem izraza, potrebno je baciti odgovarajući izuzetak.

        U slučaju da postoji problem sa brojem parametara, potrebno je baciti odgovarajući izuzetak.
        

    Returns:
        result: Broj koji reprezentuje konačnu vrednost izraza

    Primer:
        Ulaz '6.11 - 74 * 2' se pretvara u izlaz -141.89
    """
    return MathExpression.evaluate(expression = expression)
    



############     ERRORS START     ############

class ExpressionNotStringError(Exception):
    pass

class TokenNotStringError(Exception):
    pass

class UnknownCharacterError(Exception):
    pass

class InvalidOperatorOrderError(Exception):
    pass

class EmptyStackError(Exception):
    pass

class NoOpenParenthesisError(Exception):
    pass

class NoCloseParenthesisError(Exception):
    pass

class DivisionByzeroError(Exception):
    pass

class ComplexRootError(Exception):
    pass

class EmptyParenthesisError(Exception):
    pass

class EmptyExpressionError(Exception):
    pass

class UndefinedOperationError(Exception):
    pass

############     ERRORS END     ############


############     MATH EXPRESSION START     ############

class MathExpression:
    
    @staticmethod
    def postfix(expression):
        return ExpressionOperand(expression).postfix()
    
    @staticmethod
    def postfix_split(expression):
        return ExpressionOperand(expression).postfix_split()

    @staticmethod
    def evaluate(*, tokens=None, expression=None):
        if expression is not None:
            tokens = ExpressionOperand(expression).postfix_split()
        parsed = [TokenParser.parse_token(str(token)) for token in tokens]
        return ExpressionOperand("", processed_tokens=parsed).evaluate()

############     MATH EXPRESSION END     ############


############     OPERANDS START     ############

class Operand(ABC):
    def __init__(self) -> None:
        self._infix = ""
        self._tokens = ""


    @abstractmethod
    def infix(self):
        pass

    @abstractmethod
    def postfix(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass

class NumericalOperand(Operand):
    def __init__(self, value) -> None:
        super().__init__()
        self._infix = value

    def infix(self):
        return self._infix

    def postfix(self):
        return self._infix

    def evaluate(self):
        if "." in self._infix:
            return float(self._infix)
        return int(self._infix)
    
    def __str__(self) -> str:
        return self._infix
    
class ExpressionOperand(Operand):
    def __init__(self, expression, *, processed_tokens = None) -> None:
        super().__init__()
        self._infix = expression
        self._postfix = None
        self._postfix_split = None
        self._tokens = processed_tokens
        if expression == "" and processed_tokens is None:
            raise EmptyExpressionError("Expression cannot be empty.")

    def infix(self):
        return self._infix

    def postfix(self):
        if self._postfix is not None:
            return self._postfix
        if self._tokens is None:
            tokens = tokenize(self._infix)
            parsed = TokenParser.parse(tokens)
            self._tokens = parsed
        else:
            parsed = self._tokens
        stack = Stack()
        postfix = []
        for token in parsed:
            if isinstance(token, Operand):
                postfix.append(token.postfix())
            elif isinstance(token, Operator):               # its an operator
                while not stack.is_empty() and stack.peek() <= token:
                    op = stack.pop()
                    postfix.append(op.postfix())
                stack.push(token)
        while not stack.is_empty():
            postfix.append(stack.pop().postfix())
        self._postfix = " ".join(postfix)
        return self._postfix

    def postfix_split(self):
        if self._postfix_split is not None:
            return self._postfix_split
        postfix_split = self.postfix().split(" ")
        result = []
        for part in postfix_split:
            if part in "+-*^/()~":
                result.append(part)
            elif "." in part:
                result.append(float(part))
            else:
                result.append(int(part))
        self._postfix_split = result
        return result

    def evaluate(self):
        if self._tokens is None:
            self.postfix_split()
        tokens = self._tokens
        tokens = [TokenParser.parse_token(str(token)) for token in tokens]
        # print("TOKENS: ", " ".join([str(x) for x in tokens]))
        stack = Stack()
        for token in tokens:
            if isinstance(token, Operand):
                a = token.evaluate()
                stack.push(a)
                # print("PUSHED: ", a)

            elif isinstance(token, Operator):
                # print("OPERATOR: ", token)
                values = []
                for _ in range(token.number_or_arguments):
                    values.append(stack.pop())
                values.reverse()
                result = token.execute(*values)
                if result is not None:
                    stack.push(result)
        return stack.pop()

    def __str__(self) -> str:
        return self._infix

############     OPERANDS END     ############
    

############     OPERATORS START     ############

class Operator(ABC):
    def __init__(self, symbol, priority, number_of_arguments=2):
        self._symbol = symbol
        self._priority = priority
        self.number_or_arguments = number_of_arguments

    @abstractmethod
    def execute(self):
        pass

    def infix(self):
        return self._symbol
    
    def postfix(self):
        return self._symbol

    def __eq__(self, other):
        return self._priority == other._priority

    def __gt__(self, other):
        return self._priority > other._priority

    def __lt__(self, other):
        return self._priority < other._priority

    def __ge__(self, other):
        return self._priority >= other._priority

    def __le__(self, other):
        return self._priority <= other._priority
    
    def __str__(self):
        return self._symbol
    
class AdditionOperator(Operator):
    def __init__(self):
        super().__init__("+", 800)

    def execute(self, a, b):
        return a + b

class SubtractionOperator(Operator):
    def __init__(self):
        super().__init__("-", 800)

    def execute(self, a, b):
        return a - b

class MultiplicationOperator(Operator):
    def __init__(self):
        super().__init__("*", 600)

    def execute(self, a, b):
        return a * b

class DivisionOperator(Operator):
    def __init__(self):
        super().__init__("/", 600)

    def execute(self, a, b):
        if a == 0 and b == 0:
            raise UndefinedOperationError("0/0 is an undefined operation.")
        if b == 0:
            raise DivisionByzeroError("Division by zero is not allowed.")
        return a / b

class ExponentationOperator(Operator):
    def __init__(self):
        super().__init__("^", 200)

    def execute(self, a, b):
        if math.fabs(b - int(b)) > 0 and a < 0:
            raise ComplexRootError("Negative number cannot be raised to a floating-point power.")
        if a == 0 and b < 0:
            raise DivisionByzeroError("Division by zero is not allowed.")
        return a ** b
    
class NegationOperator(Operator):
    def __init__(self):
        super().__init__("~", 400, number_of_arguments=1)

    def execute(self, a):
        return -a
    
class OpeningParenthesisOperator(Operator):
    def __init__(self):
        super().__init__("(", 0, number_of_arguments=0)

    def postfix(self):
        return ""

    def execute(self):
        return None

class ClosingParenthesisOperator(Operator):
    def __init__(self):
        super().__init__(")", 0, number_of_arguments=0)

    
    def postfix(self):
        return ""

    def execute(self):
        return None

############     OPERATORS END     ############
    

############     TOKEN PARSER START     ############

class TokenParser(object):
    _addition_operator = AdditionOperator()
    _subtraction_operator = SubtractionOperator()
    _multiplication_operator = MultiplicationOperator()
    _division_operator = DivisionOperator()
    _exponentation_operator = ExponentationOperator()
    _negation_operator = NegationOperator()
    _opening_parenthesis_operator = OpeningParenthesisOperator()
    _closing_parenthesis_operator = ClosingParenthesisOperator()

    _operations = {
        "+": _addition_operator,
        "-": _subtraction_operator,
        "*": _multiplication_operator,
        "/": _division_operator,
        "^": _exponentation_operator,
        "~": _negation_operator,
        "(": _opening_parenthesis_operator,
        ")": _closing_parenthesis_operator
    }

    @staticmethod 
    def parse_token(token):
        if not isinstance(token, str):
            raise TokenNotStringError("Token should be string!")
        if token in TokenParser._operations:
            return TokenParser._operations[token]
        try:
            float(token)
            return NumericalOperand(token)
        except ValueError:
            raise ValueError(f"Token '{token}' is not valid number.")
        
    @staticmethod
    def parse_tokens(tokens):
        return [TokenParser.parse_token(token) for token in tokens]

    @staticmethod
    def parse(tokens, *, parsed = False):
        if not parsed:
            parsed_tokens = TokenParser.parse_tokens(tokens)
        else:
            parsed_tokens = tokens

        resulting_tokens = []
        number_of_parantheses = 0
        i = 0
        while i < len(parsed_tokens):
            if isinstance(parsed_tokens[i], OpeningParenthesisOperator):
                ##### found open parenthesis, need to evaluate expression inside
                number_of_parantheses += 1
                expression_tokens_string = []
                expression_tokens_parsed = []
                i += 1  # skip open parenthesis
                while i < len(parsed_tokens) and number_of_parantheses > 0:
                    expression_tokens_string.append(str(tokens[i]))
                    expression_tokens_parsed.append(parsed_tokens[i])
                    if isinstance(parsed_tokens[i], OpeningParenthesisOperator):
                        number_of_parantheses += 1
                    if isinstance(parsed_tokens[i], ClosingParenthesisOperator):
                        number_of_parantheses -= 1
                    i += 1
                if number_of_parantheses > 0:
                    raise  NoCloseParenthesisError("No closing parenthesis for open parenthesis.")
                expression_tokens_string.pop()  # remove closing parenthesis
                expression_tokens_parsed.pop()  # remove closing parenthesis
                if len(expression_tokens_parsed) == 0:
                    raise EmptyParenthesisError("Empty parenthesis.")
                resulting_tokens.append(ExpressionOperand("".join(expression_tokens_string), processed_tokens=TokenParser.parse(expression_tokens_parsed, parsed=True)))
                continue
                #### end of expression inside parenthesis
            if isinstance(parsed_tokens[i], ClosingParenthesisOperator):
                number_of_parantheses -= 1
            if number_of_parantheses < 0:
                raise NoOpenParenthesisError("No open parenthesis for closing parenthesis.")
            resulting_tokens.append(parsed_tokens[i])
            i += 1
        if number_of_parantheses > 0:
            raise NoCloseParenthesisError("No closing parenthesis for open parenthesis.")
        
        for i in range(len(resulting_tokens)-1):
            if isinstance(resulting_tokens[i], Operand) and isinstance(resulting_tokens[i+1], Operand):
                raise InvalidOperatorOrderError("Two operands cannot be next to each other.")
            if isinstance(resulting_tokens[i], Operator) and isinstance(resulting_tokens[i+1], Operator):
                raise InvalidOperatorOrderError("Two operators cannot be next to each other.")
        if isinstance(resulting_tokens[-1], Operator):
            raise InvalidOperatorOrderError("Operator cannot be at the end of the expression.")
        if isinstance(resulting_tokens[0], Operator) and not isinstance(resulting_tokens[0], NegationOperator):
            raise InvalidOperatorOrderError("Operator cannot be at the beggining of the expression.")
        return resulting_tokens

############     TOKEN PARSER END     ############


############     STACK START     ############
    
class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self._stack.pop()
        else:
            raise EmptyStackError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self._stack[-1]
        else:
            raise EmptyStackError("Stack is empty")

    def is_empty(self):
        return len(self._stack) == 0

    def size(self):
        return len(self._stack)
    
    def __str__(self) -> str:
        return " ".join([str(x) for x in self._stack[::-1]])

############     STACK END     ############
    

############     TOKENIZER START     ############
    
REGEX = r'(?:\d*\.\d+)|(?:\d+)|(?:[()+\-\^/*])'

def tokenize(expression):
    """Funkcija kreira tokene na osnovu zadatog izraza.

    Postupak formiranja liste tokena koristi regularni izraz
    zadat putem REGEX varijable. Omogućeno je pronalaženje
    sledećih tipova tokena:
        - floating-point vrednosti
        - celobrojne vrednosti
        - operatori +, -, *, /, ^
        - zagrade

    Args:
        expression (string): Izraz koji se parsira.

    Returns:
        list: Lista pronađenih tokena.

    Raises:
        AssertionError: Ako izraz nije zadat kao string.
    """
    if not isinstance(expression, str):
        raise ExpressionNotStringError("Expression should be string!")

    bare_tokens = re.findall(REGEX, expression)

    if expression.replace(" ", "") != "".join(bare_tokens):
        raise UnknownCharacterError("Expression contains unsupported character(s).")

    tokens = []
    # Find unary '-' and add it to the preceding operand
    i = 0
    while i < len(bare_tokens):
        if bare_tokens[i] == '-':
            if i == len(bare_tokens) - 1:
                raise InvalidOperatorOrderError(f"Operator cannot be at the end of the expression.")
            if bare_tokens[i+1] in '+-*/^)' or (i > 0 and bare_tokens[i-1] in "+-*/^"):
                raise InvalidOperatorOrderError(f"Two operators cannot be next to each other.")
            if (i == 0 or bare_tokens[i-1] in '+-*/^('):
                if bare_tokens[i+1] == "(" or (i+2 < len(bare_tokens) and bare_tokens[i+2] == "^"):
                    tokens.append("~")
                    i += 1
                    continue
                tokens.append('-' + bare_tokens[i+1])
                i += 2
                continue
            if (i == 0 or bare_tokens[i-1] in '+-*/^('):
                tokens.append('-' + bare_tokens[i+1])
                i += 2
                continue
        tokens.append(bare_tokens[i])
        i += 1
    return tokens

############     TOKENIZER END     ############


############     TESTS START     ############
        
class TestInfixToPostfix(unittest.TestCase):
    ############     VALID     ############
    def test_infix_to_postfix_1(self):
        input_expression = "6.11 - 74 * 2 "
        excepted_output = "6.11 74 2 * -"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)

    def test_infix_to_postfix_2(self):
        input_expression = "(24 - 7) ^ (3.2 + (-7))"
        excepted_output = "24 7 - 3.2 -7 + ^"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)

    def test_infix_to_postfix_3(self):
        input_expression = "-20 * 7.9 / (3 - 7)"
        excepted_output = "-20 7.9 * 3 7 - /"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)

    def test_infix_to_postfix_4(self):
        input_expression = "-20 * .9 / (3 - 7)"
        excepted_output = "-20 0.9 * 3 7 - /"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)

    def test_infix_to_postfix_5(self):
        input_expression = "2*3+4^(5-1-(-10+2*3*2))"
        excepted_output = "2 3 * 4 5 1 - -10 2 3 * 2 * + - ^ +"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)

    def test_infix_to_postfix_6(self):
        input_expression = "2 + 3 * 4 - (5 / 6) ^ 2"
        excepted_output = "2 3 4 * + 5 6 / 2 ^ -"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)

    def test_infix_to_postfix_7(self):
        input_expression = "(-2 + 3) * (4.36 - (-5)) / (-6) ^ 2"
        excepted_output = "-2 3 + 4.36 -5 - * -6 2 ^ /"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)

    def test_infix_to_postfix_8(self):
        input_expression = "-2^3^4^5-5*5/25+1"
        excepted_output = "2 3 ^ 4 ^ 5 ^ ~ 5 5 * 25 / - 1 +"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)

    def test_infix_to_postfix_9(self):
        input_expression = "-(-(-5.25-6))^5*(-4.99)-2"
        excepted_output = "-5.25 6 - ~ 5 ^ ~ -4.99 * 2 -"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)

    def test_infix_to_postfix_10(self):
        input_expression = "-(-(-(-(-(-(-(-(-(-5.55-(-5.55))^2)^3)^4)^5)^6)^7)^8)^9)^10"
        excepted_output = "-5.55 -5.55 - 2 ^ ~ 3 ^ ~ 4 ^ ~ 5 ^ ~ 6 ^ ~ 7 ^ ~ 8 ^ ~ 9 ^ ~ 10 ^ ~"
        function_output = infix_to_postfix(input_expression)
        output_string = " ".join([str(elem) for elem in function_output])
        self.assertEqual(output_string, excepted_output)

    ############     INVALID     ############

    def test_infix_to_postfix_11(self):
        input_expression = ""
        self.assertRaises(EmptyExpressionError, infix_to_postfix, input_expression)

    def test_infix_to_postfix_12(self):
        input_expression = "2+()"
        self.assertRaises(EmptyParenthesisError, infix_to_postfix, input_expression)

    def test_infix_to_postfix_13(self):
        input_expression = "-2-"
        self.assertRaises(InvalidOperatorOrderError, infix_to_postfix, input_expression)

    def test_infix_to_postfix_14(self):
        input_expression = "2^-3"
        self.assertRaises(InvalidOperatorOrderError, infix_to_postfix, input_expression)

    def test_infix_to_postfix_15(self):
        input_expression = "2+"
        self.assertRaises(InvalidOperatorOrderError, infix_to_postfix, input_expression)

    def test_infix_to_postfix_16(self):
        input_expression = "+5-3"
        self.assertRaises(InvalidOperatorOrderError, infix_to_postfix, input_expression)

    def test_infix_to_postfix_17(self):
        input_expression = "((2+3)"
        self.assertRaises(NoCloseParenthesisError, infix_to_postfix, input_expression)

    def test_infix_to_postfix_18(self):
        input_expression = "(2+3))"
        self.assertRaises(NoOpenParenthesisError, infix_to_postfix, input_expression)

    def test_infix_to_postfix_19(self):
        input_expression = "2a+3b"
        self.assertRaises(UnknownCharacterError, infix_to_postfix, input_expression)

    def test_infix_to_postfix_20(self):
        input_expression = "4:5"
        self.assertRaises(UnknownCharacterError, infix_to_postfix, input_expression)

class TestCalculatePostfix(unittest.TestCase):

    def test_calculate_postfix_1(self):
        input_expression = "6.11 - 74 * 2 "
        excepted_output = -141.89
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_2(self):
        input_expression = "(24 - 7) ^ (3.2 - 2)"
        excepted_output = 29.9597859131
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_3(self):
        input_expression = "20 * 7.9 / (3 - 7)"
        excepted_output = -39.5
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_4(self):
        input_expression = "-20 * .9 / (3 - 7)"
        excepted_output = 4.5
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_5(self):
        input_expression = "2*3+4^(5-1-(-10+2*3*2))"
        excepted_output = 22
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_6(self):
        input_expression = "2 + 3 * 4 - (5 / 6) ^ 2"
        excepted_output = 13.3055555555555
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_7(self):
        input_expression = "(-2 + 3) * (4.36 - (-5)) / (-6) ^ 2"
        excepted_output = 0.26
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_8(self):
        input_expression = "-2^3^4^5-5*5/25+1"
        excepted_output = -1.152921504606847e+18
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_9(self):
        input_expression = "-(-(-5.25-6))^5*(-4.99)-2"
        excepted_output = 899212.2028808594
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)
    
    def test_calculate_postfix_10(self):
        input_expression = "-(-(-(-(-(-(-(-(-(-5.55-(-5.55))^2)^3)^4)^5)^6)^7)^8)^9)^10"
        excepted_output = 0
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_11(self):
        input_expression = "-2^2"
        excepted_output = -4
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_postfix_12(self):
        input_expression = "2^0"
        excepted_output = 1
        function_output = calculate_postfix(infix_to_postfix(input_expression))
        self.assertAlmostEqual(function_output, excepted_output)

    ############     INVALID     ############

    def test_calculate_postfix_13(self):
        input_expression = "10/0"
        self.assertRaises(DivisionByzeroError, calculate_postfix, infix_to_postfix(input_expression))

    def test_calculate_postfix_14(self):
        input_expression = "15/(2-2)"
        self.assertRaises(DivisionByzeroError, calculate_postfix, infix_to_postfix(input_expression))

    def test_calculate_postfix_15(self):
        input_expression = "12 / (3 - 9/3) "
        self.assertRaises(DivisionByzeroError, calculate_postfix, infix_to_postfix(input_expression))

    def test_calculate_postfix_16(self):
        input_expression = "(-2)^0.5"
        self.assertRaises(ComplexRootError, calculate_postfix, infix_to_postfix(input_expression))

    def test_calculate_postfix_17(self):
        input_expression = "(5-5^2)^(1/3)"
        self.assertRaises(ComplexRootError, calculate_postfix, infix_to_postfix(input_expression))

    def test_calculate_postfix_18(self):
        input_expression = "0/0"
        self.assertRaises(UndefinedOperationError, calculate_postfix, infix_to_postfix(input_expression))

    
    def test_calculate_postfix_19(self):
        input_expression = "-(-2+2)/(5-5)"
        self.assertRaises(UndefinedOperationError, calculate_postfix, infix_to_postfix(input_expression))
    
    def test_calculate_postfix_20(self):
        input_expression = "0*0^(-1)"
        self.assertRaises(DivisionByzeroError, calculate_postfix, infix_to_postfix(input_expression))

class TestCalculateInfix(unittest.TestCase):

    def test_calculate_infix_1(self):
        input_expression = "6.11 - 74 * 2 "
        excepted_output = -141.89
        function_output = calculate_infix(input_expression)
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_infix_2(self):
        input_expression = "(24 - 7) ^ (3.2 - 2)"
        excepted_output = 29.9597859131
        function_output = calculate_infix(input_expression)
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_infix_3(self):
        input_expression = "20 * 7.9 / (3 - 7)"
        excepted_output = -39.5
        function_output = calculate_infix(input_expression)
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_infix_4(self):
        input_expression = "-20 * .9 / (3 - 7)"
        excepted_output = 4.5
        function_output = calculate_infix(input_expression)
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_infix_5(self):
        input_expression = "2*3+4^(5-1-(-10+2*3*2))"
        excepted_output = 22
        function_output = calculate_infix(input_expression)
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_infix_6(self):
        input_expression = "2 + 3 * 4 - (5 / 6) ^ 2"
        excepted_output = 13.3055555555555
        function_output = calculate_infix(input_expression)
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_infix_7(self):
        input_expression = "(-2 + 3) * (4.36 - (-5)) / (-6) ^ 2"
        excepted_output = 0.26
        function_output = calculate_infix(input_expression)
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_infix_8(self):
        input_expression = "-2^3^4^5-5*5/25+1"
        excepted_output = -1.152921504606847e+18
        function_output = calculate_infix(input_expression)
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_infix_9(self):
        input_expression = "-(-(-5.25-6))^5*(-4.99)-2"
        excepted_output = 899212.2028808594
        function_output = calculate_infix(input_expression)
        self.assertAlmostEqual(function_output, excepted_output)
    
    def test_calculate_infix_10(self):
        input_expression = "-(-(-(-(-(-(-(-(-(-5.55-(-5.55))^2)^3)^4)^5)^6)^7)^8)^9)^10"
        excepted_output = 0
        function_output = calculate_infix(input_expression)
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_infix_11(self):
        input_expression = "-2^2"
        excepted_output = -4
        function_output = calculate_infix(input_expression)
        self.assertAlmostEqual(function_output, excepted_output)

    def test_calculate_infix_12(self):
        input_expression = "2^0"
        excepted_output = 1
        function_output = calculate_infix(input_expression)
        self.assertAlmostEqual(function_output, excepted_output)

    ############     INVALID     ############

    def test_calculate_infix_13(self):
        input_expression = "10/0"
        self.assertRaises(DivisionByzeroError, calculate_infix, input_expression)

    def test_calculate_infix_14(self):
        input_expression = "15/(2-2)"
        self.assertRaises(DivisionByzeroError, calculate_infix, input_expression)

    def test_calculate_infix_15(self):
        input_expression = "12 / (3 - 9/3) "
        self.assertRaises(DivisionByzeroError, calculate_infix, input_expression)

    def test_calculate_infix_16(self):
        input_expression = "(-2)^0.5"
        self.assertRaises(ComplexRootError, calculate_infix, input_expression)

    def test_calculate_infix_17(self):
        input_expression = "(5-5^2)^(1/3)"
        self.assertRaises(ComplexRootError, calculate_infix, input_expression)

    def test_calculate_infix_18(self):
        input_expression = "0/0"
        self.assertRaises(UndefinedOperationError, calculate_infix, input_expression)

    def test_calculate_infix_19(self):
        input_expression = "-(-2+2)/(5-5)"
        self.assertRaises(UndefinedOperationError, calculate_infix, input_expression)

    def test_calculate_infix_20(self):
        input_expression = "0*0^(-1)"
        self.assertRaises(DivisionByzeroError, calculate_infix, input_expression)


############     TESTS END     ############
        

############     MAIN START     ############
if __name__ == '__main__':
    
    
    while ((unos := input(">> ")) != "exit"):
        print("Postfix: ", " ".join([str(x) for x in infix_to_postfix(unos)]))
        print("Rezultat: ", calculate_postfix(infix_to_postfix(unos)))
        print("Resultat infix: ", calculate_infix(unos))
        print("Python eval: ", eval(unos.replace("^", "**")))

    unittest.main()