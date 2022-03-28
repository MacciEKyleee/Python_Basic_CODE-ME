import bmi

def show_advice(state):
    filename = state + '.txt'
    with open(filename) as fopen:
        content = fopen.read()

    print('---- Twoja porada brzmi:')
    print(content)


def main():
    w = float(input('Podaj swoją wagę w [kg]\n'))
    h = float(input(('Podaj swój wzrost w [m]\n')))
    result = bmi.get_bmi_value(w, h)
    show_advice(result)
    #print('BMI:', state)

if __name__ == '__main__':
    main()