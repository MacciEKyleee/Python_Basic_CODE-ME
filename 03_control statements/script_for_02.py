"""
Utwórz listę, która zawiera składniki na ulubione danie.
Wyświetl komunikaty co należy pokolei dodać.
Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.
"""
list=['pomidory','makaron','parmezan','czosnek','cebula','mieso_mielone']
for i in range(1,7):
    print(i,list[i-1])