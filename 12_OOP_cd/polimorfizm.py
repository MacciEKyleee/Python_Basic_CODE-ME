from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def poop(self):
        pass

class Horse(Animal):
    def poop(self):
        return 'emoji'

class Unicorn(Animal):
    def floof(self):
        return "I'm flying"
    def poop(self):
        return ''


#---
def vet(animal: Animal):    #type_hints
    print('Robie badanie -- >', animal.poop())



def main():
    print('Chodźmy do weterynarza')
    konik = Horse()
    jednorozec = Unicorn()

    vet(konik)
    vet(jednorozec)

if __name__=='__main__':
    main()