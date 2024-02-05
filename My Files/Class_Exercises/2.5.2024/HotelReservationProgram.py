from datetime import datetime


def main():
    print("The Hotel Reservation program")

    while True:
        arrival = datetime.strptime(input("\nEnter arrival date (YYYY-MM-DD): "), "%Y-%m-%d")
        departure = datetime.strptime(input("Enter departure date (YYYY-MM-DD): "), "%Y-%m-%d")

        if arrival.month in [6, 7, 8]:
            season = "(High season)"
            rate = 105
        else:
            season = ""
            rate = 85

        print(f"\n"
              f"Arrival date:   {arrival:%B %d, %Y}\n"
              f"Departure date: {departure:%B %d, %Y}\n"
              f"Nightly rate:   ${rate:.2f} {season}\n"
              f"Total nights:   {(departure - arrival).days}\n"
              f"Total price:    ${(departure - arrival).days * rate}\n")

        if input("Continue? (y/n): ").lower() != 'y':
            print("\nBye!")
            break


if __name__ == '__main__':
    main()
