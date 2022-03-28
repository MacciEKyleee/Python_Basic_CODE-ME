"""
6▹ Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych.
Sprawdź dla każdej kart jej typ.
Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt.

- karty kredytowe mogą mieć dł -> 13, 15, 16
- nr karty składa się z samych cyfr

is_visa(card_number) -> T/F
- dł -> (13 lub 16)
- numer zaczyna się od 4

is_mastercard(card_number) -> T/F
- dł -> 16
- nr 51 do 55 LUB od 2221 do 2720

is_american_express(card_number) -> T/F
- dł -> 15
- 34 lub 37
"""
filename = 'Random_cards_number.txt'

def get_quotes():
    with open(filename) as fopen:
        quotes = fopen.readlines()
    return quotes

def is_american_express(card_number):
    card_length = len(card_number)
    return card_length == 15 and (card_number[0:2] == '34' or card_number[0:2] == '37')


def is_visa(card_number):
    card_length = len(card_number)
    return card_length in [13, 16] and card_number[0] == '4'


def is_mastercard(card_number):
    card_length = len(card_number)
    starts_with_51_55 = 51 <= int(card_number[0:2]) <= 55
    starts_with_2221_2720 = 2221 <= int(card_number[0:4]) <= 2720

    return card_length == 16 and (starts_with_51_55 or starts_with_2221_2720)

# def get_card_number():
#     cards_lengths = [13, 15, 16]
#     while(True):
#         #card_number = input('Podaj numer karty: ')
#         card_number = get_quotes()
#         card_number = card_number.replace(' ', '')
#
#         if card_number.isdigit() and len(card_number) in cards_lengths:
#             break
#         else:
#             print('To nie jest nr karty, spróbuj jeszcze raz ')
#
#     return card_number

def get_card_number():
    card_numbers = []
    i = 0
    while i >=0:
        card_number = get_quotes()[i]
        # card_number = get_card_number()
        #print('Numer karty użytkownika -->', card_number)
        card_numbers.append(card_number)

    return card_numbers

#--- main code

visa_list = []
mastercard_list = []
american_express_list = []

def main():
    card_numbers = get_card_number()
    for element in card_numbers:

        if is_visa(card_number):
            print("To jest visa")
            visa_list.append(card_number)

        elif is_mastercard(card_number):
            print("To jest master card")
            mastercard_list.append(card_number)

        elif is_american_express(card_number):
            print("To jest american express")
            american_express_list.append(card_number)

        else:
            print("To może być inna karta")

    return visa_list, mastercard_list, american_express_list


if __name__ == '__main__':
    main()