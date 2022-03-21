"""
7▹ Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.

Co wiemy o tych numerach tych kart?

All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.

MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.

American Express card numbers start with 34 or 37 and have 15 digits.
"""
# cards_lengths = [13,15,16]
# card_number = input('Podaj numer karty: ')
#
# if not card_number.isdigit():
#     print('To nie jest numer karty')
#
# elif len(card_number) not in cards_lengths:
#     print('Długość nr karty nieprawidłowa.')
# else:
#     print('To może być karta')

# Czy karta jest visą

# def visa(card_number):
#     if card_number[0] == 4:
#         if ((len(card_number) == 13) or (len(card_number) == 16)):
#             print('To jest karta visa !')
#         else:
#             print('To nie jest karta visa.')
#     else:
#         print('To nie jest karta visa')
# visa(4123123412341234)

# # Czy karta jest kartą Visa?
#
# def visa(card_number):
#     card_length = len(card_number)
#     if (card_length in [13,16] and card_number[0] == '4'):
#         print('To jest karta visa !')
#     else:
#         print('To nie jest karta visa.')
#
# visa('4123123412341234')
#
# # Czy karta jest kartą Mastercard?
#
# def is_mastercard(card_number):
#     card_length = len(card_number)
#     condition_1 = 51 <= int(card_number[0:2]) <= 55
#     condition_2 = 2221 <= int(card_number[0:4]) <= 2720
#
#     if card_length == 16 and (condition_1 or condition_2):
#         print('To jest karta MasterCard !')
#     else:
#         print('To nie jest karta MasterCard.')
#
# is_mastercard('5545029702979683')
#
# # Czy karta jest kartą Amex?
#
# def is_americanexpress(card_number):
#     card_length = len(card_number)
#     condition_1 = 34 <= int(card_number[0:2]) <= 37
#
#     if card_length == 15 and (condition_1):
#         print('To jest karta Amex !')
#     else:
#         print('To nie jest karta Amex.')
#
# is_americanexpress('346712404104096')

def is_visa(card_number):
    card_length = len(card_number)
    return (card_length in [13,16] and card_number[0] == '4')

def is_mastercard(card_number):
    card_length = len(card_number)
    condition_1 = 51 <= int(card_number[0:2]) <= 55
    condition_2 = 2221 <= int(card_number[0:4]) <= 2720
    return card_length == 16 and (condition_1 or condition_2)

def is_americanexpress(card_number):
    card_length = len(card_number)
    condition_1 = 34 <= int(card_number[0:2]) <= 37
    return card_length == 15 and (condition_1)


def get_card_number():
    cards_lengths = [13, 15, 16]
    while(True):
        card_number = input('Podaj numer karty.')
        card_number = card_number.replace(' ','')

        if card_number.isdigit() and len(card_number) in cards_lengths:
            break

        else:
            print('To nie jest numer karty. Spróbuj innego numeru.')
    return card_number

card_number = get_card_number()
print('Numer karty użytkownia -->',card_number)

# console.log(card_number)
#
# if is_visa(card_number):
#     print('To jest Visa')
# elif is_mastercard(card_number):
#     print('To jest Mastercard')
# elif is_americanexpress(card_number):
#     print('To jest Amex')
# else:
#     print('To jest inna karta!')
