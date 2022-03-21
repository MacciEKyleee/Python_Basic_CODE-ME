"""
3▹ Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

"""
# def max(a,b,c):
#     centre = ((a+b+c)/3)
#     if a > centre:
#         print('Maksymalna jest liczba a')
#     elif b > centre:
#         print("Maksymalna jest liczba b")
#     else:
#         print('Maksymalna jest liczba c')
#
# a = int(input('Podaj liczbę a:'))
# b = int(input('Podaj liczbę b:'))
# c = int(input('Podaj liczbę c:'))
# max(a,b,c)

# def max(a,b,c):
#     if a > b and a > c :
#         print('Największa liczbą jest: ',a)
#     elif b > a and b > c:
#         print('Największa liczbą jest: ',b)
#     else:
#         print('Największa liczbą jest: ',c)

#print('Największe wartość z pośród 200,30,1 to: ', max(200,30,1))

def max_of(x,y):
    return x if x > y else y
def maximum_of(a,b,c):
    result = max_of(a,b)
    return max_of(result,c)

print('Najwięskza wartość to', maximum_of(44,33,22))