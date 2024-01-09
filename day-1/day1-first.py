#! ../venv/bin/python3
import re


def main():
    puzzle = open("./input.txt", "r").read()[:-1]
    regex = re.compile(r"\d")
    total = 0

    for line in puzzle.split("\n"):
        matches = regex.findall(line)
        digit1, digit2 = matches[0], matches[-1]
        calnum = int(f"{digit1}{digit2}")
        total += calnum
    print(total)


if __name__ == "__main__":
    main()
