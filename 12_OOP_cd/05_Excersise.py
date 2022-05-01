"""
5▹ Stwórz abstrakcyjną klasę Pojazdy.
Utwórz potomne klasy pojazdy np. Samochód, Rower, Autobus, Ciężarówki.
 Dodaj opisy zgodne z tym jak te pojazdy są klasyfikowane.
 Jaki rodzaj dokumentu jest potrzebny, by kierować poszczegolnym pojazdem.

"""
from abc import ABC, abstractmethod

class vehicles(ABC):
    @abstractmethod
    def desc(self):
        pass
    @abstractmethod
    def require_driving_licence(self):
        pass

class car(vehicles):
    def desc(self):
        return 'Car is ....'

    def require_driving_licence(self):
        return 'cat. B'

    def __repr__(self):
        return f'Car-licence {self.require_driving_licence()}'

class bicycle(vehicles):
    def desc(self):
        return 'I love my bike ....'
    def require_driving_licence(self):
        return 'bike card'

    def __repr__(self):
        return f'Bike-licence {self.require_driving_licence()}'
class bus(vehicles):
    def type_of_document(self):
        return 'Category: D or D1'

class truck(vehicles):
    def type_of_document(self):
        return 'Category: C or C1'

Honda = car()
print(Honda)

Kross=bicycle()
print(Kross)
print(Kross.desc())