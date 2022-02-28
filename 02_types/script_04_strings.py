# 4. Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
# Połącz dane w jeden ciąg book za pomocą spacji
# Policz liczbę wszystkich znaków w napisie book

print("Proszę, podaj tytuł książki którą ostatnio czytałaś/eś:")
title=str(input())
print("")

print("Pamiętasz może nazwisko autora? Jeżeli tak to proszę Cię o podanie.")
author=str(input())
print("")

print("Najtrudniejsze przed nami. Proszę podaj szacunkową liczbę stron tej książki.")
pages=str(input())
print("")

Title=title.capitalize()
Author=author.capitalize()
book=Title+" "+Author
print("Czy tytuł książki ma same cyfry w nazwie? ", title.isalnum())
print("")

print("Czy nazwisko autora ma same cyfry w nazwie? ", author.isalnum())
print("")

print("Czy liczba stron jest wartością liczbową:", pages.isdigit())
print("")

print("Prawidłowy tytuł i autor brzmią: ", book)
print("")

print("Liczba znaków w tytule (wliczając przerwę):",len(book))
