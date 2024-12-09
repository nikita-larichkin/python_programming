def get_numbers(path: str):
    try:
        file = open(path, mode="r")

        numbers_amount = int(file.readline())
        numbers_list = []

        for i in range(numbers_amount):
            numbers_list += [int(file.readline())]

        file.close()
        return numbers_list

    except FileNotFoundError:
        return "Файл не найден."
    except ValueError:
        return "В файле не правильно указанны данные или присутствуют символы, не являющиеся числами."
    except OSError:
        return "Ошибка в системе"
