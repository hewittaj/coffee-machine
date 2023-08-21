import json


def check_resources():
    """
    Check the available resources in the coffee machine.
    """
    available_resources = json.load("data.json")
    print(available_resources)
    pass


def generate_report():
    """
    Generate a report of the shows current resource values.
    """
    available_resources = open_json('data.json')['resources']

    print(f"Water: {available_resources['water']}ml")
    print(f"Milk: {available_resources['milk']}ml")
    print(f"Coffee: {available_resources['coffee']}g")
    print(f"Money: $%.2f" % round(available_resources['money_in_machine'], 2))


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
    # Variable declarations
    index = 0
    user_request = request_user_selection()
    while user_request != 'off':
        if user_request == 'report':
            generate_report()
        print(f"test + {index}")
        index += 1

        user_request = request_user_selection()
        