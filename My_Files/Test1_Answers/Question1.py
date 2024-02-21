# Christian Barrett
# Question 1

from dataclasses import dataclass


@dataclass
class Rectangle:
    length: int
    width: int

    # Determine if object is square after initializing required values.
    def __post_init__(self):
        self._is_square = self.length == self.width

    # return absolute area
    @property
    def area(self) -> int:
        return abs(self.length) * abs(self.width)

    # return perimeter
    @property
    def perimeter(self) -> int:
        length = self.length
        width = self.width
        if length < 0:
            length = 0
        if width < 0:
            width = 0
        return 2 * length + 2 * width

    # Access private _is_square attribute as is_square property
    @property
    def is_square(self) -> bool:
        return self._is_square


def main():
    # Sample Data
    rect1 = Rectangle(5, 5)
    rect2 = Rectangle(6, 8)
    rect3 = Rectangle(-4, 4)

    print(rect1.area)
    print(rect1.perimeter)
    print(rect1.is_square)

    print(rect2.area)
    print(rect2.perimeter)
    print(rect2.is_square)

    print(rect3.area)
    print(rect3.perimeter)
    print(rect3.is_square)


if __name__ == '__main__':
    main()
