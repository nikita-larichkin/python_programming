from random import randint


def monty_hall(iterations: int = 10000):
    count_other_door = 0

    for _ in range(0, iterations):
        player_door = randint(1, 3)
        door_not_empty = randint(1, 3)

        if player_door != door_not_empty:
            count_other_door += 1

    return count_other_door * 100 / iterations


def main():
    print(monty_hall())


if __name__ == "__main__":
    main()
