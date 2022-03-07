"""
5▹ Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób,
natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
"""
people=[['Piotr','Kowalski','malarz'],['Mariusz','Nowak','artysta'],['Karolina','Bukowska','astronauta']]
for row in people:
    print(row[0],row[1],row[2])

for row in people:
    print('**********')
    for elem in row:
        print(elem, end=' ')
    print('')