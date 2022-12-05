"""

TO ADD:

[X]    Data structure for the 8 pods
[X]    Data structure for the blood bags
[X]    Max of 100 bags
[X]    Hashing of blood type
[X]    ID numbers for blood bags
[X]    Draw dates
[X]    Expiration dates (21 days past draw)
[X]    Simulating each day/week
[X]    Check expiration dates
[X]    Removing expired bags
[X]    Adding 10 units of blood each day/week
[X]    Randomly generate blood leaving/expiring and arriving
[X]    User input blood type and draw date to be added
[X]    Output when blood is added and removed
[X]    Removing used bags
[X]    Store collisions of hashes, Use a set
[X]    Custom hashing of blood bags
[X]    Simulate blood being used
[X]    Queue for each blood type
[X]    Comment on all the code!
[X]    Make it look pretty


OPTIONAL/FUTURE ADDITIONS:
[]    Generate UPC Barcodes for blood bags
[]    User input for patient's blood type and compatible blood types
[]        Don't always use o neg for everything
[]        Use the most abundant blood type / Use an algorithm
[]    Daily/weekly reports
[]    Add console/file logging for collisions
        Example:
        ERROR! CHECK LOG AT LINE ##
"""

import gc
import queue
import string
from datetime import datetime, timedelta
from random import randint, choice, random

from abneg import ABNeg
from abpos import ABPos
from aneg import ANeg
from apos import APos
from bneg import BNeg
from bpos import BPos
from oneg import ONeg
from opos import OPos

# Used to check user input
yes_list = ("Y", "y", "YES", "YEs", "Yes", "yes", "yeS", "yES")
no_list = ("N", "n", "NO", "No", "no", "nO")

# Creates sets of compatible blood types for each blood type
# Can be used to check what type a recipient can receive, not sure if it will be used
oneg_recipient = {abs(hash("oneg"))}
opos_recipient = {abs(hash("oneg")), abs(hash("opos"))}
aneg_recipient = {abs(hash("oneg")), abs(hash("aneg"))}
apos_recipient = {abs(hash("oneg")), abs(hash("opos")), abs(hash("aneg")), abs(hash("apos"))}
bneg_recipient = {abs(hash("oneg")), abs(hash("bneg"))}
bpos_recipient = {abs(hash("oneg")), abs(hash("opos")), abs(hash("bneg")), abs(hash("bpos"))}
abneg_recipient = {abs(hash("oneg")), abs(hash("aneg")), abs(hash("bneg")), abs(hash("abneg"))}
abpos_recipient = {abs(hash("oneg")), abs(hash("opos")), abs(hash("aneg")), abs(hash("apos")), abs(hash("bneg")),
                   abs(hash("bpos")), abs(hash("abneg")), abs(hash("abpos"))}

types = ["oneg", "opos", "aneg", "apos", "bneg", "bpos", "abneg", "abpos"]

# Creates a list of the blood type hashes, used to access the blood type dictionary
types_hashed = [abs(hash(types[j])) for j in range(len(types))]
# Creates a dictionary of the blood type hashes and the blood type queues
pods_hashed = {abs(hash(types[j])): queue.Queue(maxsize=100) for j in range(len(types))}

# This list will be used to store all the id nums for all blood types and will be used to check for collisions
id_list = []

# https://www.pythonprogramming.in/how-to-get-the-last-sunday-and-saturday-date-in-python.html
# https://www.justintodata.com/manipulate-date-and-time-in-python/
# Sets the program period to start at the Sunday of the current week
program_period = (datetime.now() - timedelta(days=((datetime.now().isoweekday()) % 7))).date()

# https://www.pythonpool.com/python-clear-memory/
# deletes the types list and collects the garbage to manage memory
del types
gc.collect()


# All of these are used to make the program "pretty"
def small_sep():
    print("---------------------------------------------------")


def small_space_sep():
    print()
    print("---------------------------------------------------")
    print()


def large_sep():
    print("===================================================")


def large_space_sep():
    print()
    print("===================================================")
    print()


def header():
    print()
    print()
    large_sep()
    print("Welcome to the Best Blood Bank's Management Program")
    large_sep()
    print()


def main_menu():
    print("What would you like to do?")
    print()
    print("     1 Add a Blood Bag")
    print("     2 Check Out a Blood Bag")
    print("     3 Move to the Next Period")
    print("     4 Exit the Program")
    print()
    user_input = input("Enter menu option (1-4): ")
    while user_input not in ["1", "2", "3", "4"]:
        user_input = input("Invalid choice. Choose menu option (1-4): ")
    large_space_sep()
    return user_input


