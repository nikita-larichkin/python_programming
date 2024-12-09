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
    for line in data:
        if (int(line[3]) * float(line[4])) < 500:
            ans.append((line[0], int(line[3]) * float(line[4]) + fee))
        else:
            ans.append((line[0], int(line[3]) * float(line[4])))

    return ans
