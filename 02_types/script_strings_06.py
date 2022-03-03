#!/usr/bin/env python
# coding: utf-8

# In[20]:


"""
Przekopiuj zawartość import this do zmiennej.
    import this
Policz liczbę wystąpień słowa better.
Usuń z tekstu symbol gwiazdki
Zamień jedno wystąpienie explain na understand
Usuń spacje i połącz wszystkie słowa myślnikiem
Podziel tekst na osobne zdania za pomocą kropki
"""

text = "The Zen of Python, by Tim Peters\n\nBeautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let's do more of those!"
print(text)
print("")
print("Liczba wystąpień słowa 'better':",text.count('better'))
print("")
text1=text.replace('*','')
print('Poniżej Zen Of Python bez gwiazdek (*)')
print("")
#print(text1)
print("")
text2=text1.replace('explain','understand',1)
#print(text2)
print("")
text3=text2.replace(' ','-')
#print(text3)
text4=text3.split('\n')
print(text4)


# In[ ]:




