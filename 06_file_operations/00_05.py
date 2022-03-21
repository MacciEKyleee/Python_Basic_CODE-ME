"""
5▹ Wykorzystaj plik zawierający fragment Pana Tadeusza. Znajdź najdłuższe słowo występujące w zadanym fragmencie.

"""
filename = 'Text.txt'

# with open('Text.txt', 'w', encoding = 'utf-8') as f:
#     f.write(filename)

def get_text():
    with open(filename, encoding = 'utf-8') as fopen:
        content = fopen.read()

    return content

def clean_text(text):
    extras = '.!,()'

    for symbol in extras:
        text = text.replace(symbol,'')
    return text

def find_longest_word(text):
    text = text.split()
    longest_word = ''

    for current_word in text:
        if len(current_word) > len(longest_word):
            longest_word = current_word

    return longest_word


# -- main code
text = get_text()
text = clean_text(text)
search_word = find_longest_word(text)

print(search_word, ', o długości - ', len(search_word))

# # funkcja wyświetlająca
# def show(content):
#     quote =
#     quote = quote.split(' - ')
#     width = len(quote[0]) * 2
#
#     print('Quote of the day: \n')
#     print(width * '*')
#     print(quote[0].center(width))
#     print(quote[1].rjust(width))
#     print(width * '*')