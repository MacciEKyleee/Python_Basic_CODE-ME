books={}

#1. Napisz funkcję, która pyta użytkownika
def save_book():
    book_title = input('Podaj nazwę książki.')
    book_rate = input('Podaj ocenę tej książki w skali 1 do 10.')
    books[book_title]  =   book_rate

#2. Napisz funkcję, która zapyta o tytuł książki i wyświetli tytuł wraz z oceną.
def show_book(title):
    print(f'Książka {title} ma ocenę-->{ books[title] }')

# ----- główna część programu
for i in range(3):
    save_book()
    print('---------')

print(books)

# -----
while(True):
    given_title = input('Podaj tytuł do sprawdzenia oceny:')
    if given_title in books.keys():
        break

    print('Takie tytułu nie mamy na liście.')

# --- Metoda pokazująca ocenę książki
show_book(given_title)