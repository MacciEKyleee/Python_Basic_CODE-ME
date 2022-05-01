"""
8▹ Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
    - Program zacznie ze stworzonym słownikiem o trzech kluczach:
        -- marka (str)
        -- model (str)
        -- rocznik (int)
    - Wypisze ten słownik na ekran (bez żadnego formatowania)
    - Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
	        “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
    - Jeśli nie spełnia powyższego warunku, wypisze komunikat:
	        “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
    - Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy program również zmienia swoje zachowanie.

"""
def main():
    brand = str(input("Podaj markę auta: "))
    model = str(input("Podaj model auta: "))
    year = int(input("Podaj rocznik auta: "))

    dict_creator(brand, model, year)
    year_check(model, year)

def dict_creator(brand,model,year):
    car_dict = {}
    car_dict["marka"] = brand
    car_dict["model"] = model
    car_dict["rocznik"] = year
    print(car_dict)

def year_check(model,year):
    current_year = 2022
    if current_year - year >= 25:
        print(f"Gratulacje twój samochód {model} może zostać zarejestorwany jako zabytek")
    else:
        print(f"Twój samochód {model} jest zbyt młody żeby zostać zabytkiem")

if __name__=='__main__':
    main()

