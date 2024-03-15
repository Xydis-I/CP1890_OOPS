# Question 2
from dataclasses import dataclass
from random import randint


@dataclass
class RandomIntList(list):
    __length: int

    def __post_init__(self):
        for num in range(self.__length):
            self.append(randint(1, 100))

    def __str__(self):
        return f", ".join([str(num) for num in self])

    @property
    def len(self):
        return len(self)

    @property
    def sum(self):
        return sum(self)

    @property
    def average(self):
        return f"{sum(self) / self.__length:.3f}"


def get_int(message: str) -> int:
    while True:
        num = input(message)
        if num.isnumeric():
            return int(num)
        print("Invalid integer. Please try again.")


def main():
    print("Random Integer List")

    num = get_int("\nHow many random integers should the list contain?: ")

    while True:
        int_list = RandomIntList(num)

        print(f"\n"
              f"Random Integers\n"
              f"===============\n"
              f"Integers:  {int_list}\n"
              f"Count:     {int_list.len}\n"
              f"Total:     {int_list.sum}\n"
              f"Average:   {int_list.average}\n")

        if input("\nContinue? (y/n): ").lower() != 'y':
            print("\nBye!")
            break


if __name__ == "__main__":
    main()
