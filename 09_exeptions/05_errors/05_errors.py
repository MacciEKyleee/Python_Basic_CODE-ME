"""
5▹ W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float.
Co jeśli użytkownik poda wartość 60 kg ?
Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.
"""

import bmi

def show_advice(state):
    filename = state + '.txt'
    with open(filename) as fopen:
        content = fopen.read()

    print('---- Twoja porada brzmi:')
    print(content)

def get_user_data():
    while True:
        try:
            weight = float(input('Podaj swoją wagę w [kg]\n'))
            height = float(input(('Podaj swój wzrost w [m]\n')))

            if weight > 597 or height > 2.8:
                raise ValueError('Nieprawdopodobne wartości.')
            break
#        except Exception as e:
        except:
            print('Wartość nieprawidłowa, spróbuj jeszcze raz.')
    return weight, height


def main():
    w, h = get_user_data()
    result = bmi.get_bmi_value(w, h)
    show_advice(result)
    #print('BMI:', state)

if __name__ == '__main__':
    main()