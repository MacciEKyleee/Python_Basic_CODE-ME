# import random
# #filename = 'Citats.txt'
# filename = input('Podaj nazwę pliku z którego chcesz pobrać cytaty: \n')
#
# with open(filename,'r') as fopen:
#   quotes = fopen.readlines()
#
# quote = random.choice(quotes).strip()
# quote = quote.split(' -')
#
# #print(quote)
# width = len(quote[0]) * 2
# przesuniecie = int(width * 0.5)
#
# print('Quote of the day is:\n')
# print(("*" * width))
# print(quote[0].center(width))
# #print(quote[1].center(width + przesuniecie))
# print(quote[1].rjust(width))
#
# print(("*"* width))
filename = 'Citats.txt'

import random
def get_quotes():
    with open(filename) as fopen:
        quotes = fopen.readlines()
    return quotes


# funkcja wyświetlająca
def show(content):
    quote = random.choice(content).strip()
    quote = quote.split(' - ')
    width = len(quote[0]) * 2

    print('Quote of the day: \n')
    print(width * '*')
    print(quote[0].center(width))
    print(quote[1].rjust(width))
    print(width * '*')


# main code

quotes_list = get_quotes()
show(quotes_list)