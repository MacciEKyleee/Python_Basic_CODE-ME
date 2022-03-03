"""
Jak sprawdzić czy ciąg ma
co najmniej jedną dużą literę?
"""

print("Podaj słowo - sprawdzę czy jest conajmniej 1 duża litera")
word=str(input())
print((word.islower()!=True) and(word.isupper()!=True))
