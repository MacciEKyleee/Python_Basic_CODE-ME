"""
3▹ W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.
"""
print("")
print("Napisz proszę 3 zdania o sobie.")
ciag=str(input())
print("")

upper='AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ'
lower='aąbcćdeęfghijklłmnńoóprstśtuwyzźż'
digit='0123456789'
special= '!?@#$%^&*(){}:;[]<>-_=+/*\~`,.'
u=0
l=0
d=0
s=0

for i in ciag:
    if i in lower:
        l=l+1
print("W podanym tekście jest:",l,"małych liter.")
print("")

for i in ciag:
    if i in upper:
        u=u+1
print("W podanym tekście jest:",u,"wielkich liter.")
print("")

for i in ciag:
    if i in digit:
        d=d+1
print("W podanym tekście jest:",d,"cyfr.")
print("")

for i in ciag:
    if i in special:
        s=s+1
print("W podanym tekście jest:",s,"znaków specjalnych.")
print("")