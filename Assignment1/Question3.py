from dataclasses import dataclass
import csv

fileName = "customers.csv"


@dataclass
class Customer:
    id: int
    firstName: str
    lastName: str
    company: str
    address: str
    city: str
    state: str
    zip: str

    def view(self):
        if self.company == '':
            print(f"\n"
                  f"{self.firstName} {self.lastName}\n"
                  f"{self.address}\n"
                  f"{self.city}, {self.state} {self.zip}")
        else:
            print(f"\n"
                  f"{self.firstName} {self.lastName}\n"
                  f"{self.company}\n"
                  f"{self.address}\n"
                  f"{self.city}, {self.state} {self.zip}")


def customer_parser(filename: str) -> list:
    customers = []
    with open(filename, newline='') as csvFile:
        file = csv.reader(csvFile, delimiter=',')
        for row in file:
            if not row[0].isnumeric():
                continue
            customers.append(Customer(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    return customers


def get_id() -> int:
    while True:
        idNum = input("\nEnter customer ID: ")
        if idNum.isnumeric():
            return int(idNum)
        print("Invalid ID Number.")


def main():
    print("Customer Viewer")

    customers = customer_parser(fileName)

    while True:
        userID = get_id()
        try:
            [customer] = [c for c in customers if c.id == userID]
            customer.view()
        except ValueError:
            print("\nNo customer with that ID.")

        if input("\nContinue? (y/n): ").lower() != 'y':
            print("\nBye!")
            break


if __name__ == "__main__":
    main()
