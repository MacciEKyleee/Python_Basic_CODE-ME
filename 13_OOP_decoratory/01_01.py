"""
Utwórz dekorator @uppercase_decorator, który przyjmuje dowolną funkcję zawracającą łańcuch znaków i zwracający ten sam tekst zmieniony na wielkie litery.
Utwórz funkcję zwracającą tekst
Utwórz dekorator przyjujący tę funkcję
Wywołaj funkcję, by sprawdzić, że decorator działa
"""
def uppercase_decorator(func):
    def inside_func():
        txt = func()
        txt = txt.upper()
        return txt
    return inside_func

@uppercase_decorator
def daily_news():
    return 'important!'

@uppercase_decorator
def smart_text():
    return 'smart...'

print(daily_news())
print(smart_text())

