import functions_parent
from class_employee import Employee


# The active employee will be set in the Employee class,
# can make it easier to know without always passing between functions
def setActiveEmp(empName, empPos):
    # Checking if there is already an active employee set
    activeEmpPos = Employee._activePos
    if activeEmpPos is not None:
        # If there is an active employee, change it to none
        Employee._activePos = None
    if empPos is not None:
        # If the selected employee position is provided, just set the active employee to that position
        Employee._activePos = empPos
    else:
        # If no employee position was provided, get that position with their name
        empPos = getEmpPos(empName)
        Employee._activePos = empPos


def getEmpPos(empName):
    for empPos in range(Employee._numEmps):
        # If provided name equals an employee name, return the position
        if empName == Employee._fullName[empPos]:
            return empPos
    else:
        return None


def checkEmpAcct():
    empName = input("Please enter your full name: ")
    empPos = getEmpPos(empName)
    functions_parent.smallSpaceSep()
    if empPos is None:
        # If the employee doesn't exist, allow them to create an account
        if createEmp(empName):
            return True
    # Not sure if I need this elif, but a good check anyway
    elif isinstance(empPos, int):
        # If the employee does exist, allow them to login
        if signIn(empName, empPos):
            return True


def createEmp(empName):
    print("It appears that there is no account associated with this name.")
    # Should help if somebody mistyped their name as well
    choice = input("Would you like to create one now? (y/n): ")
    # Checking input to make sure it is either a form of yes or no
    while choice not in functions_parent.yesList and choice not in functions_parent.noList:
        choice = input("Invalid choice. Please enter \"y\" or \"n\": ")
    # Will return to login page
    if choice in functions_parent.noList:
        print()
        print()
        return True
    userName = input("Enter a username with no spaces: ")
    while " " in userName:
        userName = input("Please re-enter you username WITH NO spaces: ")
    pwd = input("Enter a password with no spaces: ")
    while " " in pwd:
        pwd = input("Please re-enter you password WITH NO spaces: ")
    Employee(empName, userName, pwd)
    setActiveEmp(empName, None)
    print()
    functions_parent.smallSep()
    print(f"Welcome to the system, {empName}.")
    functions_parent.smallSep()
    print()


def signIn(empName, empPos):
    # Getting the login details loaded from employee
    userNameCheck = Employee._position[empPos].userName
    pwdCheck = Employee._position[empPos].pwd
    attempts = 0
    # User gets 5 attempts to log in, if failed, they will be returned to the login page
    while attempts < 5:
        userName = input("Enter your username: ")
        if userName == userNameCheck:
            break
        attempts += 1
    else:
        print("Your signin attempts exceeded 5. You will be returned to the signin page.")
        return True
    attempts = 0
    while attempts < 5:
        pwd = input("Enter your password: ")
        if pwd == pwdCheck:
            break
        attempts += 1
    else:
        print("Your signin attempts exceeded 5. You will be returned to the signin page.")
        return True
    setActiveEmp(empName, empPos)
    print()
    functions_parent.smallSep()
    print(f"Welcome back, {empName}.")
    functions_parent.smallSep()
    print()


def signOut():
    # Set no employee active and exit to allow them to choose to exit the program
    Employee._activePos = None
    return True
