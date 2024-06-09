"""
Modul sadrži implementaciju min heapa
"""
from pqueue import PQItem, PQError
import random
import time


class MinHeap(object):

    def __init__(self, data=None):
        if data is None:
            self._data = []
            self._heap_size = 0
        else:
            self._data = data
            self._heap_size = len(self._data)
            self._build_min_heap()

    def _left(self, index):
        """
        Metoda izračunava indeks levog potomka čvora.

        Argument:
        - `i`: indeks čvora čiji se potomak računa
        """
        return index*2+1

    def _right(self, index):
        """
        Metoda izračunava indeks desnog potomka čvora.

        Argument:
        - `i`: indeks čvora čiji se potomak računa
        """
        return index*2+2

    def _parent(self, index):
        """
        Metoda izračunava indeks roditelja čvora.

        Argument:
        - `i`: indeks čvora čiji se roditelj računa
        """
        return (index-1)//2

    def _swap(self, a, b):
        """
        Metoda menja vrednosti čvorova sa zadatim indeksima.

        Argument:
        - `a`: indeks prvog čvora
        - `b`: indeks drugog čvora
        """
        self._data[a], self._data[b] = self._data[b], self._data[a]

    def add(self, key, value=None):
        """
        Metoda dodaje novi element u heap
        :param key: prioritet novog čvora
        :param value: vrednost novog čvora
        """
        new_item = PQItem(key, value)
        self._data.append(new_item)
        self._heap_size += 1
        self._upheap(len(self._data)-1)

    def _upheap(self, index):
        """
        Metoda postavlja čvor na ispravnu poziciju poređenjem sa roditeljem
        :param index: pozicija čvora
        """
        parent_index = self._parent(index)
        if parent_index < 0 or self._data[index] > self._data[parent_index]:
            return
        self._swap(index, parent_index)
        self._upheap(parent_index)

    def min(self):
        """
        Pronalazi i vraća najmanji element heap-a
        :return: uređeni par (prioritet, vrednost) za minimalni element
        """
        if self.is_empty():
            raise PQError("Heap je prazan")
        return self._data[0].key, self._data[0].value

    def remove_min(self):
        """
        Uklanaj i vraća najmanji element heap-a
        :return: uređeni par (prioritet, vrednost) za minimalni element
        """
        if self.is_empty():
            raise PQError("Heap je prazan")

        self._swap(0, self._heap_size-1)
        ret_node = self._data.pop(self._heap_size-1)
        self._heap_size -= 1

        self._downheap(0)
        return ret_node.key, ret_node.value

    def _downheap(self, index):
        """
        Metoda (ponovo) uspostavlja ispravan redosled elemenata heap-a. Od tri čvora (roditelj, levo i desno dete),
        pronalazi se najmanji i on se postavlja na poziciju roditelja. Postupak se ponavlja dok svi elementi heap-a
        ne dođu u ispravan poredak.
        :param index: pozicija za koju se utvrđuje element
        """
        left_child = self._left(index)
        right_child = self._right(index)

        min_index = index

        if left_child < self._heap_size and self._data[left_child] < self._data[index]:
            min_index = left_child

        if right_child < self._heap_size and self._data[right_child] < self._data[min_index]:
            min_index = right_child

        if min_index != index:
            self._swap(min_index, index)
            self._downheap(min_index)

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def _min_heapify(self, i):
        """
        Metoda formira max-heap od podstabla sa korenom u čvoru i.

        Argument:
        - `i`: indeks korena podstabla
        """

        # određivanje levog i desnog potomka čvora
        left = self._left(i)
        right = self._right(i)

        # provera levog potomka
        #   - da li je još na heapu
        #   - da li je podatak levog veći od podatka korena
        if left < self._heap_size and self._data[left] < self._data[i]:
            smallest = left
        else:
            smallest = i

        # provera desnog potomka
        if right < self._heap_size and self._data[right] < self._data[smallest]:
            smallest = right

        # zameni vrednosti ako nisu u max-heap redosledu
        if smallest != i:
            self._swap(i, smallest)
            self._min_heapify(smallest)

    def _build_min_heap(self):
        """
        Metoda vrši formiranje max heapa.
        """
        self._size = len(self._data)

        # svi elementi sa indeksom većim od n/2 biće listovi stabla
        start = (self._size - 1) // 2
        for i in range(start, -1, -1):
            self._min_heapify(i)

    def sort(self):
        """
        Heap sort algoritam
        """
        for i in range(self._size - 1, 0, -1):
            # zameni prvi i poslednji
            self._swap(0, i)

            # izbaci poslednji sa heapa
            self._heap_size -= 1

            # preostale elemente transformiši u max-heap
            self._min_heapify(0)


def compare(number_of_elements):
    print("="*50)
    print("This function compares duration of building heap\n by consecutive insertion vs heapify")

    print("Currently testing on %d elements..." % number_of_elements)
    print("=" * 50)

    test_array = [_ for _ in range(number_of_elements)]
    random.shuffle(test_array)

    start = time.process_time()
    heap = MinHeap()
    for key in test_array:
        heap.add(key, None)
    end = time.process_time()
    print("%-20s %10f" % ("Add to heap", end - start))

    start = time.process_time()
    MinHeap(test_array)
    end = time.process_time()
    print("%-20s %10f" % ("Heapify", end - start))


def main():
    heap = MinHeap()
    heap.add(5)
    heap.add(10)
    heap.add(7)
    heap.add(4)
    heap.add(6)

    print(heap.remove_min())
    heap.add(17)
    heap.add(1)
    heap.add(3)
    print(heap.min())
    print(heap.remove_min())
    print(heap.remove_min())


if __name__ == '__main__':
    compare(100000)





