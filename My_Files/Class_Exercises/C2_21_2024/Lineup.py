from dataclasses import dataclass
from Player import Player


@dataclass
class Lineup:
    _players = [Player("Tommy", "La Stella", "3B", 1316, 360),
               Player("Mike", "Yastrzemski", "RF", 563, 168),
               Player("Donovan", "Solano", "2B", 1473, 407),
               Player("Buster", "Posey", "C", 4575, 1380),
               Player("Brandon", "Belt", "1B", 3811, 1003),
               Player("Brandon", "Crawford", "SS", 4402, 1099),
               Player("Alex", "Dickerson", "LF", 586, 160),
               Player("Austin", "Slater", "CF", 569, 147),
               Player("Kevin", "Gauman", "P", 56, 2)]

    @staticmethod
    def get_positions():
        return ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P']

    def get_players(self) -> list:
        for player in self._players:
            yield player

    def add_player(self, firstName: str, lastName: str, pos: str, atBats: int, hits: int) -> None:
        self._players.append(Player(firstName, lastName, pos, atBats, hits))

    def remove_player(self, index: int) -> None:
        print(f"{self._players.pop(index).firstName} {self._players.pop(index).lastName} was removed.")

    def move_player(self) -> None:
        pass

    def retrieve_player(self) -> Player:
        pass

    def edit_player(self) -> None:
        pass
