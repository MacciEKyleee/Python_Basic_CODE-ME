"""
7▹ Wróć do pierwszego zadania z lekcji o plikach, zmodyfikuj go tak, aby to użytkownik podawał nazwę pliku z cytatami.
Pamiętaj, by użytkownik po wykonaniu błędnej akcji (np. literówki w nazwie pliku) miał możliwość poprawić swój błąd.
"""
import random

def openfile():
    while True:
        try:
            filename = input('Your file name: \n')
            with open(filename) as fopen:
                text = fopen.readlines()
            break
        except FileNotFoundError:
            print("File couldn't be found here.")

    return text

def show(quote,width):
    print('Quote of the day: \n')
    print(width * '*')
    print(quote.center(width))
    print(width * '*')

def main():
    # obsłuż błędy
    quotes = openfile()
    quote = random.choice(quotes).strip()
    width = len(quote) * 2
    show(quote,width)

    # quote = random.choice(quotes).strip()
    # width = len(quote[0]) * 2
    #
    # print('Quote of the day: \n')
    # print(width * '*')
    # print(quote.center(width))
    # print(width * '*')

if __name__ == '__main__':
    main()