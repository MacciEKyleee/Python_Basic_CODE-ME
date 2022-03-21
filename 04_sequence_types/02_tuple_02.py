"""
2▹ Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.
"""
print('')
print('Stworzymy listę z elementami, które podasz.')
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

list_check = []
presence = []
for element in list:
    if element not in list_check:
        list_check.append(element)
    else:
        presence.append(element)

print('Powtarzają się elementy: ',presence)