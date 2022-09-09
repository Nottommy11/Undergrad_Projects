import functions_account
import functions_customer
import functions_employee
import functions_parent


def header():
    print()
    print()
    functions_parent.largeSep()
    print("Welcome to ABC Bank's Teller Program")
    functions_parent.largeSep()
    print()


def mainMenu():
    print("What would you like to do?")
    print()
    print("     1 Search")
    print("     2 Create Account")
    print("     3 Sign Out")
    print()
    choice = input("Enter menu option (1-3): ")
    while choice not in ["1", "2", "3"]:
        choice = input("Invalid choice. Choose menu option (1-3): ")
    functions_parent.largeSpaceSep()
    if choice == "1":
        # User can search for customers and account numbers
        search()
    elif choice == "2":
        # User can create a customer and/or account
        functions_account.createAcct(None, None)
    elif choice == "3":
        # User will sign out and choose to exit the program or go back to the signin page
        return functions_employee.signOut()


def search():
    searchInput = input("Please enter a customer's full name or account number: ")
    # All account numbers start with 8
    if searchInput[0] == "8":
        functions_account.searchAcct(searchInput, None)
    # A customer's name has to start with an alphabetic character
    elif searchInput[0].isalpha():
        functions_customer.searchCust(searchInput, None, False, True)
    else:
        print("That is not an account number or a name. Please try again")
        print()
        # Just restarting the search function if they fail the input
        search()
