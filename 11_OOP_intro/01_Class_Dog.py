"""
1▹ Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.

atrybuty: imię, kolor sierści, rasę

metody: szczekaj, machaj ogonem

Utwórz kilka obiektów klasy Pies z różnymi parametram
"""

class dog(): #class
    def __init__(self, firstname, coat_color, race):
        self.firstname = firstname
        self.coat_color = coat_color
        self.race = race

    def bark (self, number=1):
        return 'Hau ' * number

    def wave_tail(self):
        return 'Machu machu'

azor = dog('Azor','brunatna','Labrador')
reksio = dog('Reksio','biała','jamnik')
killer = dog('Killer','ciemna','Rottweiler')
kleks = dog('Kleks','żółta','Chihuahua')

print(azor.__dict__)
print(reksio.bark(22))
print(killer.wave_tail())