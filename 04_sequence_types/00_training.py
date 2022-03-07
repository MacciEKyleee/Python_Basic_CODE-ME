#veggies=['carrot','kale','peas']
#del veggies
#veggies

  #  range(10)
 #   range(0,10)
  #  zakres=range(4,20,3)
 #   print(zakres)
  #  range((4,20,3)
  #  type(zakres)


# 1. Metoda, która utworzy kopię listy?
list=[1,2.3,2,4,2,7,2,]
list_2=list.copy()
print(list_2)
#deep.copy - co to jest?
# 2. Metoda, która posortuje elementy na liście?
list_2.sort()
print(list_2)

# 3. Jaka metoda usunie wszystkie elementy z listy?
list_2.clear()
print('Wyczyszczona lista: ',list_2)

# 4. Policzy wystąpienia takiego samego elementu na liście?
#   list=[1,2.3,2,4,2,7,2,]#2->4
print(list.count(2))

# 5. Zsumuje liczby na liście?
print(sum(list))