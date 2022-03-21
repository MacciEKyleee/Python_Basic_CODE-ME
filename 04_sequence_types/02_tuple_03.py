"""
3▹ Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby.
Jeśli liczba znajduje się na krotce wyswietl jej indeks.

"""
import random
print('')
print('Stworzymy krotkę z 20 wylosowanymi liczbami całkowitymi z zakresu - 50 do 50.')
print('Podaj proszę liczbę całkowitą. Jeżeli znajduje się na liście - program poda jej indeks.')
print('')

list=[]
n=0
i=0

while i<=20:
    k = random.randint(-50,50)

    if k in list:
        continue
    else:
        list.append((k))
        i = i + 1
#print(list)
tuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
for  i in range(0,21):
    tuple = (list[i],) + tuple[:i]
print(tuple)

print('Podaj liczbę całkowitą: ')
x = int(input())
if x in list:
    print('Liczba ta znajduje się na pozycji:', (tuple.index(x)+1))
else:
    print('Liczby tej nie ma w krotce.')



        #
        # if isinstance(k, int) == True:
        #     integer = int(k)
        #     n = n + 1
        #     i = i + 1
        #     list.append(integer)
        # else:
        #     print('Podałeś element, który nie jest liczbą całkowitą.')
