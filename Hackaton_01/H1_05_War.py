"""
•	Zasady: https://pl.wikipedia.org/wiki/Wojna_(gra_karciana)
•	Konieczność użycia modułu random.
•	Program rozdaje karty i drukuje informacje o przebiegu rozgrywki
•	Pomysły na uproszczenie gry:
o	zamiast implementować talię kart, używamy liczb (0, 1, 2 ... 9, 10, 11) dla (2, 3, 4, ... Q, K, A)
o	aby gra kończyła się wcześniej, rozdajemy tylko 10 kart
o	dwa tryby: zdobyte karty dochodzą do "ręki", lub są odkładane i nie wykorzystywane

"""
import random
print('')
print('Zagramy w klasyczną grę karcianą o nazwie: "Wojna"')
print('')


#value = {'2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'10', 'walet':'11', 'dama':'12', 'król':'13', 'as':'14'}
#value = {'2Clubs':2, '2Diamonds':2, '2Hearts':2, '2Spades':2,'3Clubs':3, '3Diamonds':'3', '3Hearts':'3', '3Spades':'3', '4Clubs':'4', '4Diamonds':'4', '4Hearts':'4', '4Spades':'4', '5Clubs':'5', '5Diamonds':'5', '5Hearts':'5', '5Spades':'5','6Clubs':'6', '6Diamonds':'6', '6Hearts':'6', '6Spades':'6', '7Clubs':'7', '7Diamonds':'7', '7Hearts':'7', '7Spades':'7', '8Clubs':'8', '8Diamonds':'8', '8Hearts':'8', '8Spades':'8', '9Clubs':'9', '9Diamonds':'9', '9Hearts':'9', '9Spades':'9', '10Clubs':'10', '10Diamonds':'10', '10Hearts':'10', '10Spades':'10','JClubs':'11', 'JDiamonds':'11', 'JHearts':'11', 'JSpades':'11', 'QClubs':'12', 'QDiamonds':'12', 'QHearts':'12', 'QSpades':'12', 'KClubs':'13', 'KDiamonds':'13', 'KHearts':'13', 'KSpades':'13', 'AClubs':'14', 'ADiamonds':'14', 'AHearts':'14', 'ASpades':'14'}
value = {'2Clubs':2, '2Diamonds':2, '2Hearts':2, '2Spades':2,'3Clubs':3, '3Diamonds':3, '3Hearts':3, '3Spades':3, '4Clubs':4, '4Diamonds':4, '4Hearts':4, '4Spades':4, '5Clubs':5, '5Diamonds':5, '5Hearts':5, '5Spades':5,'6Clubs':6, '6Diamonds':6, '6Hearts':6, '6Spades':6, '7Clubs':7, '7Diamonds':7, '7Hearts':7, '7Spades':7, '8Clubs':8, '8Diamonds':8, '8Hearts':8, '8Spades':8, '9Clubs':9, '9Diamonds':9, '9Hearts':9, '9Spades':9, '10Clubs':10, '10Diamonds':10, '10Hearts':10, '10Spades':10,'JClubs':11, 'JDiamonds':11, 'JHearts':11, 'JSpades':11, 'QClubs':12,'QDiamonds':12, 'QHearts':12, 'QSpades':12, 'KClubs':13, 'KDiamonds':13, 'KHearts':13, 'KSpades':13, 'AClubs':14, 'ADiamonds':14, 'AHearts':14, 'ASpades':14}


talia = ['2Clubs', '2Diamonds', '2Hearts', '2Spades','3Clubs', '3Diamonds', '3Hearts', '3Spades', '4Clubs', '4Diamonds', '4Hearts', '4Spades', '5Clubs', '5Diamonds', '5Hearts', '5Spades','6Clubs', '6Diamonds', '6Hearts', '6Spades', '7Clubs', '7Diamonds', '7Hearts', '7Spades', '8Clubs', '8Diamonds', '8Hearts', '8Spades', '9Clubs', '9Diamonds', '9Hearts', '9Spades', '10Clubs', '10Diamonds', '10Hearts', '10Spades','JClubs', 'JDiamonds', 'JHearts', 'JSpades', 'QClubs', 'QDiamonds', 'QHearts', 'QSpades', 'KClubs', 'KDiamonds', 'KHearts', 'KSpades', 'AClubs', 'ADiamonds', 'AHearts', 'ASpades']

talia_1 = []
talia_2 = []
i=0
j=0
# We create two independent decks
while i <26:
    card = random.choice(talia)
    if card in talia_1:
        continue
    else:
        talia_1.append(card)
        i = i+1

print('Talia gracza 1: ', talia_1)

while j <26:
    card = random.choice(talia)
    if card in talia_2:
        continue
    else:
        if card in talia_1:
            continue
        else:
            talia_2.append(card)
            j = j+1

print('Talia gracza 2:', talia_2)

print("")
print("")

# We create two independent decks
print('ROZPOCZNIJMY GRĘ! ')
print("")

score_p1 = 0
score_p2 = 0

round=0

for round in range(10):
    print('Bitwa numer: ', round+1)
    print('')

    if value[talia_1[round]] > value[talia_2[round]]:
        score_p1 = score_p1+1
        print('Gracz 1 wylosował kartę: ', talia_1[round], ' a gracz 2 wylosował kartę: ', talia_2[round])
        print('Wygrał gracz 1 !')
        print('')
        print('Wynik aktualny:')
        print('Gracz 1: \n',score_p1)
        print('Gracz 2: \n',score_p2)
        round = round+1

    elif value[talia_1[round]] < value[talia_2[round]]:
        score_p2 = score_p2 + 1
        print('Gracz 1 wylosował kartę: ', talia_1[round], ' a gracz 2 wylosował kartę: ', talia_2[round])
        print('Wygrał gracz 2 !')
        print('')
        print('Wynik aktualny:')
        print('Gracz 1: \n',score_p1)
        print('Gracz 2: \n',score_p2)
        round = round + 1

    else:
        print('Gracz 1 wylosował kartę: ', talia_1[round], ' a gracz 2 wylosował kartę: ', talia_2[round])
        print('Mamy remis w bitwie - potrzebna będzie dogrywka.')
        print('')

        print('Gracze muszą wyciągnąć kolejną kartę:')
        print('--- >')
        print('')
        if value[talia_1[round+1]] > value[talia_2[round+1]]:
            score_p1 = score_p1 + 2
            print('Gracz 1 wylosował kartę: ', talia_1[round+1], ' a gracz 2 wylosował kartę: ', talia_2[round+1])
            print('Wygrał gracz 1 !')
            print('')
            print('Wynik aktualny:')
            print('Gracz 1: \n', score_p1)
            print('Gracz 2: \n', score_p2)
            round = round + 2

        elif value[talia_1[round+1]] < value[talia_2[round+1]]:
            score_p2 = score_p2 + 2
            print('Gracz 1 wylosował kartę: ', talia_1[round+1], ' a gracz 2 wylosował kartę: ', talia_2[round+1])
            print('Wygrał gracz 2 !')
            print('')
            print('Wynik aktualny:')
            print('Gracz 1: \n', score_p1)
            print('Gracz 2: \n', score_p2)
            round = round + 2



    print('___________________________')
    print('')


if score_p1 < score_p2:
    print('Wygrał gracz 2 !\n', 'Gratulacje !')
elif score_p1 > score_p2:
    print('Wygrał gracz 1 !\n', 'Gratulacje !')
else:
    print('W tej wojnie mamy .... REMIS !')
#print(value[talia_1[0]])

