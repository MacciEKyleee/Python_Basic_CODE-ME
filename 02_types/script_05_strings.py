"""
Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej 
i od prawej do lewej np.: Kobyła ma mały bok. 
Pozwól użytkownikowi wprowadzić dowolne zdanie. 
Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.
"""
print("Proszę o wprowadzenie dowolnego zdania.")
print("Sprawdzę, czy zdanie to jest palindromem.")
print("")

word=str(input())
word_1=word.lower()
Word=word_1.replace(" ","")
print(Word)

score=len(Word)
print("Długość ciągu:", score)
print("")


if int(score)%2==0:
    
    middle=(score//2)
    print("Środkowa wartość:",middle)
    print("Środkowa litera",Word[middle-1])
    print("")
    
    Middle=Word[0:(middle)]
    Ending=Word[(middle):]
    print("Pierwsza część ciągu:",Middle)
    print("Druga część ciągu:",Ending)
    Rending=Ending[::-1]
    print("Odwrócona druga część ciągu:",Rending)
    print("")
    print("Czy słowo jest palindromem?")
    print(bool((str(Middle)==str(Rending))))    
else:
    
    middle=(score//2)
    print("Środkowa wartość:",middle+1)
    print("Środkowa litera",Word[middle])
    print("")
    
    Middle=Word[0:(middle)]
    Ending=Word[(middle+1):]
    print("Pierwsza część ciągu:",Middle)
    print("Druga część ciągu:",Ending)
    Rending=Ending[::-1]
    print("Odwrócona druga część ciągu:",Rending)
    print("")
    print("Czy słowo jest palindromem?")
    print(bool((str(Middle)==str(Rending))))
