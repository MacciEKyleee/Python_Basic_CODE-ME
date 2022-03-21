"""
8* ▹ Utwórz generator dowolnego typu np. generator zdań, tweetów czy konferencji.
Dane wejściowe pobierz z pliku csv (plik csv możesz traktować jako plik txt ze znanym znakiem podziału),
który będzie przechowywał dane potrzebne do generowania.

Przykład z generatora konferencji: http://generatorkonferencji.pl (niektóre potrafią wyjść zabawne). Wygenerujcie kilka. Czy widzicie wzorzec?

Przykład generatora cytatów: http://wisdomofchopra.com/ (Można wykorzystać istniejące dane wejściowe json, lub przepisać na własny format danych).
"""
import random

citatas = 'Citats.txt'
people = 'people.txt'


def get_quotes():
    with open(filename) as fopen:
        quotes = fopen.readlines()
    return quotes

def get_says():
    with open(people) as fopen:
        says = fopen.readlines()
    return says

# funkcja wyświetlająca
def show(content):
    quote = random.choice(content).strip()
    quote = quote.split(' - ')
    width = len(quote[0]) * 2

    print('Quote of the day: \n')
    print(width * '*')
    print('Kiedyś ',says.lleft(width),'powiedział',says[])
    print(quote[1].rjust(width))
    print(width * '*')


# main code

quotes_list = get_quotes()
show(quotes_list)