import functions_parent


class Customer:
    # Makes it easier to know the amount of customers instead of having to find the size of these other attributes
    _numCusts = 0
    # Used to track the active customer's position in the _position list
    _activePos = None
    # Makes it easier to get the customer's name
    _fullName = []
    # A list that contains each instance of the Customer class, makes referencing those customers possible
    _position = []

    def __init__(self, fullName):
        # Increase the number of customers in the Customer class with each instance
        Customer._numCusts += 1
        # Pass the customer's name into this list
        self._fullName.append(fullName)
        # Pass the instance of the Customer class into this list
        self._position.append(self)
        self.fullName = fullName
        self.numAccts = 0
        # Creates a list for account numbers to populate
        self.accts = []

    # Add the account number to the customer and increase their number of accounts
    def addAcct(self, acctNum):
        self.accts.append(acctNum)
        self.numAccts += 1

    # Lists the accounts that the customer has
    def listAccts(self):
        if self.numAccts > 0:
            for acctPos in range(self.numAccts):
                acctNum = self.accts[acctPos]
                if acctNum[3] in functions_parent.ckgList:
                    print(f"     Checking Account: {acctNum}")
                elif acctNum[3] in functions_parent.svgList:
                    print(f"     Savings Account:  {acctNum}")
        else:
            print("This customer doesn't have any accounts.")
