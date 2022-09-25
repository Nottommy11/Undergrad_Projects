def main():
    camel_case = input("camelCase: ")

    while any(element.isupper() for element in camel_case):
        camel_case = make_snake(camel_case)

    snake_case = camel_case

    print(f"snake_case: {snake_case}")


def make_snake(camel_case):
    for char in range(len(camel_case)):
        if camel_case[char].isupper():
            camel_case = camel_case[:char] + "_" + camel_case[char].lower() + camel_case[char + 1:len(camel_case)]
    return camel_case


if __name__ == "__main__":
    main()
