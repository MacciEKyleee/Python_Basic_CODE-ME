filename = 'dictionary.txt'

import random

def get_answer():
    answer = input('Wybierz z jakiej kategorii chcesz odgadywać hasło: ANIMALS, FRUITS or VEGETABLES.')
    return answer

def get_quotes():
    with open(filename) as fopen:
        quotes = fopen.readlines()
    return quotes

def show(content):
    if get_answer() == 'VEGETABLES':
        content = content[0:51]
        quote = random.choice(content).strip()
        quote = quote.split('. ')
        print(quote[1])

    elif get_answer() == 'FRUITS':
        content = content[52:102]
        quote = random.choice(content).strip()
        quote = quote.split('. ')
        print(quote[1])

    elif get_answer() == 'ANIMALS':
        content = content[103:152]
        quote = random.choice(content).strip()
        quote = quote.split('. ')
        print(quote[1])

    else:
        print('Podałeś zły zakres')



# main code

quotes_list = get_quotes()
show(quotes_list)