"""
Do zmiennej quote przypisz zdanie:
„Honesty is the first chapter in the book of wisdom.”, a następnie:
"""
print("")
quote="Honesty is the first chapter in the book of wisdom."
print(quote)
print("")

print("Długość ciągu:")
print(len(quote))
b=len(quote)
print("")

print("Nie modyfikując zmiennej wyświetl słowo wisdom")
print(quote[-7:-1])
print("")


print("Wyświetl tylko pierwszą połowę tekstu")
centre=((len(quote)//2)+1)
print(quote[:centre])
print("")


print("Wyświetl tylko kropkę")
print(quote[-1])
print("")


print("Wyświetl od połowy tylko co trzecią literę cytatu")
print(quote[centre::3])
print("")

print("Wyświetl ‘Hnsyi h is hpe ntebo fwso.’")
print(quote[::2])
print("")


print("Wyświetl cały cytat odwrotnie:")
print(quote[::-1])
print("")


print("Zamień wisdom na słowo friendship")
print(quote.replace('wisdom','friendship'))
print("")
