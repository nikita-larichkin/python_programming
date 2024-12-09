import csv


def get_books(word) -> []:
    with open("books.csv", mode='r', encoding='utf-8') as f:
        scaner = csv.reader(f, delimiter='|')
        ans = []

        for line in scaner:
            if word.lower() in line[1].lower():
                ans.append(line)

        return ans


def get_totals(data, fee=100) -> []:
    ans = []

    if (int(data[0][3]) * float(data[0][4])) < 500:
        ans.append((data[0][0], int(data[0][3]) * float(data[0][4]) + fee))
    else:
        ans.append((data[0][0], int(data[0][3]) * float(data[0][4])))

    return ans
