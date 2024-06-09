class Student(object):
    """
    U ovoj implementaciji klase student prosek računamo 'nestrpljivo' (eagerly).
    Eager računanje se odnosi na situaciju kada neki proračun (ovde proseka)
    obavimo što je pre moguće uz konstantno održavanje ažurne vrednosti.
    """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._average = 0
        self._grades = []

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def average_grade(self):
        return self._average

    def print(self):
        print("Student " + self._first_name + " " + self._last_name + " ima prosek " + str(self._average))

    def _calculate_average_grade(self):
        self._average = sum(self._grades)/len(self._grades)

    def add_grade(self, new_grade):
        self._grades.append(new_grade)
        self._calculate_average_grade()

    def remove_grade(self, grade):
        self._grades.remove(grade)
        self._calculate_average_grade()
