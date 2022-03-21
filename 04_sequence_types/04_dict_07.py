"""
7▹ Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.

 example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
"""

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
print('\n Lista startowa: \n',example_list)
print('')
example_set = set(example_list)
#print('\nZestaw example: \n',example_set,' \n')

example_list_2 = list(example_set)
example_list_2.sort()
#print(example_list_2)
#example_list_2 = example_list_2.sort()
print('')
example_tuple = tuple(example_list_2)
print(example_tuple)

min = example_tuple[0]
max = example_tuple[-1]
print('\n Wartość minimalna wynosi:\n',min,'\nWartość maksymalna wynosi: \n',max)