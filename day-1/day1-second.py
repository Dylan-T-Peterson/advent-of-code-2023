#! ../venv/bin/python3
import re


def main():
    puzzle = open("./input.txt", "r").read()
    total = 0
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    regex = re.compile(f"(?=(\\d|{'|'.join(digits.keys())}))")

    for line in puzzle.split("\n")[:-1]:
        matches = regex.findall(line)
        digit1, digit2 = matches[0], matches[-1]

        if digit1 in digits:
            digit1 = digits[digit1]
        if digit2 in digits:
            digit2 = digits[digit2]

        calnum = int(f"{digit1}{digit2}")
        total += calnum
    print(total)


if __name__ == "__main__":
    main()
