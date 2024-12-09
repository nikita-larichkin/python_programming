def read_file(file):
    lst = []

    with open(file, mode="r", encoding="utf8") as text:
        for line in text:

            for i in line.split():
                lst.append(''.join(filter(str.isalnum, i.lower())))

    if '' in lst:
        lst.remove('')

    return list(set(lst))
