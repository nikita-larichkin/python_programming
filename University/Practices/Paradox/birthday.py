from random import randint


def birthday(people_in_group: int = 23, iterations: int = 10000):
    matches = 0

    for _ in range(0, iterations):
        groups = []
        for i in range(0, people_in_group):
            groups.append(randint(1, 365))

        counts = {}
        for person in groups:
            if person in counts:
                matches += 1
                break
            else:
                counts[person] = 1

    return matches * 100 / iterations


def main():
    print(birthday())


if __name__ == "__main__":
    main()
