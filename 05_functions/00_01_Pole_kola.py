"""
1▹ Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.

"""
# def field(r):
#     pi=3.14
#     return pi * (r**2)
#
# area = field(12)
# print('Pole to: ',area)

# def field(r):
#     pi=3.14
#     print('Pole: ', pi * (r**2))
#
# radius = float(input('Podaj promień ->'))
# area = field(radius)

def field():
    r = float(input('Podaj promień ->'))
    pi = 3.14
    print('Pole: ', pi * (r**2))