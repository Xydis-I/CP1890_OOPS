from Die import Die


class Dice:
    def __init__(self):
        self.__die_list = []

    def addDice(self, die: int):
        for d in range(0, die):
            self.__die_list.append(Die())

    def rollAll(self):
        for die in self.__die_list:
            die.roll()

    def getDieList(self):
        return self.__die_list
