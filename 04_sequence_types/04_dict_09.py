"""
9▹ 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
 Wyświetl najpopularniejszy przedmiot.
  (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)
"""
print('\n Dzień dobry \n Proszę kolejnych 5 graczy o podanie 4 przedmiotów szkolnych \n')
print('')

student_list = []
for k in range(5):
    print(f'Dla ucznia {k+1} przedmioty są takie:')
    list = []
    i = 0
    while i<=3:
        subject =input(f'Podaj nazwę przedmiotu szkolnego nr {(i+1)}:\n')
        subject = subject.lower()
        if subject in list:
            print('Ten przedmiot jest już na liście.')
        else:
            list.append(subject)
            i = i +1

    student_list.extend(list)

print('')
counting_dict={}
for word in student_list:
    if word in counting_dict:
        counting_dict[word] = counting_dict[word] + 1
    else:
        counting_dict[word] = 1

print(counting_dict)
#for k,v in counting_dict.items():
#    print(k,'---->',v)
# def student(y):
#     student_list = []
#     for i in range(y):
#         student_list.append(lista)
#
# lista_roku = student(5)
#print(student_list)
