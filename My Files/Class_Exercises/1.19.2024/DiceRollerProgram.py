from Dice import Dice


def get_int(message: str) -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid number. Please Try Again.")


def main():
    print("The Dice Roller program\n")

    dieCount = get_int("Enter the number of dice to roll: ")
    dice = Dice()
    dice.addDice(dieCount)

    while True:
        dice.rollAll()
        values = [d.value for d in dice.die_list]
        print("YOUR ROLL:", *values)
        if input("\nRoll again? (y/n): ").lower() != "y":
            break
    print("Bye!")


if __name__ == "__main__":
    main()
