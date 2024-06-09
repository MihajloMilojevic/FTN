class Rectangle(object):

    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    def circumference(self):
        return 2*(self._a+self._b)

    def area(self):
        return self._a*self._b

    def __str__(self):
        return "Rectangle(a=%f, b=%f)" % (self._a, self._b)


class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
        self._b = value

    def __str__(self):
        return "Square(a=%f)" % self._a


if __name__ == '__main__':

    rectangle = Rectangle(3, 4)
    print(rectangle, ": ")
    print("\tPovršina =", rectangle.area())
    print("\tObim =", rectangle.circumference())

    square = Square(5)
    print("\n", square, ": ")
    print("\tPovršina =", square.area())
    print("\tObim =", square.circumference())

    print("\nDužina stranice a kvadrata iznosi ", square.a)

    square.a = 12
    print("\n", square, ": ")
    print("\tPovršina =", square.area())
    print("\tObim =", square.circumference())
