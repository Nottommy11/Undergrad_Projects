import random
import string


def main():
    raw_input = input("Enter: ")

    raw_input = raw_input.replace(">", "").replace("<", ",").replace(";", ",")

    # print(raw_input)

    csv_list = raw_input.split(",")
    # print(f"CSV: {csv_list}")

    name_list = []
    email_list = []

    for thing in range(len(csv_list)):
        if thing % 2 == 0:
            name_list.append(csv_list[thing])
        else:
            email_list.append(csv_list[thing])

    print("NAMES:")
    for thing in range(len(name_list)):
        name_list[thing].lstrip()
        print(name_list[thing])
    print()

    print("EMAILS:")
    for thing in range(len(email_list)):
        print(email_list[thing])


if __name__ == "__main__":
    main()
