import re


def get_train_trips():
    file = open("log.txt", mode='r', encoding="utf8")
    lst = file.read().splitlines()
    matches = []
    pattern = r"Рейс\s\d+\s(отправился\sв|прибыл\sиз)\s\w+\sв\s(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])"

    for i in lst:
        string = i.split()
        match = re.search(pattern, i)

        if match:
            matches.append(f'[{string[-1]}] - Поезд № {string[1]} {string[3]} {string[-3]}')

    file.close()
    return matches


def save_data():
    file = open("schelude.txt", mode="w", encoding="utf8")
    lst_trips = get_train_trips()

    for i in lst_trips:
        file.write(f'{i}\n')
