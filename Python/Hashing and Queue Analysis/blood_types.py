from datetime import timedelta


# Create the hash id for the bag
# I have simulated over 10 years with no collisions using this hashing function
# Uses the ASCII values of each character to create a unique hash
# A person can only donate one bag on a given day, so the hash can't be duplicated.
# If they donate again, the date will be different and the hash will be different
def hash_bag(donor_name, draw_date):
    # bag_hash = hash(donor_name + str(draw_date))
    bag_hash = "#"
    for _, character in enumerate(str(donor_name)):
        # Adds the ASCII value of each character to the hash as a string
        bag_hash += str(ord(character))
    for _, character in enumerate(str(draw_date)):
        bag_hash += str(ord(character))
    return bag_hash


class BloodTypes:

    def __init__(self, draw_date, donor_name):
        self.donor_name = donor_name
        self.draw_date = draw_date
        self.exp_date = draw_date + timedelta(days=21)
        self.id_num = hash_bag(self.donor_name, self.draw_date)
