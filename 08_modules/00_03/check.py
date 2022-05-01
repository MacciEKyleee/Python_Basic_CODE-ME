import os

def opening(filename):
    if os.path.exists(filename):
        # print('Taki plik już istnieje!')
        if (os.path.getsize(filename) == 0):
            return (f'Plik o nazwie {filename} istnieje i jest pusty.')
        else:
            return (f'Plik o nazwie {filename} istnieje i posiada jakąś zawartość.\n\n')
    else:
        return('')

def save_safety(filename):
    question = input(print('Do you want to save your file - insert YES or NO.'))
    guestion = question.lower()
    if question == 'yes':
        try:
            with open(filename,'x+') as f:
                f.write()
        except FileExistsError:
            return('\n   \b Unable to save file with this name - a file with that name already exists')
    else:
        return('')


if __name__ == 'check':
    print('\n  Security module has been imported.\n')
    print('\n If you want to check is file exist - use function "check".')
    print('\n If you want to save the file - use function "save_safety".')

    print('\n\n_________________________________________________________')
    file_checking = input(print('Enter the full path of the file to be checked - e.g. test.txt. \n'))
    print(opening(file_checking))
    print(save_safety(file_checking))


