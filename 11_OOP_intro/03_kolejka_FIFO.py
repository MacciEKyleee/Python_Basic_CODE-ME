"""
3▹ Stwórz własną implementację kolejki FIFO.
Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
Wśród metod powinny się znaleźć takie jak:
    wyswietlenie kolejki,
    sprawdzenie czy jest pusta,
    dodanie elementu do kolejki (put),
    wyjęcie elementu z kolejki (get).

Utwórz kilka obiektów klasy Queue z różnymi parametrami.
"""
class queue():  #class
    def __init__(self, fifo):
        self.fifo = fifo

    def show(self):
        return self.fifo

    def is_empty(self):
        # if len(self.fifo) == 0:
        # # self.fifo == []
        #     return True
        # else:
        #     return False
        return len(self.fifo) == 0

    def put(self, element):
        self.fifo.append(element)

    def get(self):
        element = self.fifo.pop(0)
        return element

#example_queue = queue([4, 5, 35, 12, 3])
example_queue = queue([])
example_queue.show()
print(example_queue.is_empty())
example_queue.put(6)
example_queue.put(31)
example_queue.put(61)
example_queue.show()
print('====get====')
print(example_queue.get())
example_queue.show()