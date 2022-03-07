"""
3▹ Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n. Elementy powinny być oddzielone spacją

wejście:

n = 3

tab = [['-', '-', '-']
  ['-', '-', '-'],
  ['-', '-', '-']]
wyjście:

- - -
- - -
- - -
"""
print('Podaj wymiar tablicy.')
n = int(input())
tab = [['-'] * n] * n
print(tab)
print('')
print('Wyjście:')
for row in tab:
    for element in row:
        print(element, end=' ')
    print()
