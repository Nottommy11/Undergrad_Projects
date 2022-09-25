userInput = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

if userInput == "42":
    print("Yes")
elif userInput == "forty-two":
    print("Yes")
elif userInput == "forty two":
    print("Yes")
else:
    print("No")