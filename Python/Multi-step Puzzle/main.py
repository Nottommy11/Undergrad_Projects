from queue import Queue


# Hash based on two given values
def h(k, m):
    # Returns the remainder of k divided by m
    return k % m


# Checks for collisions of the hashes
def check_collisions(check_list):
    # Creates a set for the hashes
    collision_set = set()
    collision_counter = 0

    # Loops through the hash list
    for check_id in check_list:
        # Checks if the hash is in the set
        if check_id in collision_set:
            # Adds to the collision counter
            collision_counter += 1
        # Adds the hash to the set if not already in it
        else:
            collision_set.add(check_id)

    return collision_counter


# Removes consecutive characters in a string using two stacks. The stacks are made with lists
def remove_dupes(input_stack):

    # The stack without any consecutive characters
    good_stack = []

    # Pop the first element to the temp1 variable
    temp1 = input_stack.pop()

    # Pop the second element to the temp2 variable
    temp2 = input_stack.pop()

    while True:

        # Shift temp2 to temp1 and pop the next element to temp2
        # Basically shifting elements and getting rid of the consecutive character that was in temp1
        if temp1 == temp2:
            temp1 = temp2
            temp2 = input_stack.pop()

        # Replace the consecutive character that temp2 matched with in the stack and continue the loop
        elif temp2 == input_stack[-1]:
            input_stack.pop()
            temp2 = input_stack.pop()

        # Add the non-consecutive character to the good stack and shift the remaining characters and continue the loop
        else:
            good_stack.append(temp1)
            temp1 = temp2
            temp2 = input_stack.pop()

        # Break the loop when the stack is empty and add the last character to the good stack
        if len(input_stack) == 0:
            good_stack.append(temp2)
            break

    return good_stack


if __name__ == '__main__':

    print("Starting with the famous Hitchhiker's Guide to the Galaxy quote: What is the meaning of life?")

    """
    NUMBER 1
    """

    print("Starting problem solution #1")

    start_string = "What is the meaning of life?"

    # Create a list of the string separated by spaces
    split_string = start_string.split(" ")

    # The length of the 3rd word is used for the first input
    first_input = len(split_string[2])
    # The length of the 4th word minus the 5th word is used for the second input
    second_input = len(split_string[3]) - len(split_string[4])

    print(f"Output of problem #1 is: ({first_input}, {second_input}) ")

    """
    NUMBER 2
    """

    print("Starting problem solution #2")

    # Create a set of the multiples of the first input up to 1000
    first_set = set(n for n in range(first_input, 1000, first_input))
    # Create a set of the multiples of the second input up to 1000
    second_set = set(n for n in range(second_input, 1000, second_input))

    # Create a set of the second set with all elements from the first set removed
    rem_dupes = second_set - first_set

    # Create lists from the sets and get the sum of all of the elements
    total_sum = sum(list(first_set) + list(rem_dupes))

    print(f"Output for problem #2: {total_sum}")

    """
    NUMBER 3
    """

    print("Starting problem solution #3")

    # I think I did this backwards from how you expected it to be done
    queue3 = Queue()

    # Add each character in the total_sum as a string to the queue
    for _, num in enumerate(str(total_sum)):
        queue3.put(num)

    # Get the product of the first 2 elements in the queue
    queue_prod = int(queue3.get()) * int(queue3.get())

    # Get the sum of the next 2 elements in the queue
    queue_sum = int(queue3.get()) + int(queue3.get())

    # Get the average of the sum and product
    average = (int(queue_sum) + int(queue_prod)) / 2

    # Discard last 2 elements
    queue3.get()
    queue3.get()

    print(f"Output of problem #3 is: {average}")

    """
    NUMBER 4
    """

    print("Starting problem solution #4")

    raw_list = [3, 2, 9, 11, 7, 8, 13, 17]
    hash_list = []

    # Hash each element in the list and add it to the hash list
    for i in raw_list:
        hash_list.append(h(i, int(average)))

    # Pass the hash list to get the number of collisions
    num_collisions = check_collisions(hash_list)

    print(f"Output of problem #4 is: {num_collisions}")

    """
    NUMBER 5
    """

    print("Starting problem solution #5")

    # Create the dictionary with the key and values being the square of the key
    dict1 = {x: x * x for x in range(1, num_collisions + 1)}

    # Update the key 4 with the product of key 2 and key 3 plus key 4
    dict1.update({4: dict1.get(4) + (dict1.get(2) * dict1.get(3))})

    print(f"Output of problem #5 is: {dict1.get(4)}")

    """
    NUMBER 6
    """

    print("Starting problem solution #6")

    given_string = "cabbage"

    raw_stack = []

    char_sum = 0

    # Add each character in the string to the stack
    for _, char in enumerate(given_string):
        raw_stack.append(char)

    # Remove the consecutive characters in the stack
    clean_stack = remove_dupes(raw_stack)

    # Get the sum of the ASCII values of the characters in the stack
    for char in clean_stack:
        char_sum += ord(char)

    print(f"Output of problem #6 is: {char_sum}")

    """
    COMPLETION
    """

    char_list = []

    # Add each character in the string to the list
    for _, num in enumerate(str(char_sum)):
        char_list.append(int(num))

    # Get the difference between the sum of the char list and 4
    final_answer = dict1.get(4) - (sum(char_list) + 4)

    print("Finally, our mouse trap reaches the end")
    print(f"{start_string} {final_answer}")
