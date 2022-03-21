"""
1▹ Skorzystaj ze swojego kodu bmi.py.
Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika
oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość)
w zależności od otrzymanego parametru.

"""
def calculate_bmi(weight,height):
    return round(weight / height ** 2,2)

def get_state(bmi):
    if bmi < 18:
        return "niedowaga"
    elif bmi < 25:
        return "normalna"
    elif bmi < 30:
        return "otyłość"
    else:
        return "nadwaga"

def check_health(w,h):
    bmi_result = calculate_bmi(w, h)
    bmi_status = get_state(bmi_result)
        return bmi_status

#---- reszta skryptu
#pyta użytkownika

result = check_health(56,1.6)
print('Twoje BMI ->',result)