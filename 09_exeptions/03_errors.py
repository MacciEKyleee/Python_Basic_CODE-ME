"""
3▹ Stwórz listę 10 elementową (różne typy!).
Pozwól użytkownikowi podać dowolny index.
Podziel 1 przez liczbę pod indexem wybranym przez użytkownika.
Obsłuż błędy.
"""

list = [0,13,'string',2.45,True,('1','2'),[],{1,2},{'klucz':123},range(10),True]

try:
    k = int(input('Podaj dowolny indeks z listy:\n'))
    result = 1 / list[k]
    #print(10/i)
    print(result)

# except (TypeError,ZeroDivisionError):
#     print(list[k],'- nie może być dzielnikiem')
except (TypeError,IndexError) as e:
    print('Nie da rady')
except ValueError:
    print('LOL, to nie jest dobra wartość.')
except ZeroDivisionError:
    print('Pamiętaj ..... nie dziel przez zero!')
