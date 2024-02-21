# Christian Barrett
# Question 2

from dataclasses import dataclass
import datetime

# Left in some comment lines that can be switched with the lines below them
# to view the outputs when using the sample datetime rather than the current.
# When using the sample datetime all outputs match given examples.


@dataclass
class Countdown:
    # current_datatime = datetime.datetime(2022, 10, 1, 10, 30)  # Sample Output Testing
    target_datetime: datetime.datetime

    @property
    def time_left(self):
        # time = self.target_datetime - self.current_datatime  # Sample Output Testing
        time = self.target_datetime - datetime.datetime.now()  # Real Current Time

        # timeDelta conversion
        hours = time.seconds // 3600
        minutes = (time.seconds // 60) - (hours * 60)
        seconds = time.seconds - (minutes * 60) - hours * 3600

        # return formatting
        if time.days > 0:
            return f"{time.days} days, {hours}:{minutes}:{seconds}"
        if time.days == 0:
            return f"{hours}:{minutes}:{seconds}"
        return f"-{hours}:{minutes}:{seconds}"

    @property
    def is_expired(self):
        # return self.target_datetime - self.current_datatime < datetime.timedelta(0)  # Sample Output Testing
        return self.target_datetime - datetime.datetime.now() < datetime.timedelta(0)  # Real Current Time


def main():
    # Sample Data
    target_datetime_1 = datetime.datetime(2022, 10, 1, 11, 0)
    target_datetime_2 = datetime.datetime(2023, 1, 1, 0, 0)
    target_datetime_3 = datetime.datetime(2021, 9, 30, 20, 0)

    countdown1 = Countdown(target_datetime_1)
    countdown2 = Countdown(target_datetime_2)
    countdown3 = Countdown(target_datetime_3)

    print(countdown1.time_left)
    print(countdown1.is_expired)
    print()
    print(countdown2.time_left)
    print(countdown2.is_expired)
    print()
    print(countdown3.time_left)
    print(countdown3.is_expired)


if __name__ == '__main__':
    main()
