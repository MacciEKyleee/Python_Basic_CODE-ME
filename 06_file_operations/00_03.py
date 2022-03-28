"""
3▹ Wyświetl tylko 5 pierwszych linii

"""

filename = 'Citats.txt'

def get_quotes():
    with open(filename) as fopen:
        quotes = fopen.readlines()
    return quotes


# funkcja wyświetlająca
def show(content):
    quote=get_quotes()[0:5]
    for line in quote:
        print(line)

# main code

quotes_list = get_quotes()
show(quotes_list)