import csv

# Set the filename
filename = "planets.csv"
# List used to store the dictionary
rows = []


# Loads planets into a list of dictionaries from a csv file
def load_planets():
    # Open the file
    with open(filename) as planet_csv:
        # Set a variable as the reader
        csv_read = csv.DictReader(planet_csv)

        # Read each row and add it to the list
        for row in csv_read:
            rows.append(row)

    return rows
