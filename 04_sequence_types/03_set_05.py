"""
5▹ Porównaj zachowanie discard() vs remove() dla typu set.
"""
element_1={'Asia','ma','Jasia','a','on','ma','Asia'}
element_2={'Asia','ma','Jasia','a','on','ma','Asia'}

element_1.discard('Asia')
print(element_1)

element_2.remove('Asia')
print(element_2)
print('')
print('')

print('remove(elem)')
print('Remove element elem from the set. Raises KeyError if elem is not contained in the set.')
print('')
print('discard(elem)')
print('Remove element elem from the set if it is present.')