#! ../venv/bin/python3
import re


def main():
    total = 0

    puzzle = open("./input.txt", "r").read()
    regex = re.compile(r"\d")
    for line in puzzle.split("\n"):
        if line != "":
            matches = regex.findall(line)
            digit1, digit2 = matches[0], matches[-1]
            calnum = int(f"{digit1}{digit2}")
            total += calnum
        else:
            continue
    print(total)


if __name__ == "__main__":
    main()
