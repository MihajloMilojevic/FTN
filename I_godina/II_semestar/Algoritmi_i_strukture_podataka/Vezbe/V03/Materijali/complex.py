class ComplexNumber(object):

    def __init__(self, real=0, imaginary=0):
        self._real = real
        self._imaginary = imaginary

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, new_value):
        self._real = new_value

    @property
    def imaginary(self):
        return self._imaginary

    @imaginary.setter
    def imaginary(self, new_value):
        self._imaginary = new_value

    def __str__(self):
        return str(self._real) +  " + " + str(self._imaginary) + "i"

    def __add__(self, other_number):
        r1 = self._real
        i1 = self._imaginary
        r2 = other_number.real
        i2 = other_number.imaginary

        return ComplexNumber(r1+r2, i1+i2)

    def __sub__(self, other_number):
        r1 = self._real
        i1 = self._imaginary
        r2 = other_number.real
        i2 = other_number.imaginary

        return ComplexNumber(r1-r2, i1-i2)

    def __truediv__(self, other_number):
        raise NotImplementedError("Please provide implementation for this method.")


if __name__ == '__main__':
    n1 = ComplexNumber(1, 2)
    n2 = ComplexNumber(-1, 5)
    #print(n1 / n2) #n1.add(n2)



