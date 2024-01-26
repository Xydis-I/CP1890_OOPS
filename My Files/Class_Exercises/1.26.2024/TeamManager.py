import Player, datetime


def main():
    main_menu()


def main_menu():
    print('=' * 70)
    print(f"{'Baseball team Manager':>40}\n")
    currentDate = datetime.datetime.now().date()
    print("CURRENT DATE:\t", currentDate)
    gameDate = datetime.datetime.fromisoformat(input("GAME DATE:\t\t ")).date()
    print("DAYS UNTIL GAME:", (gameDate - currentDate).days)


if __name__ == '__main__':
    main()
