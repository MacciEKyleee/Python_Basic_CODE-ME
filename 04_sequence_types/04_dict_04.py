"""
4▹ Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.


"""
print('Tabliczka mnożenia.\n')
# tab = [['-'] * 10] * 10
# print(tab)
# print('')
#
# for row in tab:
#     for element in row:
#         print(row[], end=' ')
#     print()
for a in range (1,11):
    for b in range (1,11):
        print(a*b,end='\t')
    print()