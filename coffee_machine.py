def check_resources(resources):
    pass

def generate_report(resources):
    """
    Generate a report of the shows current resource values.
    """
    for item in resources:
        print(f"Water: {item['water']}ml")
        print(f"Milk: {item['milk']}ml")
        print(f"Coffee: {item['coffee']}g")
        print(f"Money: ${round(item['money'], 2)}")
    

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
    resources = {
        "water": 500,
        "milk": 500,
        "coffee": 500,
        "money": 500.0
    }

    user_request = request_user_selection()
    while user_request != 'off':
        if user_request == 'request':
            pass
        print(f"test + {index}")
        index += 1

        user_request = request_user_selection()
        