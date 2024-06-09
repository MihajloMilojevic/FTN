class Student(object):
    """
    U ovoj implementaciji klase student prosek računamo 'lenjo' (lazily).
    Lenjo računanje se odnosi na situaciju kada neku operaciju ili proračun
    (ovde proseka) obavimo ne što je pre moguće, nego kada nam zatreba,
    odnosno u poslednjem trenutku.

    Polazimo od toga da se najverovatnije ocene mnogo češće upisuju i brišu u
    odnosu na potrebu za pristupom proseku. Postavlja se pitanje da li možemo da
    proredimo računanje proseka? Možemo, jer je prosek potrebno računati jedino
    kada postoji potreba da se dobavi pa poziv metode za računanje proseka
    izmeštamo u property (odnosno getter).

    Primetićemo da je vrednost proseka veći deo vremena neažurna, odnosno ne
    odgovara realnom proseku ocena.
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
        self._calculate_average_grade()
        return self._average

    def print(self):
        print("Student " + self._first_name + " " + self._last_name + " ima prosek " + str(self._average))

    def _calculate_average_grade(self):
        self._average = sum(self._grades)/len(self._grades)

    def add_grade(self, new_grade):
        self._grades.append(new_grade)

    def remove_grade(self, grade):
        self._grades.remove(grade)
