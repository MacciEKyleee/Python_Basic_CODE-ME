import math
# def get_three_values():
#     a = int(input('Podaj wartość a: '))
#     b = int(input('Podaj wartość b: '))
#     c = int(input('Podaj wartość c: '))
#     return a, b, c

def delta(a,b,c):
    delta = (b*b)-(4*a*c)
    return delta

# if __name__ == '__main__':
#     print('')
#     a, b, c = get_three_values()
#     print('Delta wynosi:', delta(a,b,c))