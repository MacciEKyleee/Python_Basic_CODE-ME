"""
4▹ Napisz grę - kamień (k) / papier (p) / nożyce (n).

Użytkownik podaje jedną z 3 figur.

Komputer losuje jedną z 3 figur.

Sprawdź kto wygrał tę rundę.

Zmień kod tak, by użytkownik mógł podac liczbę rund.

Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.

Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’
"""

import random
print("")
print('Zagrajmy w grę kamień (k), papier (p), nożyce (n).')
print('Jeżeli chcesz zakończyć grę - napisz komendę "koniec".')

print("")
k='kamień'
p='papier'
n='nożyce'

#print('Proszę podaj co wybierasz wpisująć odpowiednią literę:kamień (k), papier (p), nożyce (n).')


c=0
h=0
i=0

print("Podaj liczbę rund jaką chcesz rozegrać w grę: ")
digit=int(input())
print("")

while (i<digit):
    print('Proszę podaj co wybierasz wpisująć odpowiednią literę:kamień, papier, nożyce.')
    choice = str(input())

    if choice=='koniec':
        break
    else:
        print('Twój wybór: ', choice)

    computer = random.choice(['kamień', 'papier', 'nożyce'])
    print('Wybór komputera: ', computer)
    print("")
    if (choice=='kamień' and computer=='kamień'):
        print('To była runda numer: ',(i+1))
        print('W tej rundzie jest remis !')
        i=i+1
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice=='kamień' and computer=='papier'):
        print('To była runda numer: ',(i+1))
        print('W tej rundzie wygrał komputer !')
        i=i+1
        c=c+1
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice == 'kamień' and computer == 'nożyce'):
        print('To była runda numer: ',(i+1))
        print('W tej rundzie wygrałeś TY!!')
        i=i+1
        h = h + 1
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice=='papier' and computer=='papier'):
        print('To była runda numer: ',(i+1))
        print('W tej rundzie jest remis !')
        i=i+1
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice == 'papier' and computer == 'nożyce'):
        print('To była runda numer: ',(i+1))
        print('W tej rundzie wygrał komputer !')
        i=i+1
        c=c+1
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice == 'papier' and computer == 'kamień'):
        print('To była runda numer: ',(i+1))
        print('W tej rundzie wygrałeś TY!!')
        i=i+1
        h = h + 1
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice=='nożyce' and computer=='nożyce'):
        print('To była runda numer: ',(i+1))
        print('W tej rundzie jest remis !')
        i=i+1
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice == 'nożyce' and computer == 'kamień'):
        print('To była runda numer: ',(i+1))
        print('W tej rundzie wygrał komputer !')
        i=i+1
        c=c+1
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice == 'nożyce' and computer == 'papier'):
        print('To była runda numer: ',(i+1))
        print('W tej rundzie wygrałeś TY!!')
        i=i+1
        h = h + 1
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")


#computer=choice([k,p,n])
#print(computer)
