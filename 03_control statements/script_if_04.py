"""
Utwórz zmienną przechowującą dowolny ciąg znaków.
Sprawdź czy utworzony string jest dłuższy niż 5
znaków oraz czy zawiera literę a.
Jeśli zawiera, wszystkie litery a podmień na z
i wyświetl powstały napis.
"""

print("Proszę napisz dowolne zdanie.")
variable=str(input())
print("")

long=len(variable)
if long>5:
    if variable.count("a")>0:
        variable1=variable.replace('a','z')
        print(variable1)