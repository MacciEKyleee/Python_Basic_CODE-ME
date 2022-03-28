"""
4▹ Wyświetl 3 losowe cytaty

"""
filename = 'Citats.txt'

import random

def get_quotes():
    with open(filename) as fopen:
        quotes = fopen.readlines()

    return quotes


# funkcja wyświetlająca
def show(content):
    quote = random.choice(content).strip()
    quote = quote.split(' -')
    width = len(quote[0]) * 2

    # print('Quote of the day: \n')
    print(width * '*')
    print(quote[0].center(width))
    print(quote[1].rjust(width))
    print(width * '*')
    print('')

def main():

    for i in range(0,3):
        print(f'{i+1} citat sound:')
        quotes_list = get_quotes()
        show(quotes_list)

# main code
if __name__ == '__main__':
    main()
