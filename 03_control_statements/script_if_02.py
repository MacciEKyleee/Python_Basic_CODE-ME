"""
Pobierz dwie liczby całkowite od użytkownika
i oblicz ich sumę.
Jeśli suma jest większa niż 100,
wyświetl wynik,
w przeciwnym wypadku wyświetl “Koniec”.


"""

print("Proszę o podanie pierwszej liczby.")
print("")
number1=int(input())
print("")

print("Proszę o podanie drugiej liczby.")
print("")
number2=int(input())
print("")

suma=number1+number2
if suma>100:
    print(suma)
else:
    print("Koniec.")