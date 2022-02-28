"""
1) Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.

C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit

Napisz rozwiązanie zarówno z użyciem pętli while jak i for.
"""

l=0
print("")
while l<=200:
    k = round(((5 / 9) * (l - 32)),2)
    print('Temperatura w Farenheitach wynosi',l,',czyli w Celsjuszach:',k)
    l=l+20

print("")

for i in range(0,220,20):
    h=round(((5 / 9) * (i - 32)),2)
    print('Temperatura w Farenheitach wynosi',i,',czyli w Celsjuszach:',h)
