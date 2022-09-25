def main():
    userInput = input()
    print(convert(userInput))

def convert(input="Test"):
    input = input.replace(":)", "🙂")
    input = input.replace(":(", "🙁")
    return input

main()