"""
Modul sadrži implementaciju deka na osnovu liste.
"""


class EmptyDequeException(Exception):
    """
    Klasa modeluje izuzetke vezane za klasu Deque.
    """
    pass


class Deque(object):
    """
    Implementacija deka na osnovu liste.
    """

    def __init__(self):
        """
        Konstruktor.
        """
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        """
        Metoda proverava da li je dek prazan.
        """
        return len(self) == 0

    def first(self):
        """
        Metoda omogućava pristup prvom elementu deka.
        """
        if self.is_empty():
            raise EmptyDequeException('Dek je prazan.')
        return self._data[0]

    def last(self):
        """
        Metoda omogućava pristup poslednjem elementu deka.
        """
        if self.is_empty():
            raise EmptyDequeException('Dek je prazan.')

        return self._data[-1]

    def add_first(self, e):
        """
        Metoda dodaje element na početak deka.

        Argument:
        - `e`: novi element
        """
        self._data.insert(0, e)

    def add_last(self, e):
        """
        Metoda dodaje element na kraj deka.

        Argument:
        - `e`: novi element
        """
        self._data.append(e)

    def delete_first(self):
        """
        Metoda izbacuje prvi element iz deka.
        """
        if self.is_empty():
            raise EmptyDequeException('Dek je prazan.')

        return self._data.pop(0)

    def delete_last(self):
        """
        Metoda izbacuje poslednji element iz deka.
        """
        if self.is_empty():
            raise EmptyDequeException('Dek je prazan.')

        return self._data.pop()

    def __str__(self):
        return str(self._data)


if __name__ == '__main__':
    d = Deque()
    d.add_last(5)
    d.add_first(7)
    d.add_first(3)
    print(d.first())

    d.delete_last()
    print(len(d))

    d.delete_last()
    d.delete_last()
    d.add_first(6)
    print(d.last())

    d.add_first(8)
    print(d.is_empty())
    print(d.last())
