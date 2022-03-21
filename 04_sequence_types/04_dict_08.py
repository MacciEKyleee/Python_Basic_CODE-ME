"""
8▹ Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem.
Nowa lista powinna zawierać 100 elementów.

Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.
"""
# names = 'European_names.csv'
#
# def get_quotes():
#     with open(names) as fopen:
#         quotes = fopen.readlines()
#     return quotes
#
# # funkcja wyświetlająca
# def show(content):
#     quote = random.choice(content).strip()
#     quote = quote.split(';')
#
# # main code
#
# quotes_list = get_quotes()
# show(quotes_list)


Germany = ['Emilia','Hannah/Hanna','Emma','Sophia/Sofia','Mia','Lina','Mila','Ella','Lea/Leah','Klara/Clara']
France = ['Jade','Louise','Emma','Alice','Ambre','Lina','Rose','Chloe','Mia','Lea']
England = ['Olivia','Amelia','Isla','Ava','Mia','Ivy','Lily','Isabella','Sophia','Rosie']
Italy = ['Sofia','Giulia','Aurora','Ginevra','Alice','Beatrice','Emma','Giorgia','Vittoria','Matilde']
Ukraine = ['Sofiya','Zlata','Mariya','Solomiya','Anastasiya','Anna','Khrystyna','Marharyta','Milana','Polina']
Spain = ['Lucía','Sofía','Martina','María','Julia','Paula','Valeria','Emma','Daniela','Carla']
Poland = ['Zuzanna','Zofia','Hanna','Julia','Maja','Laura','Oliwia','Alicja','Lena','Pola']
Romania = ['Sofia','Amelia','Anastasia','Maria','Victoria','Daria','Eva','Alexandra','Evelina','Andreea']
Netherlands = ['Julia','Mila','Emma','Nora','Olivia','Sophie','Tess','Milou','Zoë','Yara']
Greece = ['Maria','Eleni','Aikaterini','Vasiliki','Sophia','Angeliki','Georgia','Dimitra','Konstantina','Paraskevi']

dictionary = [England,France,Germany,Greece,Italy,Netherlands,Poland,Romania,Spain,Ukraine]
# print(dictionary)
# print(dictionary.count('England'))
list=[]
for element in dictionary:
    list.extend(element)
print(list)

important = []

for element in list:
    if (list.count(element)>=3):
        important.append(element)
    else:
        continue

print(important)