class Player:
    def __init__(self, firstName: str, lastName: str, position: str, atBats: int, hits: int):
        self.__firstName: str = firstName
        self.__lastName: str = lastName
        self.position: str = position
        self.__atBats: int = atBats
        self.__hits: int = hits

    @staticmethod
    def get_positions():
        return ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P']

    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        if self.get_positions().count(pos) > 0:
            self.__position = pos
        else:
            raise ValueError("Invalid position.")

    def get_atBats(self):
        return self.__atBats

    def get_hits(self):
        return self.__hits

    def get_avg(self):
        try:
            return self.__hits / self.__atBats
        except ZeroDivisionError:
            return 0
