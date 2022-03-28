# print ('Nie prawidłowa wartość')
# while True:
#     try:
#         age = int(input('Podaj wiek: '))
#         print("Za 10 lat będziesz mieć: ",age +10)
#         break
#     except ValueError: #error
#         print('Nie prawidłowa wartość')
#
# print('Poza pętlą.')

try:
    liczba = int(input('Podaj liczbę od 1 do 100.\n'))
    dzielnik = int(input('Podaj liczbę od 1 do 100.\n'))
    print(liczba/dzielnik)
# except (ValueError, ZeroDivisionError) as err:
#     print('Value is incorrect.',err)
    #print('Wartość nie jest liczbą.')
# except Exception as e:
#     print('Inny błąd.')
    raise ArithmeticError
except Exception as e:
    print('Ups...Mamy błąd.',e.__class__)
finally:
    print('\nTO ZAWSZE SIĘ WYDARZY !')

