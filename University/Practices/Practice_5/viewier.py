from file_util import *


def show():
    print('Введите "выход" чтобы завершить программу.')
    while True:
        file = input("Введите имя файла: ")

        if file == "выход":
            break

        print(get_numbers(file))


if __name__ == "__main__":
    show()
