"""
1▹ Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
Elementy na liście posortuj alfabetycznie, a następnie wyświetl.
"""
list=['mapa','kompas','buty górskie','plecak','woda','czapka','kurtka']
list_2=list.copy()
list_2.sort()
print(list_2)
for row in list_2:
    print(row)