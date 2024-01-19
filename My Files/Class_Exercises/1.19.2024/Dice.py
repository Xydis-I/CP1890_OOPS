from Die import Die


class Dice:
    def __init__(self):
        self.die_list = []

    def addDice(self, die: int):
        for d in range(0, die):
            self.die_list.append(Die())

    def rollAll(self):
        for die in self.die_list:
            die.roll()
