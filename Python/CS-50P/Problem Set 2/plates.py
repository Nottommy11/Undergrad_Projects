def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if not 3 <= len(plate) <= 6:
        return False

    if plate[0].isdigit() or plate[1].isdigit():
        return False

    first_digit = None
    digits = ""

    for element in range(len(plate)):
        ascii_value = ord(plate[element])
        if not 48 <= ascii_value <= 57 and not 65 <= ascii_value <= 90:
            return False

        if first_digit is None and plate[element].isdigit():
            first_digit = str(plate[element])
            digits = str(plate[element:])

            if first_digit == "0":
                return False

    if any(element.isalpha() for element in digits):
        return False

    return True


main()