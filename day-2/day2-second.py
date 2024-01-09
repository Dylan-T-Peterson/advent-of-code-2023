#! ../venv/bin/python3
from functools import reduce
from re import compile


def main():
    RED_REG = compile(r"\d+ red")
    GREEN_REG = compile(r"\d+ green")
    BLUE_REG = compile(r"\d+ blue")
    answer = 0
    puzzle = open("./input.txt", "r").read().split("\n")[:-1]

    for game in puzzle:
        min_values = {"red": 0, "green": 0, "blue": 0}
        pulls = game.split(": ")[1]

        # Iterates through corrosponding regex and min values for a color
        # Then extracts the max value for that color
        # Uses the reduce function to iterate over the min values to find power
        for reg, color in zip([RED_REG, GREEN_REG, BLUE_REG], min_values.keys()):
            vals = [int(pull.split(" ")[0]) for pull in reg.findall(pulls)]
            min_values[color] = max(vals)
        power = reduce((lambda x, y: x * y), min_values.values())
        answer += power
    print(answer)


if __name__ == "__main__":
    main()
