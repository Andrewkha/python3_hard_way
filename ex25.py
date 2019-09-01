def break_words(stuff: str):
    words = stuff.split(' ')
    return words


def sort_words(words: list):
    return sorted(words)


def print_first_word(words: list):
    word = words.pop(0)
    print(word)


def print_last_word(words: list):
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence: str):
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence: str):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence: str):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

