"""
Modul sadrži implementaciju steka na osnovu liste.
"""


class EmptyStackException(Exception):
    """
    Klasa modeluje izuzetak vezane za prazan Stack.
    """
    pass


class FullStackException(Exception):
    """
    Klasa modeluje izuzetke vezane za popunjen Stack.
    """
    pass


class Stack(object):
    """
    Implementacija steka na osnovu liste.
    """

    def __init__(self, capacity=10):
        self._data = []
        self._capacity = capacity

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        """
        Metoda proverava da li je stek prazan.
        """
        return len(self._data) == 0

    def push(self, e):
        """
        Metoda vrši ubacivanje elementa na stek.

        Argument:
        - `e`: novi element
        """
        if len(self._data) >= self._capacity:
            raise FullStackException("Stek je pun.")
        self._data.append(e)

    def top(self):
        """
        Metoda vraća element na vrhu steka.
        """
        if self.is_empty():
            raise EmptyStackException('Stek je prazan.')
        return self._data[-1]

    def pop(self):
        """
        Metoda izbacuje element sa vrha steka.
        """
        if self.is_empty():
            raise EmptyStackException('Stek je prazan.')
        return self._data.pop()


if __name__ == '__main__':
    s = Stack()
    s.push(2)
    print(s.top())
    print(len(s))

    s.pop()
    print(s.is_empty())
