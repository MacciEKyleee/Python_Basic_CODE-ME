"""
Najsłynniejsze zadanie z podstaw programowania. Kalkulator BMI (Body Mass Index). Wzór jest bardzo prosty:
BMI = (masa (kg)) / (wzrost (m))²
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