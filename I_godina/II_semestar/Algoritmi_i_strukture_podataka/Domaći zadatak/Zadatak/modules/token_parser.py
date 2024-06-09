import operators
from errors import *
import operands

class TokenParser(object):
    _addition_operator = operators.AdditionOperator()
    _subtraction_operator = operators.SubtractionOperator()
    _multiplication_operator = operators.MultiplicationOperator()
    _division_operator = operators.DivisionOperator()
    _exponentation_operator = operators.ExponentationOperator()
    _negation_operator = operators.NegationOperator()
    _opening_parenthesis_operator = operators.OpeningParenthesisOperator()
    _closing_parenthesis_operator = operators.ClosingParenthesisOperator()

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
            return operands.NumericalOperand(token)
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
            if isinstance(parsed_tokens[i], operators.OpeningParenthesisOperator):
                ##### found open parenthesis, need to evaluate expression inside
                number_of_parantheses += 1
                expression_tokens_string = []
                expression_tokens_parsed = []
                i += 1  # skip open parenthesis
                while i < len(parsed_tokens) and number_of_parantheses > 0:
                    expression_tokens_string.append(str(tokens[i]))
                    expression_tokens_parsed.append(parsed_tokens[i])
                    if isinstance(parsed_tokens[i], operators.OpeningParenthesisOperator):
                        number_of_parantheses += 1
                    if isinstance(parsed_tokens[i], operators.ClosingParenthesisOperator):
                        number_of_parantheses -= 1
                    i += 1
                if number_of_parantheses > 0:
                    raise  NoCloseParenthesisError("No closing parenthesis for open parenthesis.")
                expression_tokens_string.pop()  # remove closing parenthesis
                expression_tokens_parsed.pop()  # remove closing parenthesis
                if len(expression_tokens_parsed) == 0:
                    raise EmptyParenthesisError("Empty parenthesis.")
                resulting_tokens.append(operands.ExpressionOperand("".join(expression_tokens_string), processed_tokens=TokenParser.parse(expression_tokens_parsed, parsed=True)))
                continue
                #### end of expression inside parenthesis
            if isinstance(parsed_tokens[i], operators.ClosingParenthesisOperator):
                number_of_parantheses -= 1
            if number_of_parantheses < 0:
                raise NoOpenParenthesisError("No open parenthesis for closing parenthesis.")
            resulting_tokens.append(parsed_tokens[i])
            i += 1
        if number_of_parantheses > 0:
            raise NoCloseParenthesisError("No closing parenthesis for open parenthesis.")
        
        for i in range(len(resulting_tokens)-1):
            if isinstance(resulting_tokens[i], operands.Operand) and isinstance(resulting_tokens[i+1], operands.Operand):
                raise InvalidOperatorOrderError("Two operands cannot be next to each other.")
            if isinstance(resulting_tokens[i], operands.Operator) and isinstance(resulting_tokens[i+1], operands.Operator):
                raise InvalidOperatorOrderError("Two operators cannot be next to each other.")
        if isinstance(resulting_tokens[-1], operators.Operator):
            raise InvalidOperatorOrderError("Operator cannot be at the end of the expression.")
        if isinstance(resulting_tokens[0], operators.Operator) and not isinstance(resulting_tokens[0], operators.NegationOperator):
            raise InvalidOperatorOrderError("Operator cannot be at the beggining of the expression.")
        return resulting_tokens