"""Modul omogućava parsiranje aritmetičkih izraza."""
import re
from errors import ExpressionNotStringError, UnknownCharacterError, InvalidOperatorOrderError

__author__ = 'mijicd'


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



if __name__ == '__main__':
    #
    # key: izraz, value: očekivana lista tokena
    #
    test_cases = {
        # test floats
        "3.14   ^2": ['3.14', '^', '2'],
        "(2.08-.03) ^  2": ['(', '2.08', '-', '.03', ')', '^', '2'],

        # test integers
        "2+(3*4)": ['2', '+', '(', '3', '*', '4', ')'],
        "22     56": ['22', '56'],

        # test invalid
        "ab cd": [],
        "10,22": ['10', '22']
    }

    # for expression, expected in test_cases.items():
    #     assert expected == tokenize(expression)

    # print(tokenize(input(">>")))
    # 6.11 - 74 * 2
    # (24 - 7) ^ (3.2 + (-7))
    # -20 * 7.9 / (3 - 7) 
    # -20 * .9 / (3 - 7) 