import csv

# Set the filename
filename = "Pokemon_numerical.csv"
# List used to store the dictionary
rows = []


# Loads Pokemon into a list of dictionaries from a csv file
def load_pokemon():
    # Open the file
    with open(filename) as pokemon_csv:
        # Set a variable as the reader
        csv_read = csv.DictReader(pokemon_csv)

        # Read each row and add it to the list
        for row in csv_read:
            rows.append(row)

    return rows
