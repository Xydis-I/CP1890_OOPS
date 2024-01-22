from Dice import Dice


def get_int(message: str) -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid number. Please Try Again.")


def main():
    print("The Dice Roller program\n")

    die_count = get_int("Enter the number of dice to roll: ")
    dice = Dice()
    dice.addDice(die_count)

    while True:
        dice.rollAll()
        values = [d.getValue() for d in dice.getDieList()]
        print("YOUR ROLL:", *values)
        if input("\nRoll again? (y/n): ").lower() != "y":
            break
    print("Bye!")


if __name__ == "__main__":
    main()
