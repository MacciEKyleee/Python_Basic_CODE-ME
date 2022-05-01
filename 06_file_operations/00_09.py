"""
9* ▹ Korzystając z Google dowiedz się więcej o kodowaniu ASCII.
Utwórz plik, który tworzy prostą zaszyfrowaną wiadomość.
Każdą literę tekstu zapisuje za pomocą dziesiętnych wartości kodów ASCII.
Przykładowo literze A odpowiada numer 65.
Zapoznaj się z metodami ord() oraz char().
Pamiętaj o dodaniu znaku podziału. Utwórz drugi skrypt, który rozszyfruje wiadomość.
"""
def main():
    text = input("Podaj wiadomość do zaszyfrowania: ")
    encryption(text)
    decryption2(decryption1())

def encryption(text):
    for x in text:
        x = ord(x)
        print(x, end=" ")

def decryption1():
    new_list = []

    y = int(input("\nPodaj liczbę sekwencji kodu:"))
    counter = 0
    while y > counter:
        x = int(input("Podaj kod do odszyfrowania: "))
        new_list.append(x)
        counter += 1
    return new_list

def decryption2(new_list):
    for x in new_list:
        x = chr(x)
        print(x,end=" ")


if __name__ == '__main__':
    main()