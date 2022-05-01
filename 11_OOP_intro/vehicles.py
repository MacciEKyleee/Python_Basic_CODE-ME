class Vehicles():
    pass
    # cecha : mają koła
    # metoda: poruszaj_się()

class Bikes(Vehicles):
    pass
    # cecha1: mają 2 koła
    # cecha2 kierownica pozioma
    # cofnij_sie -> pedaluj do tylu



class Car(Vehicles):
    pass
    # cecha: 4 koła
    # cecha: silnik
    # uruchom_silnik()
    # cofnij_sie -> wlacz wspomaganie / podgląd / kamerkę



def wyrusz_w_droge(pojazd):
    # pojazd == obiekt typu Car
    pojazd.uruchom_silnik()