# Generates 10 bags for each blood type if the queue isn't full of 100 bags
def generate_bags():

    # Creating 10 bags for each blood type
    for _ in range(10):
        # https://blog.finxter.com/how-to-generate-a-random-date-between-two-dates/
        # start_date = program_period - timedelta(days=10)
        # end_date = program_period
        # Was using this, but just generated on program period to make queue simpler and not have to sort
        # random_date = start_date + (end_date - start_date) * random()

        # Creating ONeg bags if there are less than 100
        if pods_hashed[types_hashed[0]].full() is False:
            # Create a blood bag object
            bag = ONeg(program_period, ("".join(choice(string.ascii_lowercase) for _ in range(10))))
            # Add the blood bag object's id num to the list
            id_list.append(bag.id_num)
            # Add the blood bag object to the queue
            pods_hashed[types_hashed[0]].put(bag)

        # Creating OPos bags if there are less than 100
        if pods_hashed[types_hashed[1]].full() is False:
            # Create a blood bag object
            bag = OPos(program_period, ("".join(choice(string.ascii_lowercase) for _ in range(10))))
            # Add the blood bag object's id num to the list
            id_list.append(bag.id_num)
            # Add the blood bag object to the queue
            pods_hashed[types_hashed[1]].put(bag)

        # Creating ANeg bags if there are less than 100
        if pods_hashed[types_hashed[2]].full() is False:
            # Create a blood bag object
            bag = ANeg(program_period, ("".join(choice(string.ascii_lowercase) for _ in range(10))))
            # Add the blood bag object's id num to the list
            id_list.append(bag.id_num)
            # Add the blood bag object to the queue
            pods_hashed[types_hashed[2]].put(bag)

        # Creating APos bags if there are less than 100
        if pods_hashed[types_hashed[3]].full() is False:
            # Create a blood bag object
            bag = APos(program_period, ("".join(choice(string.ascii_lowercase) for _ in range(10))))
            # Add the blood bag object's id num to the list
            id_list.append(bag.id_num)
            # Add the blood bag object to the queue
            pods_hashed[types_hashed[3]].put(bag)

        # Creating BNeg bags if there are less than 100
        if pods_hashed[types_hashed[4]].full() is False:
            # Create a blood bag object
            bag = BNeg(program_period, ("".join(choice(string.ascii_lowercase) for _ in range(10))))
            # Add the blood bag object's id num to the list
            id_list.append(bag.id_num)
            # Add the blood bag object to the queue
            pods_hashed[types_hashed[4]].put(bag)

        # Creating BPos bags if there are less than 100
        if pods_hashed[types_hashed[5]].full() is False:
            # Create a blood bag object
            bag = BPos(program_period, ("".join(choice(string.ascii_lowercase) for _ in range(10))))
            # Add the blood bag object's id num to the list
            id_list.append(bag.id_num)
            # Add the blood bag object to the queue
            pods_hashed[types_hashed[5]].put(bag)

        # Creating ABNeg bags if there are less than 100
        if pods_hashed[types_hashed[6]].full() is False:
            # Create a blood bag object
            bag = ABNeg(program_period, ("".join(choice(string.ascii_lowercase) for _ in range(10))))
            # Add the blood bag object's id num to the list
            id_list.append(bag.id_num)
            # Add the blood bag object to the queue
            pods_hashed[types_hashed[6]].put(bag)

        # Creating ABPos bags if there are less than 100
        if pods_hashed[types_hashed[7]].full() is False:
            # Create a blood bag object
            bag = ABPos(program_period, ("".join(choice(string.ascii_lowercase) for _ in range(10))))
            # Add the blood bag object's id num to the list
            id_list.append(bag.id_num)
            # Add the blood bag object to the queue
            pods_hashed[types_hashed[7]].put(bag)


# Checks for collisions of the id nums for the blood bags
def check_collisions():
    # Creates a set for the id nums
    collision_set = set()

    # Loops through the blood bags id num list
    for check_id in id_list:
        # Checks if the id num is in the set
        if check_id in collision_set:
            # Prints the id num to the collisions file
            with open("collisions_file.txt", "a") as col_file:
                col_file.write(f"{check_id} Had a Collision!\n")
        # Adds the id num to the set if not already in it
        else:
            collision_set.add(check_id)

    # deletes the set
    del collision_set
    gc.collect()


