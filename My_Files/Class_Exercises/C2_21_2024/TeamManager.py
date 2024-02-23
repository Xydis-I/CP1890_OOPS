from Player import Player
from Lineup import Lineup
from datetime import datetime, timedelta


def main() -> None:
    main_menu()
    lineup = Lineup()
    players = lineup.get_players()
    user_interface(lineup)


def main_menu() -> None:
    print('=' * 64)
    print(f"{'Baseball team Manager':>40}\n")
    currentDate = datetime.now().date()
    print("CURRENT DATE:\t", currentDate)
    gameDate = datetime.fromisoformat(input("GAME DATE:\t\t ")).date()
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
    print(*Lineup.get_positions(), sep=', ')
    print('=' * 64, end='')


def user_interface(lineup: Lineup) -> None:
    while True:
        userInput = input("\nMenu Option: ")
        if userInput == '1':
            display_lineup(lineup)
        elif userInput == '2':
            add_player(lineup)
        elif userInput == '7':
            print("Bye!")
            break
        else:
            print("Invalid option. Please try again.")


def display_lineup(lineup: Lineup) -> None:
    print(f"{'Player':>9}{'POS':>32}{'AB':>9}{'H':>6}{'AVG':>8}")
    print('-' * 64)
    for n, player in enumerate(lineup.get_players(), 1):
        print(f"{n:<3d}{player.firstName+' '+player.lastName:35}{player.position:3}"
              f"{player.atBats:>9}{player.hits:>6}{player.avg:>8.3f}")


def add_player(lineup: Lineup) -> None:
    while True:
        try:
            firstName = input("First name: ")
            lastName = input("Last name: ")
            position = input("Position: ").upper()
            if position not in Lineup.get_positions():
                raise ValueError
            atBats = get_int("At bats: ")
            hits = get_int("Hits: ")
            lineup.add_player(firstName, lastName, position, atBats, hits)
            print(f"{firstName} {lastName} was added.")
            break
        except ValueError:
            print("Invalid input. Please try again.")


def get_int(message: str) -> int:
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == '__main__':
    main()
