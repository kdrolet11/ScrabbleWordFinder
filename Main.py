from itertools import combinations


def input_letters():
    while True:
        letters_entered = input("Input up to 10 only alphabetical letters with no spaces in between them, "
                                "then hit enter:\n").upper()
        if letters_entered.isalpha() and len(letters_entered) <= 10:
            break
        else:
            print("Your input contained non-alphabetical letters or more than 10 letters. Try again!")
    return letters_entered


def get_letter_values():
    letter_values = {}
    letter_values.update({'A': 10000000000000000000000000})
    letter_values.update({'B': 1000000000000000000000000})
    letter_values.update({'C': 100000000000000000000000})
    letter_values.update({'D': 10000000000000000000000})
    letter_values.update({'E': 1000000000000000000000})
    letter_values.update({'F': 100000000000000000000})
    letter_values.update({'G': 10000000000000000000})
    letter_values.update({'H': 1000000000000000000})
    letter_values.update({'I': 100000000000000000})
    letter_values.update({'J': 10000000000000000})
    letter_values.update({'K': 1000000000000000})
    letter_values.update({'L': 100000000000000})
    letter_values.update({'M': 10000000000000})
    letter_values.update({'N': 1000000000000})
    letter_values.update({'O': 100000000000})
    letter_values.update({'P': 10000000000})
    letter_values.update({'Q': 1000000000})
    letter_values.update({'R': 100000000})
    letter_values.update({'S': 10000000})
    letter_values.update({'T': 1000000})
    letter_values.update({'U': 100000})
    letter_values.update({'V': 10000})
    letter_values.update({'W': 1000})
    letter_values.update({'X': 100})
    letter_values.update({'Y': 10})
    letter_values.update({'Z': 1})
    return letter_values


def map_words(all_words, letter_values):
    all_words_map = {}
    for word in all_words:
        value = 0
        for letter in word:
            value += letter_values.get(letter, 0)
        words = all_words_map.get(value, [])
        words.append(word.strip('\n'))
        all_words_map.update({value: words})

    return all_words_map


def get_word_entered_value(letters_entered, letter_values):
    word_entered_value = 0
    for letter in letters_entered:
        word_entered_value += letter_values.get(letter, 0)
    return word_entered_value


def get_all_words(words_file):
    all_words_file = open(words_file, "r")
    all_words = all_words_file.readlines()
    return all_words


def get_all_word_entered_values(letters_entered, letter_values):
    word_entered_values = []
    word_entered_values_set = set()

    letters_entered_list = []
    for letter in letters_entered:
        letters_entered_list.append(letter)

    all_letter_combinations = \
        [''.join(l) for i in range(len(letters_entered_list)) for l in combinations(letters_entered_list, i + 1)]

    for letter_combination in all_letter_combinations:
        value = 0
        for letter in letter_combination:
            value += letter_values.get(letter)
        if value not in word_entered_values_set:
            word_entered_values_set.add(value)
            word_entered_values.append(value)

    return word_entered_values


def get_all_found_words(all_words_map, all_word_entered_values):
    found_values = set()
    found_words = list()
    for word_entered_value in all_word_entered_values:
        if word_entered_value not in found_values and all_words_map.get(word_entered_value) is not None:
            found_values.add(word_entered_value)
            found_words.append(all_words_map.get(word_entered_value))

    return found_words


def categorize_found_words(all_found_words):
    if len(all_found_words) < 1:
        return [], 0
    all_found_words_sorted = []
    current_word_length = len(all_found_words[0][0])
    sorted_words = []
    i = 0
    total_found_words = 0
    for words in all_found_words:
        i += 1
        for word in words:
            if len(word) > current_word_length:
                current_word_length = len(word)
                all_found_words_sorted.append(sorted_words)
                sorted_words = []
            sorted_words.append(word)
            total_found_words += 1
        if i == len(all_found_words):
            all_found_words_sorted.append(sorted_words)

    return all_found_words_sorted, total_found_words


def output_found_words(all_found_words_sorted, total_found_words, letters_entered):
    print("There are", total_found_words, "words that can be constructed with the letters:", letters_entered)
    for found_words_sorted in all_found_words_sorted:
        print(len(found_words_sorted[0]), "Letter words: ", end='')
        first_word = True
        for word in found_words_sorted:
            if not first_word:
                print(", ", end='')
            else:
                first_word = False
            print(word, end='')
        print()


def main():
    letters_entered = input_letters()

    letter_values = get_letter_values()

    all_words = get_all_words("All_Words.txt")

    all_words_map = map_words(all_words, letter_values)

    all_word_entered_values = get_all_word_entered_values(letters_entered, letter_values)

    all_found_words = get_all_found_words(all_words_map, all_word_entered_values)

    all_found_words_categorized, total_found_words = categorize_found_words(all_found_words)

    output_found_words(all_found_words_categorized, total_found_words, letters_entered)


if __name__ == '__main__':
    main()
