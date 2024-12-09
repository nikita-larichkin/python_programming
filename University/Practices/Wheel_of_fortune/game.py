from random import *
from file_utils import *


def game():
    global default_health
    word_list = get_words()
    record = 0
    hidden_word = []

    playing = True

    word = word_list.pop(randint(0, len(word_list) - 1))

    for i in range(0, len(word)):
        hidden_word.append("\u25A0")

    while playing:
        level = input("Выберите сложность:\n1 - Легко.\n2 - Средне.\n3 - Сложно.\n4 - Одна жизнь.\n")
        match level:
            case '1':
                default_health = 7
                break
            case '2':
                default_health = 5
                break
            case '3':
                default_health = 3
                break
            case '4':
                default_health = 1
                break
            case _:
                print("Вы ввели неправильное значение!")

    health = default_health
    letter = ""

    while True:

        if "".join(hidden_word) != word and health > 0:
            word_hide_str = " ".join(hidden_word)
            print(f"{word_hide_str} | \u2665x{health}")
            letter = input("Назовите букву или слово целиком: ")

        if len(letter) != 1 and len(letter) != len(word):
            print("Неккоректный ввод\n")

        elif letter.upper() != word and len(letter) == len(word):
            print(f"\nВы проиграли.")
            print(f"Счёт: {record}")
            break

        elif letter.upper() == word or "".join(hidden_word) == word:
            record += 1
            print("".join(word))
            print("Вы угадали слово!")
            print(f"Счёт: {record}")

            if not word_list:
                break

            elif input("Вы хотите продолжить (да/нет)? ") == "да":
                health = default_health

                word = word_list.pop(randint(0, len(word_list) - 1))

                hidden_word.clear()
                for i in range(0, len(word)):
                    hidden_word.append("\u25A0")
            else:
                break
        elif letter.upper() in hidden_word:
            print("Такая буква уже есть.")

        elif letter.upper() in word:
            for i in range(0, len(word)):
                if word[i] == letter.upper():
                    hidden_word[i] = letter.upper()

        elif health == 0:
            print(f"Вы проиграли.")
            print(f"Счёт: {record}")
            break

        else:
            health -= 1
            print("Неправильно. Вы теряете жизнь")

        if not word_list and not playing:
            break

    if record == get_records(record):
        print("\nПоздравляем! Вы установили новый рекорд!")
    print(f"\nВы угадали одно слово.\nРекорд: {get_records(record)}" if record == 1 else(f"\n\nВы угадали {record} слов подряд.\nРекорд: {get_records(record)}" if record % 10 > 4 or record % 10 == 0 else(f"\n\nВы угадали {record} слова подряд.\nРекорд: {get_records(record)}")))


if __name__ == "__main__":
    game()

