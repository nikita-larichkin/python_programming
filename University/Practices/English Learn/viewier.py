from main import *


def show():
    words = get_words()
    words = normalize_words(words)
    words = sort_words(words)
    translate_words_list(words)


if __name__ == "__main__":
    show()
