
dom = 1
szkola = 2
szpital = 3
teatr = 4
kino = 5
kosciol = 6
bar = 7

buildings = ['dom','szkola','szpital','teatr','kino','kosciol','bar']


routes = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 4],
    4: [1, 3, 5],
    5: [2, 4, 6, 7],
    6: [3, 5, 7],
    7: [5, 6]
}

for start, neighbourhood in routes.items():
    for neighbourhood in neighbourhood:
        print(buildings[start-1],'--->',buildings[neighbourhood-1])