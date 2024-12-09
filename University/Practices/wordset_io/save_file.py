from os import path


def save_file(file, words):
    count = len(words)
    new_words = sorted(words)

    if not path.exists(file):
        with open(file, mode='w', encoding="utf8") as text:
            text.write(f"Всего уникальных слов: {count}\n")

            for i in new_words:
                text.write(f'{i}\n')

    else:
        with open(file, mode='a', encoding="utf8") as text:
            for i in new_words:
                text.write(f'{i}\n')
