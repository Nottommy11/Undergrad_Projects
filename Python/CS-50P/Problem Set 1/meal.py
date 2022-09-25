# 24-hour clock
def main():
    hours, minutes = input("Time: ").split(":")
    time = convert(hours, minutes)

    if time >= 7 and time <= 8:
        print("breakfast time")

    elif time >= 12 and time <= 13:
        print("lunch time")

    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(hours, minutes):
    time = float(hours) + (float(minutes) / 60)
    return time


if __name__ == "__main__":
    main()


"""
# a.m./p.m. support
def main():
    time = input("Time: ")
    time = convert(time)

    if time >= 7 and time <= 8:
        print("breakfast time")

    elif time >= 12 and time <= 13:
        print("lunch time")

    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time="Test"):

    if time.endswith("a.m."):
        hours, minutes = time.rstrip("a.m.").split(":")
        time = float(hours) + (float(minutes) / 60)

    elif time.endswith("p.m."):
        hours, minutes = time.rstrip("p.m.").split(":")
        time = float(hours) + 12 + (float(minutes) / 60)

    return time


if __name__ == "__main__":
    main()
"""