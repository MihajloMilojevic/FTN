import random


class HashMap(object):
    """
    Klasa modeluje heš mapu
    """
    def __init__(self, capacity=8):
        """
        Konstruktor

        Argumenti:
        - `capacity`: inicijalni broj mesta u lookup nizu
        - `prime`: prost broj neophodan heš funkciji
        """
        self._data = capacity * [None]
        self._capacity = capacity
        self._size = 0
        self._prime = 109345121

        # konstante heširanja
        self._a = 1 + random.randrange(self._prime-1)
        self._b = random.randrange(self._prime)

    def _hash(self, x):
        """
        Heš funkcija

        Izračunavanje heš koda vrši se po formuli (ax + b) mod p.

        Argument:
        - `x`: vrednost čiji se kod računa
        """
        hashed_value = (hash(x)*self._a + self._b) % self._prime
        compressed = hashed_value % self._capacity
        return compressed
