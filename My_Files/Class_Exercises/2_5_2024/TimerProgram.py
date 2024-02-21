from datetime import datetime


def main():
    print("The Timer program\n\n"
          "Press Enter to start...", end='')
    input()
    start = datetime.now()
    print(f"Start time: {start}\n\n"
          f"Press Enter to stop...", end='')
    input()
    stop = datetime.now()
    print(f"Stop time: {stop}\n\n"
          f"ELAPSED TIME\n"
          f"Time: {stop - start}")


if __name__ == '__main__':
    main()
