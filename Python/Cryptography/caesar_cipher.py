import string
import random
import sys
from datetime import time

# Seed random with time in microseconds
random.seed(time.microsecond)
# Create original list
orig_list = []
# Create encrypted list
encrypted_list = []
# Created decrypted list
decrypted_list = []
# Characters will be shifting left (0) or right (1)
shift = random.randint(0, 1)
# How far characters will be shifted
shift_value = random.randint(1, 10)


# Make program look pretty
def large_spacer():
    print()
    print("============================================")
    print()


# Make program look pretty
def small_spacer():
    print()
    print("--------------------------------------------")
    print()


# Create the strings in the list
def create_list():
    # Creates 50 string elements
    for x in range(50):
        # Creates a string of 7 characters in length with uppercase and lowercase letters and digits
        orig_list.append("".join(random.choice(string.ascii_letters + string.digits) for y in range(7)))
        # Copy the list as the encrypted list will begin the encryption process
        encrypted_list.append(orig_list[x])
    large_spacer()
    print(f"List Created:   {orig_list}")


# Will rotate all the characters in a string
def rotate_string(decrypt):
    # If the list is to be decrypted, switch shift direction accordingly
    if decrypt is True:
        if shift == 1:
            shift_side = 0
        else:
            shift_side = 1
    # Otherwise it is being encrypted
    else:
        shift_side = shift

    # Check which direction the characters will be shifted, this being left
    if shift_side == 0:
        # Each element in the list
        for element in range(len(encrypted_list)):
            new_string = ""
            # Each character in the string
            for char in encrypted_list[element]:
                # Get the local ASCII value
                local_value = convert_to_local(char)
                # Get the rotated value of the character
                char_value = rotate_value(local_value, shift_side)
                # Add the character to a new string
                new_string += char_value
            # If the list is being decrypted, add the string to the list
            if decrypt is True:
                decrypted_list.append(new_string)
            # If the list is being encrypted, set the new string to the element
            else:
                encrypted_list[element] = new_string

    # Check which direction the characters will be shifted, this being right
    elif shift_side == 1:
        # Each element in the list
        for element in range(len(orig_list)):
            new_string = ""
            # Each character in the string
            for char in encrypted_list[element]:
                # Get the local ASCII value
                local_value = convert_to_local(char)
                # Get the rotated value of the character
                char_value = rotate_value(local_value, shift_side)
                # Add the character to a new string
                new_string += char_value
            # If the list is being decrypted, add the string to the list
            if decrypt is True:
                decrypted_list.append(new_string)
            # If the list is being encrypted, set the new string to the element
            else:
                encrypted_list[element] = new_string


# Converts ASCII values to local values
# 1-10 is digits
# 11-36 is lowercase letters
# 37-62 is uppercase letters
def convert_to_local(char):
    # Gets the ASCII value of the character
    ascii_value = ord(char)
    # Check if the character is an uppercase letter
    if char.isupper():
        # Uppercase A starts at 65, so this starts A at 11
        local_value = 10 + (ascii_value - 64)
    # Check if the character is a lowercase letter
    elif char.islower():
        # Lowercase a starts at 97, so this starts a at 37
        local_value = 36 + (ascii_value - 96)
    # Otherwise it is a digit
    else:
        # Number 0 starts at 48, so this starts 0 at 1
        local_value = ascii_value - 47
    # print(f"{ascii_value}: {char} was converted to {local_value}")
    return local_value


# This changes the character by the amount it should be shifted and the direction
# It will also return the character by converting the local value to the ASCII value
def rotate_value(local_value, shift_side):
    # If being shifted left
    if shift_side == 0:
        # Shift the character value
        temp_value = local_value - shift_value
        # If it goes below 1, will need to start back at the top
        if temp_value < 1:
            # Adding a negative value
            # Anything below one starts subtracting from 62
            temp_value = 62 + temp_value
    # If being shifted right
    else:
        # Shift the character value
        temp_value = local_value + shift_value
        # If above 62, will need to start back at the bottom
        if temp_value > 62:
            # Anything above 62 starts at 0
            temp_value = temp_value - 62
    # print(f"{local_value} was rotated to {temp_value}")
    # If the value is a digit
    if 1 <= temp_value <= 10:
        # Find the ASCII value by starting at ASCII value for 0 and adding the local value
        rotated_value = 47 + temp_value
    # If the value is an uppercase letter
    elif 11 <= temp_value <= 36:
        # Find the ASCII value by starting at ASCII value for A and adding the local value
        rotated_value = 64 + (temp_value - 10)
    # If the value is a lowercase letter
    else:
        # Find the ASCII value by starting at ASCII value for a and adding the local value
        rotated_value = 96 + (temp_value - 36)
    # Return the character of the ASCII value
    return chr(rotated_value)


# Display each changed string of the list
def disp_changes():
    large_spacer()
    print("Displaying changes...")
    # For each element in the list
    for x in range(len(orig_list)):
        if shift == 0:
            shift_dir = "Left"
        else:
            shift_dir = "Right"
        small_spacer()
        print(f"Original String:   {orig_list[x]}")
        print(f"Shift Direction:   {shift_dir}")
        print(f"Shift Value:       {shift_value}")
        print(f"Encrypted Text:    {encrypted_list[x]}")
    large_spacer()


# Checks that the list was successfully encrypted and decrypted, so checks if the encryption process is working
def check_list():
    large_spacer()
    print("Checking your lists...")
    small_spacer()
    # Used to check if the encryption failed
    encryption_failed = False
    # For each element in the list
    for x in range(len(orig_list)):
        # Check if each string is the same
        if orig_list[x] == decrypted_list[x]:
            # Check next element
            pass
        # Check if the strings don't match
        elif orig_list[x] != decrypted_list[x]:
            encryption_failed = True
            small_spacer()
            print(f"Failed at:        {x}")
            print(f"Original String:  {orig_list[x]}")
            print(f"Decrypted string: {decrypted_list[x]}")
        # Shouldn't even be able to get here, but just in case
        else:
            print("What???")

    # Let the user know that the encryption process was successful
    if encryption_failed is False:
        print("The encryption was Successful.")
        print(f"Encrypted List:   {encrypted_list}")
        print(f"Original List:    {orig_list}")
        print(f"Decrypted List:   {decrypted_list}")

    # Let the user know that the encryption process failed
    elif encryption_failed is True:
        print("The encryption failed.")
        print(f"Encrypted List:   {encrypted_list}")
        print(f"Original List:    {orig_list}")
        print(f"Decrypted List:   {decrypted_list}")

        # Exit the program so the user knows that the encryption failed
        small_spacer()
        print("Exiting the program now.")
        return sys.exit(1)
