from Player import Player
import datetime


def main():
    main_menu()
    players = [Player("Tommy", "La Stella", "3B", 1316, 360),
               Player("Mike", "Yastrzemski", "RF", 563, 168),
               Player("Donovan", "Solano", "2B", 1473, 407),
               Player("Buster", "Posey", "C", 4575, 1380),
               Player("Brandon", "Belt", "1B", 3811, 1003),
               Player("Brandon", "Crawford", "SS", 4402, 1099),
               Player("Alex", "Dickerson", "LF", 586, 160),
               Player("Austin", "Slater", "CF", 569, 147),
               Player("Kevin", "Gauman", "P", 56, 2)]
    user_interface(players)


def main_menu():
    print('=' * 64)
    print(f"{'Baseball team Manager':>40}\n")
    currentDate = datetime.datetime.now().date()
    print("CURRENT DATE:\t", currentDate)
    gameDate = datetime.datetime.fromisoformat(input("GAME DATE:\t\t ")).date()
    print("DAYS UNTIL GAME:", (gameDate - currentDate).days)
    print("\n"
          "1 - Display lineup\n"
          "2 - Add player\n"
          "3 - Remove Player\n"
          "4 - Move player\n"
          "5 - Edit player position\n"
          "6 - Edit player stats\n"
          "7 - Exit program\n")
    print("POSITION")
    print(*Player.get_positions(), sep=', ')
    print('=' * 64, end='')


def user_interface(players: list):
    while True:
        userInput = input("\nMenu Option: ")
        if userInput == '1':
            display_lineup(players)
        elif userInput == '2':
            add_player(players)
        elif userInput == '7':
            print("Bye!")
            break
        else:
            print("Invalid option. Please try again.")


def display_lineup(players: list) -> None:
    print(f"{'Player':>9}{'POS':>32}{'AB':>9}{'H':>6}{'AVG':>8}")
    print('-' * 64)
    for n, player in enumerate(players, 1):
        print(f"{n:<3d}{player.get_firstName()+' '+player.get_lastName():35}{player.position:3}"
              f"{player.get_atBats():>9}{player.get_hits():>6}{player.get_avg():>8.3f}")


def add_player(players: list):
    try:
        fname = input("First name: ")
        lname = input("Last name: ")
        position = input("Position: ").upper()
        atBats = get_int("At bats: ")
        hits = get_int("Hits: ")
        players.append(Player(fname, lname, position, atBats, hits))
        print(f"{fname} {lname} was added.")
    except ValueError:
        print("Invalid input. Please try again.")


def get_int(message: str):
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == '__main__':
    main()
