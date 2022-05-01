"""
5▹ Napisz grę ciepło - zimno tak, aby korzystać z funkcji.
"""
import random


def ask():
    x = int(input('Podaj liczbę: \n'))
    return x


def test():
    # a = randint(0,20)
    # b = randint(21,40)
    a = 18
    b = 23
    # c = randint(a,b)
    c = 20
    return c


def game(wylosowana, szukana):
    max = int(1.5 * wylosowana)
    min = int(0.5 * wylosowana)
    a = int(wylosowana + 1)
    b = int(wylosowana - 1)

    if (szukana > (max)):
        return ('Bardzo zimnooooo - dużo mniejsza')
    elif (szukana < (max)) & (szukana > a):
        return ('Zimno - trochę mniejsza')
    elif (a > szukana & szukana > b):
        return ('Ciepło - już prawie!')
    elif (szukana > (min)) & (szukana < b):
        return ('Zimno - trochę większa')
    elif (szukana < (min)):
        return ('Bardzo zimnooooo - dużo większa')
    else:
        return ('Brawo to ta liczba ! ')


c = test()
x = ask()

while (c != x):
    print(game(c, x))
    print('\nWpisz ponownie szukaną liczbę. \n')
    print('------------------')
    x = ask()
print('Brawo - to ta liczba!')
