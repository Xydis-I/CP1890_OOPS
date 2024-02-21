from Die import Die


class Dice:
    def __init__(self):
        self.__list = []

    def addDice(self, die: int):
        for d in range(0, die):
            self.__list.append(Die())

    def rollAll(self):
        for die in self.__list:
            die.roll()

    def getDieList(self):
        return self.__list
