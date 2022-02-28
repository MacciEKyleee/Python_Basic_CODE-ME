"""
#1.Na kartce papieru oblicz jak twój wiek będzie reprezentowany binarnie. 
# Sprawdź czy to samo zwróci Python.
"""

dec=28
print(bin(dec))

"""
# Dla podanej liczby w systemie dwójkowym bin_num = 1001111
# oblicz wartość w systemie dziesiętnym. Zamianę z systemu binarnego na dziesiętny 
# napisz samodzielnie (nie korzystaj z metody wbudowanej).
"""

bin_num="1001111"
int(bin_num,2)

#Dla liczb hex_num = 1DB i oct_num = 2063 zwróć wartość w systemie dziesiętynym.

hex_num="1DB"
oct_num="2063"
print(int(hex_num,16))
print(int(oct_num,8))




