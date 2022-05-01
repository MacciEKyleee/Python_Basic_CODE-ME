""""
2▹ Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).
"""
def min_of(x,y):
    return x if x < y else y
def minimum_of(a,b,c):
    result = min_of(a,b)
    return min_of(result,c)

print('Najmniejsza wartość to', minimum_of(44,33,22))