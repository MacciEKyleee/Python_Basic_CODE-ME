"""
4▹ Zmodyfikuj swoją grę wisielec tak, aby w dowolny uzasadniony sposób wykorzystać moduł lub moduły.
"""
import random

def main():
    sport_list = ["koszykowka", "bilard", "siatkowka", "boks", "mma", "badminton", "kolarstwo", "szachy", "tenis"]
    random_word_from_list(sport_list)
    check()
    encryption()

def check():
    word = input("Podaj słowo: ")
    guess = input("\nPodaj literę: ")
    if guess in word:
        print(f"litera {guess} jest w tym słowie")
    else:
        print(f"Litery {guess} nie ma w słowie {word}")

def encryption():
    random_word = input("Podaj jekieś słowo: ")
    for i in random_word:
            print("_", end="")
            break

def random_word_from_list(list):
    x = random.choice(list)
    print(x)

if __name__ == '__main__':
    main()
