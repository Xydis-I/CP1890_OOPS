from random import randint


class Die:
    def __init__(self):
        self.value = 1

    def roll(self):
        self.value = randint(1, 6)
