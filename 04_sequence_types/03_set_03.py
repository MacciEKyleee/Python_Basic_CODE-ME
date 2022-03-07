"""
3▹ Utwórz 2 krotki.
Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki, a oraz nieparzystych elementów z drugiej.
Przekształć powstałą listę w set.
"""
element=('Asia','ma','Jasia','a','on','ma','Asia')
print('krotka 1:',element)
print('')
dog=('pies','Golden Retriever','Neska')
print('krotka 2:',dog)
print('')

tmp_list_1=list(element)
tmp_list_2=list(dog)
n=tmp_list_1 [0::2]
m=tmp_list_2 [1::2]

tmp_list_3=n+m
tmp_set = set(tmp_list_3)

print('Lista, która jest połączeniem elementów o parzystym indeksie z pierwszej krotki oraz elementów o nieparzystym indeksie z drugiej krotki: ')
print(tmp_set)