import functions_parent


def main():

    # Load saved files
    functions_parent.loadLists()
    # Start the teller program
    functions_parent.runProgram()
    # Save files
    functions_parent.saveLists()


if __name__ == "__main__":
    main()
