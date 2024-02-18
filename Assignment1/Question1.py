"""
Question 1: Rectangle Program
Group Member: Matthew King
"""

from dataclasses import dataclass


@dataclass
class Rectangle:
    """
    Class object that represents a rectangle.
    With attitudes of height and width
    and methods to find the area and the perimeter
    of the rectangle.
    """
    height: int = 0
    width: int = 0

    @property
    def get_height(self):
        return self.height

    @get_height.setter
    def get_height(self, value):
        if value <= 0:
            raise ValueError("Height cannot be less than or equal 0")
        else:
            self.height = int(value)

    @get_height.getter
    def get_height(self):
        return int(self.height)

    @property
    def get_width(self):
        return self.width

    @get_width.setter
    def get_width(self, value):
        if value <= 0:
            raise ValueError("Width cannot be less than or equal 0")
        else:
            self.width = int(value)

    @get_width.getter
    def get_width(self):
        return int(self.width)

    def area(self) -> int:
        """
        Method that calculates the area of the rectangle.
        :return:
        Area of the rectangle as 'rec_area' -> integer.
        """
        rec_area = self.width * self.height
        return int(rec_area)

    def perimeter(self):
        """
        Method that calculates the perimeter of the rectangle.
        :return:
        Perimeter of the rectangle as 'rec_perimeter' -> integer.
        """
        rec_perimeter = (self.width * 2) + (self.height * 2)
        return int(rec_perimeter)

    def string_representation(self):
        """
        Method that prints a string representation of the rectangle
        Handles cases where width and height are 1 as well.
        """
        if self.height == 1 and self.width == 1:
            print('*')
        elif self.height == 1:
            print("* " * self.width)
        elif self.width == 1:
            for line in range(self.height):
                print("*")
        else:
            empty_width = self.width * 2 - 3
            print('* '*self.width)
            for line in range(self.height - 2):
                print(f"{'*'}{' ' * empty_width}{'*'}")
            print('* ' * self.width)


def main():
    print('Rectangle Calculator\n')
    rec = Rectangle()
    while True:
        rec.get_height = int(input(f"{'Height:':<11}"))
        rec.get_width = int(input(f"{'Width:':<11}"))
        perimeter = rec.perimeter()
        area = rec.area()
        print(f"{'Perimeter:':<11}{perimeter}")
        print(f"{'Area:':<11}{area}")
        rec.string_representation()
        cont = input("\nContinue? (y/n) : ")
        print()
        if cont == 'y':
            continue
        elif cont == 'n':
            break
        else:
            print("Invalid input entered")


if __name__ == '__main__':
    main()
    print('\nBye!')
