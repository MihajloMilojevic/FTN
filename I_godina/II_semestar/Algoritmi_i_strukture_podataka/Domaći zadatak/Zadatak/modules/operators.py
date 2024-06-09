from abc import ABC, abstractmethod
import errors
import math

class Operator(ABC):
    def __init__(self, symbol, priority, number_of_arguments=2):
        self._symbol = symbol
        self._priority = priority
        self.number_or_arguments = number_of_arguments

    @abstractmethod
    def execute(self, a, b):
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
            raise errors.UndefinedOperationError("0/0 is an undefined operation.")
        if b == 0:
            raise errors.DivisionByzeroError("Division by zero is not allowed.")
        return a / b

class ExponentationOperator(Operator):
    def __init__(self):
        super().__init__("^", 200)

    def execute(self, a, b):
        if math.fabs(b - int(b)) > 0 and a < 0:
            raise errors.ComplexRootError("Negative number cannot be raised to a floating-point power.")
        if a == 0 and b < 0:
            raise errors.DivisionByzeroError("Division by zero is not allowed.")
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
