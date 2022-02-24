"""
Stwórz dwie zmienne s1 i s2
przechowujące dowolne wyrazy,
utwórz nowy łańcuch s3,
dołączając s2 w środku s1.
"""
print("")

print("Podaj pierwsze słowo")
word1=str(input())
print("")

print("Podaj drugie słowo")
word2=str(input())
print("")

n=len(word1)
m=(n//2)
word3=word1[:m]+word2+word1[(m-1):]
print("Wyjdzie z ich połączenia taki ciąg:")
print(word3)
print("")