# Checks for expired blood bags
def check_for_expired():

    # Loops through the ONeg queue
    while True:
        # Checks if the blood bag object's expiration date is less than the current date
        if pods_hashed[types_hashed[0]].queue[0].exp_date < program_period:
            # Removes the blood bag object from the queue
            pods_hashed[types_hashed[0]].get()
            # Check the first blood bag object in the queue again
            continue
        # Since the queue is sorted by FIFO, if the blood bag object's expiration date is greater than the current date, then break
        else:
            break

    # Loops through the OPos queue
    while True:
        # Checks if the blood bag object's expiration date is less than the current date
        if pods_hashed[types_hashed[1]].queue[0].exp_date < program_period:
            # Removes the blood bag object from the queue
            pods_hashed[types_hashed[1]].get()
            # Check the first blood bag object in the queue again
            continue
        # Since the queue is sorted by FIFO, if the blood bag object's expiration date is greater than the current date, then break
        else:
            break

    # Loops through the ANeg queue
    while True:
        # Checks if the blood bag object's expiration date is less than the current date
        if pods_hashed[types_hashed[2]].queue[0].exp_date < program_period:
            # Removes the blood bag object from the queue
            pods_hashed[types_hashed[2]].get()
            # Check the first blood bag object in the queue again
            continue
        # Since the queue is sorted by FIFO, if the blood bag object's expiration date is greater than the current date, then break
        else:
            break

    # Loops through the APos queue
    while True:
        # Checks if the blood bag object's expiration date is less than the current date
        if pods_hashed[types_hashed[3]].queue[0].exp_date < program_period:
            # Removes the blood bag object from the queue
            pods_hashed[types_hashed[3]].get()
            # Check the first blood bag object in the queue again
            continue
        # Since the queue is sorted by FIFO, if the blood bag object's expiration date is greater than the current date, then break
        else:
            break

    # Loops through the BNeg queue
    while True:
        # Checks if the blood bag object's expiration date is less than the current date
        if pods_hashed[types_hashed[4]].queue[0].exp_date < program_period:
            # Removes the blood bag object from the queue
            pods_hashed[types_hashed[4]].get()
            # Check the first blood bag object in the queue again
            continue
        # Since the queue is sorted by FIFO, if the blood bag object's expiration date is greater than the current date, then break
        else:
            break

    # Loops through the BPos queue
    while True:
        # Checks if the blood bag object's expiration date is less than the current date
        if pods_hashed[types_hashed[5]].queue[0].exp_date < program_period:
            # Removes the blood bag object from the queue
            pods_hashed[types_hashed[5]].get()
            # Check the first blood bag object in the queue again
            continue
        # Since the queue is sorted by FIFO, if the blood bag object's expiration date is greater than the current date, then break
        else:
            break

    # Loops through the ABNeg queue
    while True:
        # Checks if the blood bag object's expiration date is less than the current date
        if pods_hashed[types_hashed[6]].queue[0].exp_date < program_period:
            # Removes the blood bag object from the queue
            pods_hashed[types_hashed[6]].get()
            # Check the first blood bag object in the queue again
            continue
        # Since the queue is sorted by FIFO, if the blood bag object's expiration date is greater than the current date, then break
        else:
            break

    # Loops through the ABPos queue
    while True:
        # Checks if the blood bag object's expiration date is less than the current date
        if pods_hashed[types_hashed[7]].queue[0].exp_date < program_period:
            # Removes the blood bag object from the queue
            pods_hashed[types_hashed[7]].get()
            # Check the first blood bag object in the queue again
            continue
        # Since the queue is sorted by FIFO, if the blood bag object's expiration date is greater than the current date, then break
        else:
            break


# Simulates the use of a random number of bags
def sim_use_bags():

    # Loops based on a random number, 1-10 to remove that many bags from each queue
    for _ in range(randint(1, 10)):
        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[0]].get()

        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[1]].get()

        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[2]].get()

        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[3]].get()

        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[4]].get()

        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[5]].get()

        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[6]].get()

        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[7]].get()


