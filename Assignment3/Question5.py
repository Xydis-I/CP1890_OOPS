# Question #5
import datetime
import csv
import sqlite3
from dataclasses import dataclass


DATE_FORMAT = "YYYY-MM-DD"


conn = sqlite3.connect("SupportingFiles/Question5/Q5Database.sqlite")
c = conn.cursor()


@dataclass
class Region:
    code: str
    name: str


@dataclass
class Regions:
    regions: list

    def add(self, region):
        self.regions.append(region)


@dataclass
class DailySales:
    id: int
    amount: float
    salesDate: str
    region: str
    quarter: int

    def fromDb(self):
        pass


@dataclass
class SalesList:
    sales: list


class Db:
    def import_csv(self):
        fileName = input("File name: ")
        with open(fileName) as csvFile:
            file = csv.reader(csvFile, delimiter=',')
            next(file)  # Skips Header
            for line in file:
                c.execute(f"""INSERT INTO Sales VALUES (NULL, {line[1]}, "{line[2]}", "{line[3]}");""")
            conn.commit()


def view():
    print(f"{'Date':>9}{'Quarter':>18}{'Region':>14}{'Amount':>19}")
    print(60 * '-')


def menu():
    print("\n"
          "COMMAND MENU\n"
          "view   - View all sales\n"
          "add    - Add sales\n"
          "import - Import sales from file\n"
          "menu   - Show menu\n"
          "exit   - Exit program")


def main():
    print("SALES DATA IMPORTER")
    menu()

    while True:
        command = input("\nPlease enter a command: ").lower()

        if command == "view":
            view()
        elif command == "add":
            pass
        elif command == "import":
            pass
        elif command == "menu":
            menu()
        elif command == "exit":
            print("\nBye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
