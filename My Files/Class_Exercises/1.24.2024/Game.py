from random import randint


class Game:
    def __init__(self):
        self.__turn = 0
        self.__totalScore = 0
        self.__turnScore = 0
        self.__turnState = True

    def start(self):
        while True:
            if self.__totalScore < 20:
                self.update()
            else:
                print(f"\nYou finished in {self.__turn} turns!")
                break

    def update(self):
        self.__turn += 1
        print("\nTURN", self.__turn)
        while self.__turnState:
            self.turn_logic()
        self.__turnState = True

    def turn_logic(self):
        userInput = input("Roll or hold? (r/h): ").lower()

        if userInput == "r":
            die = self.roll()
            self.__turnScore += die
            print("Die:", die)
            if die == 1:
                print("End of turn.")
                self.__turnScore = 0
                self.__turnState = False

        elif userInput == "h":
            print("Score for turn:", self.__turnScore)
            self.__totalScore += self.__turnScore
            self.__turnScore = 0
            print("Total score:", self.__totalScore)
            self.__turnState = False

        else:
            print("Invalid option. Please try again.")

    def roll(self) -> int:
        return randint(1, 6)