# User inputs the blood type and donor's name to add the bag to the queue
def user_add_bag():
    input_type = input("What is the blood type?: ")
    while abs(hash(input_type)) not in types_hashed:
        input_type = input("Invalid type. Please enter a valid blood type: ")
    # input_draw_date = input("What is the draw date? (YYYY/MM/DD): ")
    input_donor_name = input("What is the donor's name: ")
    # input_draw_date = datetime.strptime(input_draw_date, '%Y/%m/%d').date()
    # Using this instead once again to simplify the queue and not have to sort it

    if abs(hash(input_type)) == types_hashed[0]:
        # Create a blood bag object
        bag = ONeg(program_period, input_donor_name)
        # Add the blood bag object's id num to the list
        id_list.append(bag.id_num)
        # Add the blood bag object to the queue
        pods_hashed[types_hashed[0]].put(bag)

    elif abs(hash(input_type)) == types_hashed[1]:
        # Create a blood bag object
        bag = OPos(program_period, input_donor_name)
        # Add the blood bag object's id num to the list
        id_list.append(bag.id_num)
        # Add the blood bag object to the queue
        pods_hashed[types_hashed[1]].put(bag)

    elif abs(hash(input_type)) == types_hashed[2]:
        # Create a blood bag object
        bag = ANeg(program_period, input_donor_name)
        # Add the blood bag object's id num to the list
        id_list.append(bag.id_num)
        # Add the blood bag object to the queue
        pods_hashed[types_hashed[2]].put(bag)

    elif abs(hash(input_type)) == types_hashed[3]:
        # Create a blood bag object
        bag = APos(program_period, input_donor_name)
        # Add the blood bag object's id num to the list
        id_list.append(bag.id_num)
        # Add the blood bag object to the queue
        pods_hashed[types_hashed[3]].put(bag)

    elif abs(hash(input_type)) == types_hashed[4]:
        # Create a blood bag object
        bag = BNeg(program_period, input_donor_name)
        # Add the blood bag object's id num to the list
        id_list.append(bag.id_num)
        # Add the blood bag object to the queue
        pods_hashed[types_hashed[4]].put(bag)

    elif abs(hash(input_type)) == types_hashed[5]:
        # Create a blood bag object
        bag = BPos(program_period, input_donor_name)
        # Add the blood bag object's id num to the list
        id_list.append(bag.id_num)
        # Add the blood bag object to the queue
        pods_hashed[types_hashed[5]].put(bag)

    elif abs(hash(input_type)) == types_hashed[6]:
        # Create a blood bag object
        bag = ABNeg(program_period, input_donor_name)
        # Add the blood bag object's id num to the list
        id_list.append(bag.id_num)
        # Add the blood bag object to the queue
        pods_hashed[types_hashed[6]].put(bag)

    elif abs(hash(input_type)) == types_hashed[7]:
        # Create a blood bag object
        bag = ABPos(program_period, input_donor_name)
        # Add the blood bag object's id num to the list
        id_list.append(bag.id_num)
        # Add the blood bag object to the queue
        pods_hashed[types_hashed[7]].put(bag)

    print()
    print("Your bag has been added.")
    large_space_sep()


# User inputs the blood type and a bag of that type is removed from the queue
def user_remove_bag():
    input_type = input("What is the blood type?: ")
    while abs(hash(input_type)) not in types_hashed:
        input_type = input("Invalid type. Please enter a valid blood type: ")

    if abs(hash(input_type)) == types_hashed[0]:
        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[0]].get()

    elif abs(hash(input_type)) == types_hashed[1]:
        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[1]].get()

    elif abs(hash(input_type)) == types_hashed[2]:
        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[2]].get()

    elif abs(hash(input_type)) == types_hashed[3]:
        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[3]].get()

    elif abs(hash(input_type)) == types_hashed[4]:
        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[4]].get()

    elif abs(hash(input_type)) == types_hashed[5]:
        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[5]].get()

    elif abs(hash(input_type)) == types_hashed[6]:
        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[6]].get()

    elif abs(hash(input_type)) == types_hashed[7]:
        # Removes the first blood bag object from the queue
        pods_hashed[types_hashed[7]].get()

    print()
    print("Your bag has been removed.")
    large_space_sep()


if __name__ == '__main__':

    run_program = True

    header()

    # Continues running the program week-by-week
    while run_program:
        # Make sure removed bags are being collected
        gc.collect()

        # Display the program's current period
        small_sep()
        print(f"Current Period: {program_period} - {program_period + timedelta(days=6)}")
        small_sep()
        print()

        # Generate 10 bags per blood type
        generate_bags()

        # Check for collisions
        check_collisions()

        # Check for expired bags in each blood type queue
        check_for_expired()

        # Simulate the use of a range from 1-10 bags for all blood types
        sim_use_bags()

        # Allows the user to use the menu options during the week
        while run_program:

            # Display the menu and receive user's input
            option = main_menu()

            if option == "1":
                # User will add a bag to a blood type
                user_add_bag()
            elif option == "2":
                # User will check out a bag from a blood type
                user_remove_bag()
            elif option == "3":
                # Advance one week and break from this week's loop
                program_period += timedelta(weeks=1)
                break
            elif option == "4":
                # Exit the program
                run_program = False

    print("Hope to see you again soon!")
