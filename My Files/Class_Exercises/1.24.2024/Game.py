from random import randint


class Game:
    def __init__(self):
        self.__turn = 0
        self.__totalScore = 0
        self.__turnScore = 0
        self.__turnState = True
        self.__dieValue = 0

    def start(self):
        while True:
            self.update()

    def update(self):
        self.__turn += 1
        while self.__turnState:
            self.turn_logic()

    def turn_logic(self):
        userInput = input("Roll or hold? (r/h): ")

    def roll(self) -> int:
        return randint(1, 6)
