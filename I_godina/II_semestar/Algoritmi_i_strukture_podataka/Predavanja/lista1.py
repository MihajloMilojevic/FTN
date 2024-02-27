class Node:
    def __init__(self, element, next):
        self._element = element
        self._next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, elem):  # O(1)
        node = Node(elem, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node

    def append(self, elem):  # O(1)
        node = Node(elem, None)
        if self.tail is not None:
            self.tail._next = node
            self.tail = node
        else:
            self.tail = self.head = node

    def remove_first(self):  # O(1)
        if self.head is None:
            raise Exception('Lista je prazna')
        self.head = self.head._next
        if self.head is None:
            self.tail = None

    def remove_last(self):  # O(n)
        if self.tail is None:
            raise Exception('Lista je prazna')
        if self.head == self.tail:
            self.head = self.tail = None
            return
        current = self.head
        while current._next != self.tail:
            current = current._next
        current._next = None
        self.tail = current

    def traverse(self, func):  # O(n)
        current = self.head
        while current is not None:
            func(current._element)
            current = current._next

    def has_common_elem(self, other):  # O(1)
        if self.tail is None or other.tail is None:
            return False
        return self.tail == other.tail

lista1 = LinkedList()
lista1.insert(1)
lista1.insert('dva')
lista1.insert({'value': 3})
lista1.traverse(print)
lista1.remove_first()
print('---')
lista1.traverse(print)
lista1.remove_last()
print('---')
lista1.traverse(print)

lista2 = LinkedList()
lista2.insert('dva')

print(lista2.has_common_elem(lista1))

