import re
from collections import Counter


def remove():
    with open('./two_cities_ascii.txt', 'r+') as file:
        file = file.read()

        new_string = re.sub('[^a-zA-Z]+', ' ', file)

    return new_string.lower()


def main():
    
    filtered_txt = remove().split()
    count = Counter(filtered_txt)
    print("10 most common words: ", count.most_common(10))

    count = count.most_common(20)
    For_2Letters = []
    For_3Letters = []
    for word in count:
        word = word[0]
        if len(word) > 1:
            for word_2 in count:
                word_2 = word_2[0]
                if len(word_2) > 1:
                    if word[:2] == word_2[:2] and word is not word_2 and word not in  For_2Letters and word_2 not in  For_2Letters:
                         For_2Letters.append([word, word_2])
                    if word[:3] == word_2[:3] and word is not word_2 and word not in  For_3Letters and word_2 not in For_3Letters:
                         For_3Letters.append([word, word_2])

    print("2 letters combinations: ", For_2Letters)
    print("3 letters combinations: ", For_3Letters )


if __name__ == "__main__":
    main()