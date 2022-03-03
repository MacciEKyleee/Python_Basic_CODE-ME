"""
Zapytaj użytkownika o numer od 1 do 100,
jeśli użytkownik zgadnie liczbę ukrytą przez programistę
wyświetl komunikat “gratulacje!”,
 w przeciwnym razie wyświetl “pudło!”.
"""
print("")
print("Proszę podaj cyfrę/liczbę od 1 do 100. Może uda Ci się trafić :)")
digit=int(input())
print("")

if digit==39:
    print("Gratulacje!")
else:
    print("Pudło!")