"""
Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
 która wyświetli w zależności od wyniku:
 niedowaga / waga normalna / nadwaga / otyłość.
"""
print("")
print("Witam w programie wyliczającym Twoje BMI. Prosimy o podanie kilku podstawowych danych.")
print("")
print("Podaj proszę swoją aktualną wagę wyrażoną w kilogramach.")
weight=int(input())
print("")
print("Podaj proszę swój wzrost mierzony w centymetrach.")
height=int(input())
print("")

BMI=(weight/((height/100)**2))

print("Twoje BMI wynosi: ",round(BMI,2))
print("")

if BMI >30.0:
    print("Według wskaźnika BMI należysz do grupy: otyły.")
elif BMI >25.0:
    print("Według wskaźnika BMI należysz do grupy: nadwaga.")
elif BMI > 18.5:
    print("Według wskaźnika BMI należysz do grupy: waga normalna.")
else:
    print("Według wskaźnika BMI należysz do grupy: niedowaga.")
