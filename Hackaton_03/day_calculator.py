from datetime import datetime
import timedelta

def main():
    choosen_date = input(print('Podaj wybraną przez siebie datę (max. 7 dni do przodu) w formacie DD-MM-YYYY.\n'))
    time = number_of_days(choosen_date)
    print(time)
    return time

def number_of_days(choosen_date):
    date_format = "%d-%m-%Y"
    now = datetime.now()
    today = now.strftime("%d-%m-%Y")
    print(today)
    a = datetime.strptime(today,date_format)


    b = datetime.strptime(choosen_date,date_format)
    time = b-a
    time = int(time.days)
    return(time)

if __name__=='__main__':
    main()