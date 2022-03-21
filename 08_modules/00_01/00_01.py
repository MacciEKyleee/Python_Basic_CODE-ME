'''
1▹ Stwórz moduł, który będzie przechowywał funkcję obliczającą bmi.py.
Zaimportuj module do pliku fitmeter.py.
Nowy plik będzie informował użytkownika o jego aktualnym BMI i na podstawie wyniku (niedowaga, nadwaga, otyłość)
sugerował zmiany w stylu życia pobierane z odpowiedniego pliku.

1) Utwórz plik bmi.py zawierający metodę obliczania bmi. Metoda zwraca wartości: niedowaga, waga normalna, nadwaga, otyłość.

2) Utwórz 4 pliki .txt zawierające porady.

3) Utwórz plik fitmeter.py, który zaimportuje moduł bmi.

4) fitmeter.py pobierze wagę i wzrost pacjenta i przekaże do odpowiedniej funkcji z modułu bmi.

5) Na podstawie zwróconej wartości fitmeter.py wyświetli odpowiednie porady dla pacjenta.

'''

def calculate_bmi(weight,height):
    return
def get_state(bmi):
    if bmi < 18:
        return "niedowaga"
    elif bmi <25:
        return "norma"
    elif bmi <30:
        return 'nadwaga'
    else:
        return 'otylosc'

def get_bmi_value(w,h):
    bmi_result = calculate_bmi()
    bmi_status = get_state(bmi_result)
    return bmi_status

if __name__ == "__main__":
    # reszta skrypotw
    result = get_bmi_value(w,h)
    print('Twoje BMI ->',result)