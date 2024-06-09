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