"""

TODO:

[X]     Get a random Leonardo da Vinci quote
[X]     Hash the quote
[X]     Doubly Linked List Stack
[X]     Attempt to crack the hash with itertools

OPTIONAL:
[ ]     Attempt to crack the hash with other python libraries
[X]     Use thread pool to enhance permutations

"""
from multiprocessing import Pool

from crack_hash import my_attempt
from dll_stack import Stack
from quote import get_quote


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


if __name__ == '__main__':
    # Get a random quote from Leonardo da Vinci
    quote = get_quote()
    # Hash the quote
    quote_hashed = abs(hash(quote))
    # Create a stack to hold the hashed quote
    quote_stack = Stack()

    # Used to display the current test
    test = 1

    # Loop from 6 to 19 stepping by 2
    # Probably won't even reach 19, so it doesn't matter that it wouldn't even make it there
    for i in range(6, 19, 2):
        # Enumerates through hash of the quote and adds each character to the stack
        for _, num in enumerate(str(quote_hashed)):
            quote_stack.push(num)

        print("\n")
        large_sep()
        print(f"<~~~~~~~~~~~~~~~~~~> Output #{test} <~~~~~~~~~~~~~~~~~~>")
        large_sep()
        print()

        print(f"Testing with quote:\n  \"{quote}\"")
        print()
        print(f"Here is the hash:\n  {quote_hashed}")
        print()

        # Displays the stack, which is basically the hash of the quote reversed
        print("=======================.....=======================")
        quote_stack.print_stack()
        print(f"Attempting to unlock the first {i} digits!")
        print("=======================.....=======================")
        print()

        # Pop the number of digits that will be tested off the stack into the correct hash
        correct_hash = ""
        for _ in range(i):
            correct_hash += quote_stack.pop()

        # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.apply_async
        # Creates a pool utilizing all available cores
        my_pool = Pool()
        # Calls the my_attempt function passing correct_hash as the argument
        # Starts the thread pool
        my_pool.apply_async(my_attempt, args=(correct_hash,))

        # Waits for the pool to complete and shuts down the pool
        my_pool.close()
        my_pool.join()
        # Added this just in case
        del my_pool

        # Remove the rest of the elements from the stack
        while quote_stack.pop():
            pass
        # Increment the test number
        test += 1
