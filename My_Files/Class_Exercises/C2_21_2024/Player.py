class Player:
    def __init__(self, firstName: str, lastName: str, position: str, atBats: int, hits: int):
        self._firstName: str = firstName
        self._lastName: str = lastName
        self._position: str = position
        self._atBats: int = atBats
        self._hits: int = hits

    @property
    def firstName(self) -> str:
        return self._firstName

    @property
    def lastName(self) -> str:
        return self._lastName

    @property
    def position(self) -> str:
        return self._position

    @property
    def atBats(self) -> int:
        return self._atBats

    @property
    def hits(self) -> int:
        return self._hits

    @property
    def avg(self) -> float:
        try:
            return self._hits / self._atBats
        except ZeroDivisionError:
            return 0
