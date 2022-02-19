import re
from collections import Counter


def remove():
    with open('two_cities_ascii.txt', 'r+') as file:
        file = file.read()
     
    new_string = re.sub('[^a-zA-Z]+', ' ', file)

    return new_string


def sum_Word(word):
    return sum((ord(char) - 64) for char in word)


def word_Length(array):
    var = f'Γράμματα/Χαρακτήρες (:) Φορές που Εμφανίζονται.\n {Counter(map(len, array))}'
    print(var)
     
def main():
    var2_txt = remove().split(" ")
    new_txt = list(filter(None, var2_txt))

    list_Word_sum20 = []
    for word in new_txt:
        if sum_Word(word) != 20:
           list_Word_sum20.append(word)

    word_Length(list_Word_sum20)


if __name__ == "__main__":
    main()