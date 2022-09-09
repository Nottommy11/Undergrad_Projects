import random
from datetime import datetime
from random import randint

import functions_customer
import functions_parent
from class_account import Account
from class_checking import Checking
from class_customer import Customer
from class_savings import Saving


# Seed random with time. This creates the last 5 digits for the account number
def randAcctNum():
    random.seed(datetime.now())
    value = randint(10000, 99999)
    return str(value)


# The active account will be set in the Account class,
# can make it easier to know without always passing between functions
def setActiveAcct(acctNum, acctPos):
    # Checking if there is already an active account set
    activeAcctPos = Account._activePos
    if activeAcctPos is not None:
        # If there is an active account, change it to none
        Account._activePos = None
    if acctPos is not None:
        # If the selected account position is provided, just set the active account to that position
        Account._activePos = acctPos
    else:
        # If no account position was provided, get that position with the account number
        acctPos = getAcctPos(acctNum)
        Account._activePos = acctPos


def getAcctPos(acctNum):
    for acctPos in range(Account._numAccts):
        # If provided account number equals an account number in the Accounts class, return the position
        if acctNum == Account._acctNum[acctPos]:
            return acctPos
    else:
        return None


def searchAcct(acctNum, acctPos):
    if acctPos is None:
        acctPos = getAcctPos(acctNum)
        if acctPos is None:
            print("This account does not exist. If you would like to create it, select \"Create Account\"")
            return
    setActiveAcct(acctNum, acctPos)
    dispAcctMenu(acctNum, acctPos)


def createAcct(custName, custPos):
    if custName is None:
        custName = input("Please enter the customer's full name: ")
        # Verify that the customer exists
        custPos = functions_customer.searchCust(custName, None, True, False)
        if custPos is None:
            print("It appears that this is a new customer. This customer will be added to the system.")
            Customer(custName)
    functions_parent.smallSpaceSep()
    print(f"What kind of account would you like to create for {custName}?")
    print()
    print("     1 Checking")
    print("     2 Savings")
    print()
    choice = input("Enter menu option (1-2): ")
    while choice not in ["1", "2"]:
        choice = input("Invalid choice. Choose menu option (1-2): ")
    functions_parent.largeSpaceSep()
    if choice == "1":
        createCkg(custName, custPos)
    elif choice == "2":
        createSvg(custName, custPos)


def createCkg(custName, custPos):
    random.seed(datetime.now())
    # The 4th digit is decided based on this account being a checking account
    acctNum = "800" + str(randint(0, 7)) + randAcctNum()
    Checking(custName, acctNum, 0.00)
    # Add the account to the corresponding customer
    Customer._position[custPos].addAcct(acctNum)
    setActiveAcct(acctNum, None)


def createSvg(custName, custPos):
    random.seed(datetime.now())
    # The 4th digit is decided based on this account being a savings account
    acctNum = "800" + str(randint(8, 9)) + randAcctNum()
    Saving(custName, acctNum, 0.00)
    # Add the account to the corresponding customer
    Customer._position[custPos].addAcct(acctNum)
    setActiveAcct(acctNum, None)


def dispAcctMenu(acctNum, acctPos):
    if acctPos is None:
        acctPos = Account._activePos
    # Show the account balance and other useful account info
    functions_parent.smallSpaceSep()
    Account._position[acctPos].showInfo()
    functions_parent.smallSpaceSep()
    print(f"What would you like to do for account #{acctNum}?")
    print()
    print("     1 Deposit")
    print("     2 Withdraw")
    print("     3 Exit Menu")
    print()
    choice = input("Enter menu option (1-3): ")
    while choice not in ["1", "2", "3"]:
        choice = input("Invalid choice. Choose menu option (1-3): ")
    functions_parent.largeSpaceSep()
    if choice == "1":
        while True:
            try:
                # Make sure they enter a number
                amtDep = float(input("How much will be deposited?: "))
                if amtDep < 0:
                    # Make sure that number isn't less than 0
                    print("You cannot deposit a negative amount. Please try again.")
                    print()
                    continue
                break
            except ValueError:
                print("You must enter a number. Please try again.")
                print()
        Account._position[acctPos].deposit(amtDep)
    elif choice == "2":
        while True:
            try:
                # Make sure they enter a number
                amtWtd = float(input("How much will be withdrawn?: "))
                if amtWtd < 0:
                    # Make sure the number isn't less than 0
                    print("You cannot withdraw a negative amount. Please try again.")
                    print()
                    continue
                if amtWtd > float(Account._position[acctPos].balance):
                    # Also make sure they have enough money in their account
                    print("You cannot withdraw more than what is in the account. Please try again.")
                    print()
                    continue
                break
            except ValueError:
                print("You must enter a number. Please try again.")
                print()
        Account._position[acctPos].withdraw(float(amtWtd))
    elif choice == "3":
        return True
    # Show the new balance and other account info again
    functions_parent.smallSpaceSep()
    Account._position[acctPos].showInfo()
    functions_parent.smallSpaceSep()


# Checks the 4th digit to see if it is a checking or savings account
def getAcctType(acctNum):
    if acctNum[3] in functions_parent.ckgList:
        return "Checking"
    elif acctNum[3] in functions_parent.svgList:
        return "Savings"
