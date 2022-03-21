import random

with open('generator.csv') as f:
    content = f.readlines()
#print(content)

first = []
second = []
third = []

# for --> uzupełnienie kolumny

for line in content:
    splitted_line = line.split(';')
    first.append(splitted_line[0])
    second.append(splitted_line[1])
    third.append(splitted_line[2])

#print(first)
#print((second))
#print(third)

beginning = random.choice(first)
mid = random.choice(second)
ending = random.choice(third)

print('Generator tytułu konferencji naukowej')
print('________________________')
print(f'{beginning} {mid} to {ending}')
# random początek, koniec i środek zadania