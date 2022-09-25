def main():

    valid_denoms = {5, 10, 25}
    amount_due = 50
    amount_owed = 0
    input_amount = 0

    while input_amount < 50:
        print(f"Amount Due:  {amount_due - input_amount}")
        user_input = int(input("Insert Coin: "))
        if user_input in valid_denoms:
            input_amount += user_input

    amount_owed = input_amount - amount_due
    print(f"Change Owed: {amount_owed}")


if __name__ == "__main__":
    main()