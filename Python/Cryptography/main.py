# Check out ord function: Returns ASCII Value
# Seed random to the key
import sys

import caesar_cipher


def main():
    caesar_cipher.create_list()
    caesar_cipher.rotate_string(False)
    caesar_cipher.rotate_string(True)
    caesar_cipher.check_list()
    caesar_cipher.disp_changes()
    print("Thank you, come again!")


if __name__ == "__main__":
    sys.exit(main())
