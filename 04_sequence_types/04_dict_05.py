"""
5▹ W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

"Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"

Zadbaj o sposób wyświetlania np.: szybko : 5
zbudź : 1
"""
txt = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

print(txt)
print('')
txt = txt.lower()
txt = txt.replace(',','')
words = txt.split()
print(words)

counting_dict={}
for word in words:
    if word in counting_dict:
        counting_dict[word] = counting_dict[word] + 1
    else:
        counting_dict[word] = 1

print(counting_dict)
for k,v in counting_dict.items():
    print(k,'---->',v)

#fast=txt.count('szybko')
#print('szybko: ',fast)

#wake=txt.count('zbudź się')
#print('zbudź się: ',wake)

#wstawaj=txt.count('wstawaj')
#print('wstawaj: ',wstawaj)

#stygnie=txt.count('stygnie')
#print('stygnie: ',stygnie)

#coffee=txt.count('kawa')
#print('kawa: ',coffee)