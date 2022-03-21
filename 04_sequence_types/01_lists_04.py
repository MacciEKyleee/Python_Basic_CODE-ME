"""
4▹ Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.
"""
print('')
print('Stworzymy listę z liczbami, które podasz.')
print('Jeżeli dodasz już wszystkie elementy ciągu wpisz: "KONIEC".')

print('')
list=[]
n=0
i=0

while i>=0:
    print("Podaj ",(i+1),'element ciągu:')
    k=input()
    k=k.upper()
    if k == "KONIEC":
        i = i + 1
        break
    else:
        n = n + 1
        i = i + 1
        list.append(k)



if n%2==0:
    print('Liczba jest parzysta.')
else:
    print('Podałeś nieparzystą liczbę elementów.\n\nPodaj conajmniej jeszcze jeden:')
    g = input()
    list.append(g)

print('Twoja lista wygląda następująco:', list)
print('')

center_1 = ((i//2)-1)
center_2 = (i//2)

print('Dwa elementy środkowe to :',list[center_1],' i ',list[center_2],'.')
if list[center_1] == list[center_2]:
    print('Elementy te są sobie równe.')
else:
    print('Elementy te nie są sobie równe.')