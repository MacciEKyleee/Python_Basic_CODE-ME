"""
4▹ Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.
"""


def ask():
    q1 = int(input('Podaj zakres dolny: \n'))
    q2 = int(input('Podaj zakres górny \n'))
    szukana = int(input('Podaj liczbę \n'))
    return q1, q2, szukana


def test(a, b):
    return (a, b) if (a < b) else ((b, a))


def group(a, b, x):
    (a, b) = test(a, b)
    if (x >= a and x <= b):
        print('Dolny zakres', a, 'Górny zakres', b)
        print('Tak, liczba x znajduje się w zadanym zakresie. \n')

    else:
        print('Dolny zakres', a, 'Górny zakres', b)
        print('Nie, liczba x jest z poza zakresu. \n')


(m, n, x) = ask()
sprawdzenie = group(m, n, x)
