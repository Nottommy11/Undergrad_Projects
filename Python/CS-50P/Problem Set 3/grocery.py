def main():
    grocery_list = {}

    try:
        while(True):
            item = input()

            if item.title() in grocery_list:
                grocery_list[item.title()] += 1
            else:
                grocery_list[item.title()] = 1
    except EOFError:
        sorted_list = dict(sorted(grocery_list.items()))

        for key, value in sorted_list.items():
            print(f"{value} {key.upper()}")

        exit()


if __name__ == "__main__":
    main()
