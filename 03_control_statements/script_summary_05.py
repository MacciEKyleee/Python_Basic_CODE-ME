"""
5▹ Stwórz grę ciepło zimno.

Komputer losuje liczbę z zakresu od 1 do 100.
Użytkownik podaje swój traf.
Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
Jeśli użytkownik zgadnie wygrywa gracz.
Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.
"""
import random
print("")
print("Zagrajmy w grę ciepło zimno. Komputer wylosuję cyfrę/liczbę z zakresu od 1 do 100.")
print("Twoim zadaniem jest w 6 próbach odnaleźć wylosowaną cyfrę/liczbę.")
print("")

digit=random.randint(1,100)
sdigit=int(digit)
print(sdigit)

ldigit=round(((sdigit*9)//10),0)
print(ldigit)

h_0=1,1*sdigit
hdigit=round(((sdigit*11)//10),0)
print(hdigit)
#print(digit)


k=0
while k<6:
    print("")
    print("Podaj swój szczęśliwy traf.")
    user = int(input())
    print("")

    if (user==sdigit):
        print("Wygrywasz grę")
        break
    elif ((user<(ldigit))or(user>(hdigit))):
        print("Zimno :( ")
        k=k+1
        if k==6:
            print("Niestety przegrałeś :( ")
        else:
            print("Gramy dalej.")
            print("Pozostało Ci jeszcze: ", 6-k,'prób')
    elif (user>=(ldigit) and user<=(hdigit)):
        print("Ciepło! ")
        k = k + 1
        if k==6:
            print("Niestety przegrałeś :( ")
        else:
            print("Gramy dalej.")
            print("Pozostało Ci jeszcze: ", 6-k,'prób')







