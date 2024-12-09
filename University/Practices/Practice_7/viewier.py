from csv_util import *


def show():
    print('Введите "0" для выхода')
    while True:
        input_data = input('Введите слово для поиска книг: ')
        if input_data == "0":
            break
        data = get_books(input_data)
        print(data)
        print(get_totals(data))


if __name__ == "__main__":
    show()
