print("")
print("Podaj słowo większe niż 7 liter i nieparzyste:")
print("")

word=str(input())
long=int(len(word))
if long>7 :
    if (long%2==1):
        n=int((long)//2)
        print(word[(n-1):(n+2)])
    else:
        print("To słowo nie ma nieparzystej liczby znaków")
else:
    print("To słowo nie ma więcej niż 7 liter")