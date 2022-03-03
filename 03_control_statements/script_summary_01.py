"""
1▹ Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
(np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
Następnie powitaj każdą osobę na liście.
"""
print("")
print("Wprowadź proszę imiona, które Cię interesują:")
print("")
ciag=str(input())
ciag_1=ciag.replace(',',' ')
ciag_2=ciag_1.split(sep=None)
#print(ciag_2)
for i in ciag_2:
    i=i.capitalize()
    print('Witaj ',i,'!')
    print("")