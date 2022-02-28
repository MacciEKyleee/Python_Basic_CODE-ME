"""
Stwórz skrypt, który przyjmuje 3 opinie
użytkownika o książce.
Oblicz średnią opinię o książce.
W zależności od wyniku dodaj komunikaty.
Jeśli uzytkownik ocenił książkę na ponad
7 - bardzo dobry,
ocena 5-7 przeciętna,
4 i mniej - nie warta uwagi.
"""

print("Oceń przeczytaną książkę w skali 1-10")
print("")
print("Twoja ocena czytelniku pierwszy:")
rate1=int(input())

print("")
print("Twoja ocena czytelniku drugi:")
rate2=int(input())

print("")
print("Twoja ocena czytelniku trzeci:")
rate3=int(input())
print("")

rate=(rate1+rate2+rate3)//3

if rate>=7:
    print("Bardzo dobra.")
elif rate>=5:
    print("Przeciętna.")
else:
    print("Nie warta uwagi.")