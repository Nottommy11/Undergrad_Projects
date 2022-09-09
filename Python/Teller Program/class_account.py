import functions_parent


class Account:
    # Makes it easier to know the amount of accounts instead of having to find the size of these other attributes
    _numAccts = 0
    # Used to track the active account's position in the _position list
    _activePos = None
    # Makes it easier to get the customer's name
    _fullName = []
    # Makes it easier to get the account number
    _acctNum = []
    # A list that contains each instance of the Account class, makes referencing those accounts possible
    _position = []

    def __init__(self, fullName, acctNum, balance):
        # Increase the number of accounts in the Account class with each instance
        Account._numAccts += 1
        # Pass the customer's name into this list
        self._fullName.append(fullName)
        # Pass the account number into this list
        self._acctNum.append(acctNum)
        # Pass the instance of the Account class into this list
        self._position.append(self)
        self.fullName = fullName
        self.balance = balance
        self.acctNum = acctNum

    def deposit(self, amtDep):
        self.balance = float(self.balance) + float(amtDep)

    def withdraw(self, amtWtd):
        self.balance = float(self.balance) - float(amtWtd)

    # Used to show basic info about the account
    def showInfo(self):
        print(f"     Name:                   {self.fullName}")
        if self.acctNum[3] in functions_parent.ckgList:
            print(f"     Account Type:           Checking")
        if self.acctNum[3] in functions_parent.svgList:
            print(f"     Account Type:           Savings")
        print(f"     Account Number:         {self.acctNum}")
        print(f"     Balance:                {self.balance}")
