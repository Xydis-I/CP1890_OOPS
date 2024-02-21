import Game


def main():
    print("Let's Play PIG!\n"
          "\n"
          "* See how many turns it takes you to get to 20.\n"
          "* Turn ends when you hold or roll a 1.\n"
          "* If you roll a 1, you lose all points for the turn.\n"
          "* If you hold, you save all points for the turn.")

    play_game()

    while True:
        if input("Play again? (y/n): ").lower() == 'y':
            play_game()
        else:
            break


def play_game():
    game = Game.Game()
    game.start()


if __name__ == '__main__':
    main()
