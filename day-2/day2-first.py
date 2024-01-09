#! ../venv/bin/python3
import re


def main():
    RED_REG = re.compile(r"\d+ red")
    GREEN_REG = re.compile(r"\d+ green")
    BLUE_REG = re.compile(r"\d+ blue")
    MAX_VALUES = {"red": 12, "green": 13, "blue": 14}
    answer = 0
    puzzle = open("./input.txt", "r").read().split("\n")[:-1]

    for game in puzzle:
        iterations = 0
        game_num, pulls = game.split(": ")
        game_num = int(game_num.split(" ")[1])

        # Iterates through corrosponding regex and max values for a color
        # Then checks if all colors passed the check
        for reg, max in zip([RED_REG, GREEN_REG, BLUE_REG], MAX_VALUES.values()):
            if (
                all(
                    max >= int(num)
                    for num in [pull.split(" ")[0] for pull in reg.findall(pulls)]
                )
            ) is False:
                break
            iterations += 1
        if iterations == 3:
            answer += game_num

    print(answer)


if __name__ == "__main__":
    main()
