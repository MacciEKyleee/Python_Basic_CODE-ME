"""
2▹ Stwórz moduł, który przechowuje wzór na deltę.
Skorzystaj z wbudowanego modułu math.
W nowym pliku wykorzystaj moduł.
"""
import delta as det

def get_three_values():
    a = int(input('Podaj wartość a: '))
    b = int(input('Podaj wartość b: '))
    c = int(input('Podaj wartość c: '))
    return a, b, c


if __name__ == '__main__':
    print('')
    a, b, c = get_three_values()

    print('Delta wynosi:', det.delta(a,b,c))