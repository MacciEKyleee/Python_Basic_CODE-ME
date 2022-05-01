# Stwórz własną implementację kolejki FIFO. Klasa kolejka (Queue) powinna na starcie przyjmować
# listę elementów. Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki,
# sprawdzenie czy jest pusta, dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).
# stack =/= queue
# stack -> first in / last out | słoik z sałatką
# queue -> first in / first out | kolejka na poczcie

class Queue():
    def __init__(self, fifo):
        self.fifo = fifo

    def show(self):
        print(self.fifo)

    def is_empty(self):
        return len(self.fifo) == 0

    def put(self, element):
        self.fifo.append(element)

    def get(self):
        element = self.fifo.pop(0)
        return element


example_queue = Queue([])
example_queue.show()
print(example_queue.is_empty())
example_queue.put(6)
example_queue.put(1)
example_queue.put(61)
example_queue.show()
print('====get ====')
print(example_queue.get())
example_queue.show()