"""
Modul sadrži implementaciju stabla.
"""
from my_queue import Queue
from tree_node import TreeNode


class Tree(object):
    """
    Klasa modeluje stablo.
    """
    def __init__(self):
        self.root = None

    def is_empty(self):
        """
        Metoda proverava da li stablo ima elemenata.
        """
        return self.root is None

    def depth(self, node):
        """
        Metoda izračunava dubinu zadatog čvora.

        Argument:
        - `x`: čvor čija dubina se računa
        """
        if node.is_root():
            return 0
        else:
            return 1 + self.depth(node.parent)

    def _height(self, node):
        """
        Metoda izračunava visinu podstabla sa zadatim korenom.

        Argument:
        - `x`: koren posmatranog podstabla
        """
        if node.is_leaf():
            return 0
        else:
            return 1 + max(self._height(child) for child in node.children)

    def height(self):
        return self._height(self.root)

    def preorder(self, node):
        """
        Preorder obilazak po dubini

        Najpre se vrši obilazak roditelja a zatim svih njegovih potomaka.

        Argument:
        - `x`: čvor od koga počinje obilazak
        """
        if not self.is_empty():
            print(node.data)
            for child in node.children:
                self.preorder(child)

    def postorder(self, node):
        """
        Postorder obilazak po dubini

        Najpre se vrši obilazak potomaka a zatim i roditelja

        Argument:
        - `x`: čvor od koga počinje obilazak
        """
        if not self.is_empty():
            for child in node.children:
                self.postorder(child)
            print(node.data)

    def breadth_first(self):
        """
        Metoda vrši obilazak stabla po širini.
        """
        to_visit = Queue()
        to_visit.enqueue(self.root)
        while not to_visit.is_empty():
            e = to_visit.dequeue()
            print(e.data)

            for child in e.children:
                to_visit.enqueue(child)

    def __iter__(self):
        current = self.root
        return self._iterate_recursively(current)

    def _iterate_recursively(self, node):
        yield node
        for child in node.children:
            if not child.is_leaf():
                for subnode in self._iterate_recursively(child):
                    yield subnode
            else:
                yield child


if __name__ == '__main__':
    # instanca stabla
    t = Tree()
    t.root = TreeNode(3)

    # kreiranje relacija između novih čvorova
    a = TreeNode(7)
    b = TreeNode(4)
    c = TreeNode(2)
    d = TreeNode(9)
    e = TreeNode(6)
    f = TreeNode(5)

    t.root.add_child(a)
    t.root.add_child(b)
    a.add_child(c)
    a.add_child(d)
    a.add_child(e)
    d.add_child(f)

    for node in t:
        print(node)


    # visina stabla
    print('Visina = %d' % t.height())

    # dubina čvora
    print('Dubina(a) = %d' % t.depth(a))

    # obilazak po dubini - preorder
    print('PREORDER')
    t.preorder(t.root)

    # obilazak po dubini - postorder
    print('POSTORDER')
    t.postorder(t.root)

    # obilazak po širini
    print('BREADTH FIRST')
    t.breadth_first()
