from random import randint


class Die:
    def __init__(self):
        self.__value = 1

    def roll(self):
        self.__value = randint(1, 6)

    def getValue(self):
        return self.__value
