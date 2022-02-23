# Obliczanie BMI

print("Witam ! Policzmy Twoje BMI :)")

sex = input(str(print("Podaj swoją płęć [W/M]")))

if sex == "W":

    print("Niech poda Pani swoją masę w kg -->")
    masa = int(input())

    print("Proszę, podaj swój wzrost w centymetrach -->")
    wzrost = (int(input()))/100

    BMI=masa/(wzrost*wzrost)
    BMI=int(BMI)
    print("Twoje BMI wynosi:", BMI)

    if BMI<16:
      print("Jesteś wygłodzona")
    elif BMI>40:
       print("Jesteś otyła")
    else:
        (print("Jesteś w granicach odpowiedniego BMI"))
else:
    print("Niech Pan poda swoją masę w kg -->")
    masa = int(input())

    print("Proszę, podaj swój wzrost w centymetrach -->")
    wzrost = (int(input()))/100

    BMI=masa/(wzrost*wzrost)
    BMI=int(BMI)
    print("Twoje BMI wynosi:", BMI)

    if BMI<16:
      print("Jesteś wygłodzony")
    elif BMI>40:
       print("Jesteś otyły")
    else:
        (print("Jesteś w granicach odpowiedniego BMI"))