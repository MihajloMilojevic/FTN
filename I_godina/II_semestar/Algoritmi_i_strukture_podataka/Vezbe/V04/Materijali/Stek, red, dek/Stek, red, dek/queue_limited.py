"""
Modul sadrži implementaciju reda na osnovu liste.
"""


class EmptyQueueException(Exception):
    """
    Klasa modeluje izuzetke vezane za klasu Queue.
    """
    pass


class Queue(object):
    """
    Implementacija reda na osnovu liste.
    """

    def __init__(self, capacity=10):
        """
        Konstruktor.

        """
        self._data = [None] * capacity
        self._capacity = capacity
        self._first = 0
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        """
        Metoda proverava da li je red prazan.
        """
        return self._size == 0

    def first(self):
        """
        Metoda omogućava pristup prvom elementu reda.
        """
        if self.is_empty():
            raise EmptyQueueException('Red je prazan.')
        return self._data[self._first]

    def dequeue(self):
        """
        Metoda izbacuje prvi element iz reda.
        """
        if self.is_empty():
            raise EmptyQueueException('Red je prazan.')

        element = self._data[self._first]
        self._data[self._first] = None
        self._size -= 1
        self._first = (self._first + 1) % self._capacity

        if self._size < self._capacity/4:
            self._resize(self._capacity//2)

        return element

    def enqueue(self, e):
        """
        Metoda vrši dodavanje elementa u red.

        Argument:
        - `e`: novi element
        """
        if self._size + 1 > self._capacity:
            self._resize(self._capacity*2)

        new_index = (self._first + self._size) % self._capacity
        self._data[new_index] = e
        self._size += 1

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity

        for new_index in range(self._size):
            old_index = (self._first + new_index) % self._capacity
            new_data[new_index] = self._data[old_index]

        self._data = new_data
        self._capacity = new_capacity
        self._first = 0


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(3)
    queue.enqueue(8)
    queue.enqueue(1)
    print(len(queue))
    print(queue.first())

    queue.dequeue()
    print(len(queue))

    print(queue.first())
    print(queue.is_empty())
