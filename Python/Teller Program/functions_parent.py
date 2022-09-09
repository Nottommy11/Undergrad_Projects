import logging

import functions_employee
import functions_files
import functions_menu

# Used to check user input
yesList = ("Y", "y", "YES", "YEs", "Yes", "yes", "yeS", "yES")
noList = ("N", "n", "NO", "No", "no", "nO")
# Used to check account type at the 4th digit
ckgList = ("0", "1", "2", "3", "4", "5", "6", "7")
svgList = ("8", "9")


# Isn't needed currently, but could clean up a list and leave it as comma separated values
def cleanStringList(dirtyList):
    logging.info(f"Here is the list before replace: {dirtyList}")
    cleanList = dirtyList.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
    logging.info(f"Here is the list after replace: {cleanList}")
    return cleanList


# All of these are used to make the program "pretty"
def smallSep():
    print("-------------------------------------")


def smallSpaceSep():
    print()
    print("-------------------------------------")
    print()


def largeSep():
    print("=====================================")


def largeSpaceSep():
    print()
    print("=====================================")
    print()


# Calls on the specific functions to load files
def loadLists():
    functions_files.loadEmpList()
    functions_files.loadCustAcctList()


# Calls on the specific functions to save files
def saveLists():
    functions_files.saveEmpList()
    functions_files.saveCustAcctList()


# Runs the program in a loop until user decides to quit
def runProgram():
    exitProgram = False
    while exitProgram is False:
        functions_menu.header()
        if functions_employee.checkEmpAcct():
            # If the employee fails to signin, it will restart the program at the login page
            continue
        signOut = False
        while signOut is not True:
            signOut = functions_menu.mainMenu()
        userInput = input("Would you like to exit the program? (y/n): ")
        while userInput not in yesList and userInput not in noList:
            userInput = input("Invalid choice. Please enter \"y\" or \"n\": ")
        if userInput in yesList:
            # This will close the program and lead to saving the files
            exitProgram = True
        elif userInput in noList:
            # This will restart the program at the login page
            exitProgram = False

