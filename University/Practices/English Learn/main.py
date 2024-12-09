import pymorphy3
import concurrent.futures
from translate import Translator


def get_words(filename="text.txt") -> []:
    words = []

    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            words.extend(word.lower() for word in line.replace(',', '').replace('.', '').replace(')', '').replace('\n', '').split())

    return words


def normalize_words(words) -> []:
    morph_analyzer = pymorphy3.MorphAnalyzer()
    normalized_words = [morph_analyzer.parse(word)[0].normal_form for word in words]

    return normalized_words


def sort_words(words) -> []:
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

    return sorted_words


def translate_word(args):
    translator, word, count, i = args
    eng_word = translator.translate(word)
    return f"{word}|{eng_word}|{count}\n"


def translate_words_list(words) -> None:
    translator = Translator(from_lang="ru", to_lang="en")

    output_lines = ["Исходное слово|Перевод|Количество упоминаний\n"]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        args = ((translator, word, count, i) for i, (word, count) in enumerate(words, start=1))
        result_lines = list(executor.map(translate_word, args))

    output_lines.extend(result_lines)

    with open("translation.txt", "w", encoding="utf8") as f:
        f.writelines(output_lines)
