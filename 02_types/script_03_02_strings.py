"""
Jak wyświetlić wyśrodkowany tekst
o zadanej szerokośći i  dodatkowo
puste miejsca wypełnić np. gwiazdką"

"""
print("Podaj słowo")
word=str(input())

print("Podaj długość chcianego ciągu")
size=int(input())

print(word.center(size,'*'))