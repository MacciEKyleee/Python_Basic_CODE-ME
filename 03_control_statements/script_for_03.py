"""
Napisz program, który dla 10 kolejnych liczb naturalnych
wyświetli sumę poprzedników.
Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
"""
print("Sumy kolejnych 10 liczb naturalnych wynoszą:",)
k=0
for i in range(1,11,1):
    k=k+i
    print(k)

print("")
sum_number=0
for number in range(11):
    sum_number=sum_number+number
    print(sum_number)
