from dataclasses import dataclass
from Player import Player


@dataclass
class Lineup:
    players = [Player("Tommy", "La Stella", "3B", 1316, 360),
               Player("Mike", "Yastrzemski", "RF", 563, 168),
               Player("Donovan", "Solano", "2B", 1473, 407),
               Player("Buster", "Posey", "C", 4575, 1380),
               Player("Brandon", "Belt", "1B", 3811, 1003),
               Player("Brandon", "Crawford", "SS", 4402, 1099),
               Player("Alex", "Dickerson", "LF", 586, 160),
               Player("Austin", "Slater", "CF", 569, 147),
               Player("Kevin", "Gauman", "P", 56, 2)]

    def get_players(self):
        for player in self.players:
            yield player
