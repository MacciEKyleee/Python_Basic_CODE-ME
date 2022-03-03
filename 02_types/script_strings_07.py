#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
Stwórz dwie dowolne zmienne przechowujące wartość liczbową i tekstową.
Użyj funkcji format(), by wyświetlić zdanie zawierające te wartości.
"""

print("")
print("Która reprezentacja w piłce siatkowej mężczyzn, wygrała złoyt medal ostatnich Igrzysk Olimpijskich (Tokio)?")
winner=str(input())
print("")
print("Reprezentacja ta wygrała w finałowym meczu z jaką reprezentacją?")
loser=str(input())
print("")
print("Przegrany zespół zdobył ile setów (0, 1 czy 2)?")
score=int(input())
print("")
print("")
print('W finałowym meczu Igrzysk Olimpijskich w Tokio w roku 2021, reprezentacja {} wygrała z zespołem {} wynikem 3:{}.'.format(winner,loser,score))


# In[ ]:




