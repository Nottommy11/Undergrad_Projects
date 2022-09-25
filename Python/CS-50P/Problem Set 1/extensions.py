
def main():
    userInput = input("File Name: ").lower().strip()

    if userInput.endswith("gif"):
        imageFam("gif")
    elif userInput.endswith("jpg"):
        imageFam("jpeg")
    elif userInput.endswith("jpeg"):
        imageFam("jpeg")
    elif userInput.endswith("png"):
        imageFam("png")

    elif userInput.endswith("pdf"):
        appFam("pdf")
    elif userInput.endswith("zip"):
        appFam("zip")

    elif userInput.endswith("txt"):
        textFam("plain")

    else:
        print("application/octet-stream")


def imageFam(input):
    print(f"image/{input}")


def appFam(input):
    print(f"application/{input}")


def textFam(input):
    print(f"text/{input}")


main()