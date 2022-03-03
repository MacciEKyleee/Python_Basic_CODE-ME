"""
Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
(N podane przez użytkownika, ale nie większe niż 8).

"""

print("Podaj liczbę naturalną nie większą niż 8.")
liczba=int(input())
if liczba>8 :
    print("Podałeś liczbę większą niż 8")
else:
    k=1
    for i in range(1,(liczba+1)):
        k=k*i
        print(i, "silnia wynosi:",k)

"""
print("Podaj liczbę naturalną nie większą niż 8.")
liczba = int(input())
while liczba > 8:
    print("Podałeś liczbę większą niż 8")
else:
    k = 1
    for i in range(1, (liczba + 1)):
        k = k * i
        print("Silnia wynosi:", k)
"""