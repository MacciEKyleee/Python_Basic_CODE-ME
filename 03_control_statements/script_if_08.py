"""
Sortowanie.
Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.
"""
print("")
print("W ramach zadania posortujemy 3 zmienne wskazane przez Panią/Pana.")
print("")
print("Proszę o wskazanie pierwszej zmiennej numerycznej (liczba).")
digit_1=int(input())
print("")
print("Proszę o wskazanie drugiej zmiennej numerycznej (liczba).")
digit_2=int(input())
print("")
print("Proszę o wskazanie trzeciej zmiennej numerycznej (liczba).")
digit_3=int(input())
print("")

if digit_1>digit_2:
    if digit_1>digit_3:
        print("Największa jest liczba podana jako pierwsza,czyli: ", digit_1)
        if digit_2>digit_3:
            print("Kolejność podanych liczb:",digit_1,digit_2,digit_3)
        else:
            print("Kolejność podanych liczb:",digit_1,digit_3,digit_2)
    else:
        print("Największa jest liczba podana jako trzecia,czyli: ",digit_3)
        print("Kolejność podanych liczb:",digit_3,digit_1,digit_2)
elif digit_2>digit_3:
    print("Największa jest liczba podana jako druga,czyli: ",digit_2)
    if digit_1>digit_3:
        print("Kolejność podanych liczb:", digit_2, digit_1, digit_3)
    else:
        print("Kolejność podanych liczb:", digit_2, digit_3, digit_1)
else:
    print("Największa jest liczba podana jako trzecia,czyli: ", digit_3)
    print("Kolejność podanych liczb:", digit_3, digit_2,digit_1)





