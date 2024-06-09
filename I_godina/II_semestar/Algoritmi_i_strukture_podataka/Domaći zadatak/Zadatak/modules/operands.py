from abc import ABC, abstractmethod
from operators import Operator
from stack import Stack
from token_parser import TokenParser
from tokenizer import tokenize

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