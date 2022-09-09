import functions_account
import functions_parent
from class_account import Account
from class_customer import Customer


# The active customer will be set in the Customer class,
# can make it easier to know without always passing between functions
def setActiveCust(custName, custPos):
    # Checking if there is already an active customer set
    activeCustPos = Customer._activePos
    if activeCustPos is not None:
        # If there is an active customer, change it to none
        Customer._activePos = None
    if custPos is not None:
        # If the selected customer position is provided, just set the active customer to that position
        Customer._activePos = custPos
    else:
        # If no customer position was provided, get that position with their name
        custPos = getCustPos(custName)
        Customer._activePos = custPos


def getCustPos(custName):
    for custPos in range(Customer._numCusts):
        # If provided name equals a customer name, return the position
        if custName == Customer._fullName[custPos]:
            return custPos
    else:
        return None


def searchCust(custName, custPos, byPass, fromSearch):
    if custPos is None:
        custPos = getCustPos(custName)
        # This message is for users that put a non-customer in the search menu
        if custPos is None and fromSearch:
            print("This customer does not exist. If you would like to create them, select \"Create Account\"")
            functions_parent.largeSpaceSep()
            return
        elif custPos is None:
            Customer(custName)
            custPos = getCustPos(custName)
        # This bypass is for users that decide to create an account, but the customer still needs to be verified
        if byPass:
            return custPos
    setActiveCust(custName, custPos)
    dispCustMenu(custName, custPos)


def dispCustMenu(custName, custPos):
    # Make sure the program has the custPos
    if custPos is None:
        custPos = Customer._activePos
    functions_parent.smallSpaceSep()
    print(f"Customer's Name: {custName}")
    Customer._position[custPos].listAccts()
    functions_parent.smallSpaceSep()
    print(f"What would you like to do for {custName}?")
    print()
    print("     1 Create Account")
    print("     2 Deposit/Withdraw From an Account")
    print("     3 Display Customer Report")
    print("     4 Exit Menu")
    print()
    choice = input("Enter menu option (1-4): ")
    while choice not in ["1", "2", "3", "4"]:
        choice = input("Invalid choice. Choose menu option (1-4): ")
    functions_parent.largeSpaceSep()
    if choice == "1":
        functions_account.createAcct(custName, custPos)
    elif choice == "2":
        acctNum = input("Which account would you like to enter?: ")
        functions_account.searchAcct(acctNum, None)
    elif choice == "3":
        dispCustRep(custName, custPos)
    elif choice == "4":
        return True


def dispCustRep(custName, custPos):
    if custPos is None:
        custPos = Customer._activePos
    numAccts = Customer._position[custPos].numAccts
    print(f"Customer's Name:    {custName}")
    print(f"Number of Accounts: {numAccts}")
    for acctNumPos in range(numAccts):
        acctNum = Customer._position[custPos].accts[acctNumPos]
        acctPos = functions_account.getAcctPos(acctNum)
        acctType = functions_account.getAcctType(acctNum)
        if acctType == "Checking":
            print(f"     Checking Account: {acctNum}")
        elif acctType == "Savings":
            print(f"     Savings Account: {acctNum}")
        print(f"       Account Balance: {Account._position[acctPos].balance}")
    functions_parent.largeSpaceSep()
