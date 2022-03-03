"""
2) Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.
"""
print("")
print("Zagrajmy w grę.")
print("")
print("Aby wygrać grę, musisz odgadnąć liczbę z zakresu od 0 do 20.")
print("")
print("Gotowa/y? Podaj liczbę:")
num_u=int(input())
print("")
secret_num=5

while num_u!=secret_num:
    while num_u<0 or num_u>20:
        print("Nie podałeś liczby z zakresu 0 do 20. Podaj inną liczbę.")
        num_u = int(input())
    print("Niestety - to nie ta liczba. Podaj inną liczbę:")
    num_u = int(input())
    print("")
print('Brawo! Udało Ci się trafić.')