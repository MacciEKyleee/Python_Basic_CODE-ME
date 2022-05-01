"""
4▹ Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)
"""
def even_number(x):
    return ('To jest liczba parzysta') if x%2==0 else ('To jest liczba nieparzysta')
def testing(y):
    list=[]
    for element in s:
        if even_number(element) == 'To jest liczba parzysta':
            print(element)
        else:
            continue

s=[2,4,5,6,7,12,213,312,22,33,11]
testing(s)
