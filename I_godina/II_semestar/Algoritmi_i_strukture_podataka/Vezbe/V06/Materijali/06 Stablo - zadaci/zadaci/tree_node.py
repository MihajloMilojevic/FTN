class TreeNode(object):
    """
    Klasa modeluje čvor stabla.
    """
    __slots__ = '_parent', '_children', '_data'

    def __init__(self, data):
        """
        Konstruktor.

        Argument:
        - `data`: podatak koji se upisuje u čvor
        """
        self._parent = None
        self._children = []
        self._data = data

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        self._children = value

    def is_root(self):
        """
        Metoda proverava da li je čvor koren stabla.
        """
        return self.parent is None

    def is_leaf(self):
        """
        Metoda proverava da li je čvor list stabla.
        """
        return len(self.children) == 0

    def add_child(self, x):
        """
        Metoda dodaje potomka čvoru.

        Argument:
        - `x`: čvor potomak
        """
        # kreiranje dvosmerne veze između čvorova
        x.parent = self
        self.children.append(x)

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)

    print(b)
