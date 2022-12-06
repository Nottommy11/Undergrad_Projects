import itertools
from time import process_time_ns


# https://medium.com/@ben.nour_68691/cracking-a-virtual-4-digit-combination-lock-using-python-d0d186712eed
# Uses itertools to generate all possible permutations of the hash
def my_attempt(correct_hash):
    # https://www.geeksforgeeks.org/time-process_time-function-in-python/
    # Get the start time in nanoseconds
    start = process_time_ns()
    # Creates a list of the possible digits in each position
    digits = list(range(0, 10))
    # Generates all possible permutations of the hash
    for permutation in itertools.product(digits, repeat=len(correct_hash)):
        # Creates a list of the current permutation
        permutation_list = [str(digit) for digit in permutation]
        # Joins the list into a string
        permutation = "".join(permutation_list)
        # Checks if the current permutation is the correct hash
        if int(permutation) == int(correct_hash):
            # Get the end time in nanoseconds
            end = process_time_ns()
            # Display the correct permutation
            print(f"Cryptex unlocked: {permutation}")
            # Display the time it took to crack the hash in seconds
            # Nanoseconds to seconds = nanoseconds / 1,000,000,000
            print(f"Actual decrypt time: {(end - start) / 1_000_000_000}")
            return permutation
