import functions_parent
from class_account import Account
from class_checking import Checking
from class_customer import Customer
from class_employee import Employee
from class_savings import Saving


# Loads the information related to employees saved in the employee file
def loadEmpList():
    # Used with as I believe it is better than opening and closing the file. I saw that this can be
    # better at handling errors
    with open("emp_file.txt", "r") as empFile:
        empLine = empFile.readline()
        # Loop will read all lines in the file
        while empLine:
            # Assigning values by splitting at commas
            fullName, userName, pwd = empLine.split(",", 2)
            # Had issues with the last item on the line, but this seemed to work
            pwd = pwd.strip()
            # Create an employee object from the empLine
            Employee(fullName, userName, pwd)
            # Read the next line and start loop again
            empLine = empFile.readline()


# Loads the information related to customers and their accounts saved in the customer and accounts file
def loadCustAcctList():
    # Used with as I believe it is better than opening and closing the file. I saw that this can be
    # better at handling errors
    with open("cust_acct_file.txt", "r") as custAcctFile:
        custLine = custAcctFile.readline()
        # Loop will read all lines in the file
        while custLine:
            # Assigning values by splitting at commas
            fullName, numAccts = custLine.split(",")
            # Had issues with the last item on the line, but this seemed to work
            numAccts = numAccts.strip()
            # Did this to work around having to call a longer argument for the customer object
            tempCust = Customer(fullName)
            # Used the numAccts to determine how many lines to read based on the number of accounts
            for acctLine in range(int(numAccts)):
                acctLine = custAcctFile.readline()
                # Assigning values by splitting at commas
                acctNum, balance = acctLine.split(",")
                # Had issues with the last item on the line, but this seemed to work
                balance = balance.strip()
                # Checking if the account is a checking or savings account based on the 4th digit
                if acctNum[3] in functions_parent.ckgList:
                    # Create the checking account
                    Checking(fullName, acctNum, balance)
                    # Add the account to the customer
                    tempCust.addAcct(acctNum)
                elif acctNum[3] in functions_parent.svgList:
                    # Create the savings account
                    Saving(fullName, acctNum, balance)
                    # Add the account to the customer
                    tempCust.addAcct(acctNum)
            # Read the next line to continue the loop
            custLine = custAcctFile.readline()


def saveEmpList():
    # Used with as I believe it is better than opening and closing the file. I saw that this can be
    # better at handling errors
    with open("emp_file.txt", "w") as empFile:
        # Will print a line in the file for the number of employees
        for empLine in range(Employee._numEmps):
            fullName = Employee._fullName[empLine]
            userName = Employee._position[empLine].userName
            pwd = Employee._position[empLine].pwd
            # Print comma separated values in the file to store the employee's information
            empFile.write(f"{fullName},{userName},{pwd}\n")


def saveCustAcctList():
    # Used with as I believe it is better than opening and closing the file. I saw that this can be
    # better at handling errors
    with open("cust_acct_file.txt", "w") as custAcctFile:
        # Will print a line in the file for the number of customers
        for custLine in range(Customer._numCusts):
            fullName = Customer._fullName[custLine]
            numAccts = Customer._position[custLine].numAccts
            # Print comma separated values in the file to store the customer's information
            custAcctFile.write(f"{fullName},{numAccts}\n")
            # Will print a line in the file for the number of accounts corresponding to the current customer
            for acctLine in range(numAccts):
                acctNum = Customer._position[custLine].accts[acctLine]
                # Checking for a match in the Account class to match the balance to the account
                for acctPos in range(Account._numAccts):
                    if acctNum == Account._acctNum[acctPos]:
                        balance = Account._position[acctPos].balance
                # Print comma separated values in the file to store the account's information
                custAcctFile.write(f"{acctNum},{balance}\n")
