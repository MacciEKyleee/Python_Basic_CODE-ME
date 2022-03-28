"""
9▹ Sprawdź jak wygląda kod modułu antigravity.
Korzystając z tego samego sposobu otwarcia dowolnego url pozwól użytkownikowi podać adres www.

Pamiętaj sprawdzić czy url jest prawidłowy może zaczynać się:

https://

http://

www

bez www

Może się kończyć za pomocą:

.pl

.com

Jeśli podany adres nie jest linkiem, podnieś wyjątek URLError, który będzie informował, że url jest nieprawidłowy.

Nie masz dość? Swietnie! Przepisz to zadanie za pomocą wyrażeń regularnych (RegEx)
"""

import webbrowser
from urllib.error import URLError


def ensure_correct_beginning(url):
    return url.startswith('https://') or url.startswith('http://')

def ensure_correct_enging(url):
    return url.endswith('.pl') or url.endswith('.com')

def check_www_beginning(url):
    return url.startswith('www.')

def get_url():
    url = input("Podaj dowolny url -->")
    if ensure_correct_beginning(url) and ensure_correct_enging(url):
        return url
    elif check_www_beginning(url):
        return 'http://' + url
    else:
        raise URLError('URL w nieprawidłowym formacie.')
        #print('Błąd')

def main():
    while True:
        try:
            url = get_url()
            break
        except URLError as message:
            print(message)

    webbrowser.open(f"{url}")


if __name__ == '__main__':
    main()



