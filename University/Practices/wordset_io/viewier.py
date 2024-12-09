from read_file import *
from save_file import *


def show():
    words = read_file("data.txt")
    save_file("count.txt", words)


if __name__ == "__main__":
    show()
