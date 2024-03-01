from dataclasses import dataclass
from random import randint


@dataclass
class Player:
    name: str
    roshambo: str = "rock"

    def generate_roshambo(self):
        self.roshambo = "rock"

    def play(self, player):
        if self.roshambo == player.roshambo:
            return None

        if ((self.roshambo == "paper" and player.roshambo == "rock")
                or (self.roshambo == "rock" and player.roshambo == "scissors")
                or (self.roshambo == "scissors" and player.roshambo == "paper")):
            return self

        return player


@dataclass
class Bart(Player):
    name: str = "Bart"


@dataclass
class Lisa(Player):
    name: str = "Lisa"

    def generate_roshambo(self):
        self.roshambo = ["rock", "paper", "scissors"][randint(0, 2)]


@dataclass
class Roshambo:
    __wins: int = 0
    __loses: int = 0
    __player: Player = None
    __opponent: Player = None

    __choices = {'r': "rock", "p": "paper", "s": "scissors"}

    @property
    def wins(self):
        return self.__wins

    @property
    def loses(self):
        return self.__loses

    def add_win(self):
        self.__wins += 1

    def add_lose(self):
        self.__loses += 1

    def start_game(self):
        print("Roshambo\n")
        playerName = input("Enter your name: ")
        __player = Player(playerName)

        while True:
            opponentName = input("\nWould you like to play Bart or Lisa? (b/l): ").lower()
            if opponentName == "b":
                __opponent = Bart()
                break

            elif opponentName == "l":
                __opponent = Lisa()
                break

            else:
                print("\nInvalid input.")

        while True:
            while True:
                userInput = input("\nRock, paper, or scissors? (r/p/s): ").lower()

                if ["r", "p", "s"].count(userInput) == 1:
                    __player.roshambo = self.__choices[userInput]
                    break

                else:
                    print("\nInvalid input.")

            __opponent.generate_roshambo()

            print(f"\n{__player.name}: {__player.roshambo}")
            print(f"{__opponent.name}: {__opponent.roshambo}")

            winner = __player.play(__opponent)

            if winner is None:
                print("Draw!")

            else:
                if winner == __player:
                    self.add_win()
                else:
                    self.add_lose()

                print(f"{winner.name} wins!")

            if input("\nPlay again? (y/n): ").lower() != 'y':
                print("\nThanks for playing!")
                break


def main():
    game = Roshambo()
    game.start_game()


if __name__ == "__main__":
    main()
