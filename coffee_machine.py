import json

AVAILABLE_DRINKS = ['espresso', 'cappuccino', 'latte']


def check_resources(drink_selected):
    """
    Check the available resources in the coffee machine.
    """
    # Variable declarations
    data = open_json("data.json")
    available_resources = data['resources']
    recipes = data['recipes']

    for item in available_resources:
        if available_resources[item] < recipes[drink_selected][item]:
            print(f"Sorry, there is not enough {item}.")
            return False
        elif available_resources[item] == 0:
            print(f"Sorry, there is not enough {item}.")
            return False

    return True


def generate_report():
    """
    Generate a report of the shows current resource values.
    """
    available_resources = open_json('data.json')['resources']

    print(f"Water: {available_resources['water']}ml")
    print(f"Milk: {available_resources['milk']}ml")
    print(f"Coffee: {available_resources['coffee']}g")
    print(f"Money: $%.2f" % round(available_resources['money'], 2))


def open_json(file_name):
    """
    Helper function that opens up specified json file
    """
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data


def request_user_selection():
    """
    Asks the user what they would like to drink.
    """
    return input("What would you like to drink? (espresso/latte/cappuccino): ")


def run_coffee_machine():
    """
    Main code block to run coffee machine.
    """
    # Variable declarations\
    enough_resources = True
    index = 0
    user_request = request_user_selection().lower()

    while user_request != 'off':
        if user_request == 'report':
            generate_report()
        if user_request in AVAILABLE_DRINKS:
            enough_resources = check_resources(user_request)
        print(enough_resources)
        print(f"test + {index}")
        index += 1

        user_request = request_user_selection()
        