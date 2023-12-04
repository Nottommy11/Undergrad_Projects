def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0.00

    try:
        while(True):
            item = input("Item: ")

            if item.title() in menu:
                total += menu[item.title()]
                print(f"Total: ${format(total, ".2f")}")

    except EOFError:
        exit()


if __name__ == "__main__":
    main()
