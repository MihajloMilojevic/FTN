from operands import ExpressionOperand
from token_parser import TokenParser

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