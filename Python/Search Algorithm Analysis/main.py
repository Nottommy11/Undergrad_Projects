from operator import itemgetter
from time import perf_counter_ns, sleep

import file_io


def main():
    # Get the values from the file
    rows = file_io.load_pokemon()

    # Search 100 times using linear and binary search algorithms
    for search in range(1, 101):
        linear_search(rows, search)
        binary_search(rows, search)

        print()
        print("Sleeping...")
        print()
        sleep(2)


# Linear search for the count of "Poison" types
def linear_search(rows, num_search):

    print(f"Starting linear problem solution: {num_search}")

    # Number of occurrences of Poison
    counter = 0

    # Get the time before the start of the search
    start_time = perf_counter_ns()

    # Search each row/dictionary item
    for row in rows:
        # Loop through each key / value pair
        for key, value in row.items():
            # If the key is a "Type" field, check if the value is Poison and add the occurrence
            if "Type" in key:
                if value == "Poison":
                    counter += 1

    # Get the time after the search
    stop_time = perf_counter_ns()

    # Display the time it took to complete the search
    print(f"Time taken: {stop_time - start_time} nanoseconds")
    print(f"Frequency of Poison found: {counter}")


# Binary search for each occurrence of the maximum total
def binary_search(rows, num_search):

    # Create a new dictionary to store the max total Pokemon
    max_dict = {}

    print(f"Starting binary problem solution: {num_search}")

    # Get the time before the start of the search
    start_time = perf_counter_ns()

    # https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
    # Sort the list by the values in the total
    new_rows = sorted(rows, key=itemgetter("Total"))

    # The last item in the list should be the maximum total
    max_total = new_rows[-1].get("Total")

    # The last item's position
    max_end = len(new_rows)

    # Get the first occurrence of that maximum total
    max_start = search_max(new_rows, 0, len(new_rows) - 1, max_total, True) - 1

    # Loop from the first occurrence to the last occurrence
    for row in range(max_start, max_end):
        # Add the Name and Total to the dictionary
        max_dict.update({new_rows[row].get("Name"): new_rows[row].get("Total")})

    # Get the time after the search
    stop_time = perf_counter_ns()

    # Display the time it took to complete the search
    print(f"Time taken: {stop_time - start_time} nanoseconds")
    print(f"Key / Value Maximums: {max_dict}")


# Find the first occurrence of the maximum total
def search_max(rows, low, high, max_total, first_search):
    if high >= low:
        # Find the middle of the list
        mid = (high + low) // 2
        if rows[mid].get("Total") == max_total:
            # If the total of the item equals the max, and it's the first search, set the high as the mid - 1
            if first_search:
                return search_max(rows, low, mid - 1, max_total, False)
            # Otherwise return the position
            else:
                return mid
        # Continue to split the search until a match is found
        elif rows[mid].get("Total") > max_total:
            return search_max(rows, low, mid - 1, max_total, False)
        else:
            return search_max(rows, mid + 1, high, max_total, False)
    else:
        return -1


if __name__ == '__main__':
    main()
