def main():
    try:
        user_input = input("Fraction: ")
        val_1, val_2 = user_input.split("/")

        if int(val_1) > int(val_2):
            main()

        fuel_gauge = (int(val_1) / int(val_2)) * 100

        if round(fuel_gauge) <= 1:
            print("E")
        elif round(fuel_gauge) >= 99:
            print("F")
        else:
            print(f"{round(fuel_gauge)}%")

    except (ValueError, ZeroDivisionError):
        main()


if __name__ == "__main__":
    main()
