from time import perf_counter_ns

import file_io


"""
https://www.baeldung.com/cs/time-vs-space-complexity

The Insertion Sort took fewer steps and it's average completion time was almost half of the Selection Sort.
They both sorted the data effectively.


Selection Sort:
Time Complexity (Best): O(n^2)
Has to loop through list for each element
Space Complexity: O(1)
Only changes by the element added


Insertion Sort:
Time Complexity (Best): O(n)
Doesn't have to loop through list for each element
Space Complexity: O(1)
Only changes by the element added
"""

selection_time = []
insertion_time = []


def main():
    # Get the values from the file
    planets = file_io.load_planets()

    unsorted_mass = []

    # Populate the list with the Mass values from the planets
    for planet in planets:
        unsorted_mass.append(float(planet.get("Mass (10^24kg)")))

    print()

    # Search 100 times using linear and binary search algorithms
    for sort in range(1, 101):
        selection_sort(unsorted_mass, sort)

        print()
        print("------------------------------------------")
        print()

        insertion_sort(unsorted_mass, sort)

        print()
        print("==========================================")
        print()

    selection_average = 0
    insertion_average = 0

    # Add the time taken for each sort together
    for element in range(len(selection_time)):
        selection_average += selection_time[element]
        insertion_average += insertion_time[element]

    # Print the average by dividing the total by number of sorts
    print(f"Selection Sort Average: {selection_average / len(selection_time)}")
    print(f"Insertion Sort Average: {insertion_average / len(insertion_time)}")


def selection_sort(unsorted_mass, sort):
    # Create a copy to retain clean original data
    sorted_mass = unsorted_mass.copy()
    steps = 0

    print("Original Mass Data:")
    print(sorted_mass)
    print(f"Starting Selection Sort: Pass {sort}")

    # Get the time before the start of the sort
    start_time = perf_counter_ns()

    # https://www.programiz.com/dsa/selection-sort
    # Loop through the list
    for index in range(len(sorted_mass)):
        # Initially set the minimum to the current index
        min_index = index

        # Loop through the list starting at the next index
        for element in range(index + 1, len(sorted_mass)):
            # If the current element is less than the minimum, set the minimum to this element
            if sorted_mass[element] < sorted_mass[min_index]:
                min_index = element
        # The sort algorithm completed a step
        steps += 1
        # Swap the current index with the minimum
        (sorted_mass[index], sorted_mass[min_index]) = (sorted_mass[min_index], sorted_mass[index])

    # Get the time after the sort
    stop_time = perf_counter_ns()

    # Add the time of the sort to the list
    selection_time.append(stop_time - start_time)

    print()
    print("Selection Sort Data:")
    print(sorted_mass)
    print(f"Time Taken: {stop_time - start_time} nanoseconds")
    print(f"Steps Taken: {steps}")


def insertion_sort(unsorted_mass, sort):
    # Create a copy to retain clean original data
    sorted_mass = unsorted_mass.copy()
    steps = 0

    print("Original Mass Data:")
    print(sorted_mass)
    print(f"Starting Insertion Sort: Pass {sort}")

    # Get the time before the start of the search
    start_time = perf_counter_ns()

    # https://www.programiz.com/dsa/insertion-sort
    # Loop through the list
    for index in range(1, len(sorted_mass)):

        # Set the key as the current element
        key = sorted_mass[index]
        element = index - 1

        # Compare the element with the element to the left until a smaller element is found
        while element >= 0 and key < sorted_mass[element]:
            sorted_mass[element + 1] = sorted_mass[element]
            element -= 1
        steps += 1
        sorted_mass[element + 1] = key

    # Get the time after the search
    stop_time = perf_counter_ns()

    # Add the time of the sort to the list
    insertion_time.append(stop_time - start_time)

    print()
    print("Insertion Sort Data:")
    print(sorted_mass)
    print(f"Time Taken: {stop_time - start_time} nanoseconds")
    print(f"Steps Taken: {steps}")


if __name__ == '__main__':
    main()
