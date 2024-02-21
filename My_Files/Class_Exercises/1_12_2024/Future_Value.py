import locale as lc


def get_investment() -> float:
    while True:
        try:
            investment = float(input("Enter monthly investment:\t "))
            return investment
        except ValueError:
            print("Invalid input.")


def get_rate() -> float:
    while True:
        try:
            rate = float(input("Enter monthly investment:\t "))
            return rate
        except ValueError:
            print("Invalid input.")


def get_year() -> int:
    while True:
        try:
            year = int(input("Enter monthly investment:\t "))
            return year
        except ValueError:
            print("Invalid input.")


def main():
    while True:
        mon_investment = get_investment()
        rate = get_rate()
        years = get_year()

        lc.setlocale(lc.LC_ALL, 'en-ca')

        total = 0
        for year in range(years * 12):
            total += mon_investment
            total *= (1 + (rate/12/100))

        print(f"\nMonthly investment: {lc.currency(mon_investment, grouping=True):>12s}")
        print(f"Interest rate: {rate:>17.1f}")
        print(f"Years: {years:>25d}")
        print(f"Future Value: {lc.currency(total, grouping=True): >18s}")

        if input("\nContinue? (y/n) ").lower() != 'y':
            break


if __name__ == '__main__':
    main()
