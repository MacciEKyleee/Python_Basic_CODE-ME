"""
Losowe zamek z Heroes 3.
"""
import random
lista = ['Castle','Rampart','Tower','Inferno','Necropolis','Dungeon','Stronghold','Fortress','Conflux','Cove']
while(True):
    choice = random.choice(lista)

    if choice == 'Inferno':
        print('\nWygląda, że Inferno - ale to jakiś żart, losujemy dalej!')
        continue
    else:
        print('\nDzisiaj zagramy zamkiem:\n')
        print(choice)
        break