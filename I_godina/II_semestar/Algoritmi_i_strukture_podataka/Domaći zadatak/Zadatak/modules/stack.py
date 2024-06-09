from errors import EmptyStackError


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
    


