class Player:
    def __init__(self, firstName, lastName, position, atBats, hits):
        self.__firstName: str = firstName
        self.__lastName: str = lastName
        self.position: str = position
        self.__atBats: int = atBats
        self.__hits: int = hits

    positions = ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P']

    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        if self.positions.count(pos) > 0:
            self.__position = pos
        else:
            raise ValueError("Invalid position.")
