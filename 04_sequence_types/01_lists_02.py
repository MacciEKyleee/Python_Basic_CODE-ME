"""
2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
"""
print('')
print('Stworzymy listę z 10 liczbami, które podasz.')
print('')
list=[]
i=0
while i<10:
    print("Podaj ",(i+1),'element ciągu:')
    k=input()
    list.append(k)
    i=i+1
print('Twoja lista wygląda następująco:', list)
print('')
print('Wyświetlę Ci elementy nieparzyste: ')

list_2=[]
for i in list:
    if ((int(i))%2)==1:
        list_2.append(i)
    else:
        continue
print(list_2)