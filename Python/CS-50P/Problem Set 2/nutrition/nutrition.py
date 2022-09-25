def main():
    # File I/O wouldn't work with check50; pain :(
    fruit_dict = {'apple': '130', 'avocado': '50', 'banana': '110', 'cantaloupe': '50', 'grapefruit': '60', 'grapes': '90', 'honeydew melon': '50', 'kiwifruit': '90', 'lemon': '15', 'lime': '20', 'nectarine': '60', 'orange': '80', 'peach': '60', 'pear': '100', 'pineapple': '50', 'plums': '70', 'strawberries': '50', 'sweet cherries': '100', 'tangerine': '50', 'watermelon': '80'}

    user_input = input("Item: ")
    user_input = user_input.lower()

    if user_input in fruit_dict.keys():
        print(f"Calories: {fruit_dict.get(user_input)}")
    else:
        return


def load_fruit():
    fruit_dict = {}
    with open("raw_fruits.txt", "r") as fruit_file:
        fruit_line = fruit_file.readline()
        while fruit_line:
            name, calories = fruit_line.split(",")
            name = name.lower()
            calories = calories.replace("\n", "")
            fruit_dict.update({name: calories})
            fruit_line = fruit_file.readline()
    return fruit_dict

main()