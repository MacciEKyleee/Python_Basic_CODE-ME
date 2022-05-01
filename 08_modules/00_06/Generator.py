"""
6▹ Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz jej długość np.
Wejście:
    var = ‘banannnnannnnnnnnnanananananaaaana’
Wyjście
    ‘nnnnnnnnn’, 9
1. Utwórz generator instancji testowych, który wygeneruje losowe ciągi znaków składające się z jedynie z cyfr od 0-9.
    Upewnij się, że conajmniej 2 takie same znaki znajdą się w sekwencji.
2. Zmodyfikuj generator tak, by oczekiwał znaków podanych przez użytkownika np. użytkownik podaje 4 znaki: ‘a’, ‘b’, ‘c’, ‘*’.
3. Zaimportuj generator bezpośrednio do programu.

"""
import random

def main():
    x = range(10)
    y = random.choices(x,k= 10)
    additional_number = random.choice(y)
    additional_number_int = int(additional_number)
    y.append(additional_number_int)
    print(y)

def instance_generator():
    x = input("Podaj 4 znaki: ")
    y = random.choices(x,k= 10)
    y2 = ""
    for i in y:
        y2 += i
    return y2

if __name__ == "__main__":
    main()