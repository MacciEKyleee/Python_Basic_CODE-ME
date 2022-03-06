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
print("")
k='kamień'
p='papier'
n='nożyce'

#print('Proszę podaj co wybierasz wpisująć odpowiednią literę:kamień (k), papier (p), nożyce (n).')



h=0
c=0
while (h<3 and c<3):
    print('Proszę podaj co wybierasz wpisująć odpowiednią literę:kamień, papier, nożyce.')
    choice = str(input())

    print('Twój wybór: ', choice)
    computer = random.choice(['kamień', 'papier', 'nożyce'])
    print('Wybór komputera: ', computer)
    print("")
    if (choice=='kamień' and computer=='kamień'):
        print('W tej rundzie jest remis !')
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice=='kamień' and computer=='papier'):
        print('W tej rundzie wygrał komputer !')
        c=c+1
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice == 'kamień' and computer == 'nożyce'):
        print('W tej rundzie wygrałeś TY!!')
        h = h + 1
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice=='papier' and computer=='papier'):
        print('W tej rundzie jest remis !')
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice == 'papier' and computer == 'nożyce'):
        print('W tej rundzie wygrał komputer !')
        c=c+1
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice == 'papier' and computer == 'kamień'):
        print('W tej rundzie wygrałeś TY!!')
        h = h + 1
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice=='nożyce' and computer=='nożyce'):
        print('W tej rundzie jest remis !')
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice == 'nożyce' and computer == 'kamień'):
        print('W tej rundzie wygrał komputer !')
        c=c+1
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")
    elif (choice == 'nożyce' and computer == 'papier'):
        print('W tej rundzie wygrałeś TY!!')
        h = h + 1
        print('Aktualny wynik to: Ty ',h,'komputer ',c)
        print("")

#computer=choice([k,p,n])
#print(computer)