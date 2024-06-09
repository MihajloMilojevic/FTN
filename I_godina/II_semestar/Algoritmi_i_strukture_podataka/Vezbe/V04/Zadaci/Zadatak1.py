"""
Modul sadrži implementaciju steka na osnovu liste.
"""

class StackError(Exception):
    """
    Klasa modeluje izuzetke vezane za klasu Stack.
    """
    pass


class Stack(object):
    """
    Implementacija steka na osnovu liste.
    """

    def __init__(self):
        self._data = []

    def __len__(self):
        """
        Metoda utvrđuje broj elemenata na steku.
        :return: Broj elemenata na steku.
        """
        return len(self._data)

    def is_empty(self):
        """
        Metoda proverava da li je stek prazan.
        :return: True ako je stek prazan, False ako nije.
        """
        return len(self) == 0 

    def push(self, element):
        """
        Metoda dodaje novi element na stek.
        :param element: Element koji se dodaje na stek.
        """
        self._data.append(element)

    def top(self):
        """
        Metoda pronalazi element na vrhu steka. Ukoliko je stek prazan, potrebno je baciti izuzetak.
        :return: Element na vrhu steka.
        """
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._data[-1]

    def pop(self):
        """
        Metoda izbacuje element sa vrha steka. Ukoliko je stek prazan, potrebno je baciti izuzetak.
        :return: Uklonjeni element.
        """
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._data.pop()
        


if __name__ == '__main__':
    s = Stack()
    s.push(2)
    print(s.top())
    print(len(s))

    s.pop()
    print(s.is_empty())
