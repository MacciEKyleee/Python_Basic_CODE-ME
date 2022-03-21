import math
def get_three_values():
    b = input('Podaj wartość b.')
    a = input('Podaj wartość c.')
    c = input('Podaj wartość a.')
    return a,b,c



if __name__ == "__main__":
    delta_value = ((b*b)-(4*a*c))
    print(delta_value)