"""
6▹ Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów.

days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}
"""
days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}
print('\n Słownik: \n',days)

numbers = []
for element in days:
    k = days.setdefault(element)
    numbers.append(k)

numbers = set(numbers)
print('\n Lista zawierająca wartości słownika, bez duplikatów \n',numbers)
# numbers = {}
# numbers = days.values()
# print(numbers)
# # for value in days.items():
# #     print(value)
# #     numbers.append(value)
