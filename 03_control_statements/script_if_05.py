"""
Stwórz zmienną password.
Hasło powinno składać z liter i cyfr,
zwierać conajmniej 1 dużą literę i
mieć długość conajmniej 8 znaków.
Poinformuj użytkownika,
jeśli wpisane hasło jest nie poprawne.
Wyświetl różne komunikaty w zależności
od rodzaju błędu.
"""

print("")
print("Prosimy o podanie hasła.")
print("Hasło powinno składać z liter i cyfr,zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.")
print("Hasło nie powinno zawierać znaków specjalnych takich jak: !, &, ^, %, $, #.")


password=str(input())
print("")

if len(password)<8:
    print("Hasło nie ma 8 znaków.")
elif password.isalpha()==True:
    print("Hasło nie zawiera liter")
elif password.isdigit() == True:
    print("Hasło nie zawiera cyfr")
elif password.islower() == True:
    print("Hasło nie zawiera dużej litery")
elif password.isupper() == True:
    print("Hasło nie zawiera małej litery")
elif password.__contains__('!' or '&' or '^' or '%' or '$' or '#'):
        print('Haslo zawiera znak specjalny !')
else:
    print("Hasło jest silne.")