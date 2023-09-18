import json

AVAILABLE_DRINKS = ['espresso', 'cappuccino', 'latte']


def check_money_inserted(quarters, dimes, nickles, pennies, cost_of_drink):
    """
    Check if the money inserted into the machine is greater than or equal to the cost of coffee.
    """
    total_cash_deposited = (.25 * quarters) + (.1 * dimes) + (.05 * nickles) + (.01 * pennies)
    if total_cash_deposited < cost_of_drink:
        return False
    if total_cash_deposited == cost_of_drink:
        return True
    elif total_cash_deposited > cost_of_drink:
        change_amount = total_cash_deposited-cost_of_drink
        print(f"Here is your ${change_amount} in change.")
        return True


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


def get_drink_cost(selected_drink):
    """
    Return the cost of the drink selected by the user.
    """
    data = open_json("data.json")
    drink_cost = data['recipes'][selected_drink]['money']
    return drink_cost


def open_json(file_name):
    """
    Helper function that opens up specified json file
    """
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data


def request_money(selected_drink):
    """
    Ask the user to input money.
    """
    drink_cost = get_drink_cost(selected_drink)
    enough_money = False

    print("Please insert coins.")
    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    nickles = int(input("how many nickles? "))
    pennies = int(input("how many pennies? "))

    enough_money = check_money_inserted(quarters, dimes, nickles, pennies, drink_cost)

    if not enough_money:
        print("Sorry, that's not enough money. Money refunded.")
    elif enough_money:
        print(f"Here is your {selected_drink}. Enjoy!")


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
    user_request = request_user_selection().lower()

    while user_request != 'off':
        if user_request == 'report':
            generate_report()
        if user_request in AVAILABLE_DRINKS:
            enough_resources = check_resources(user_request)
            if not enough_resources:
                user_request = request_user_selection()
                continue
            request_money(selected_drink=user_request)
            update_report(selected_drink=user_request)
        user_request = request_user_selection()


def update_report(selected_drink):
    data = open_json('data.json')

    drink_cost = data['recipes'][selected_drink]['money']
    drink_coffee_amount = data['recipes'][selected_drink]['coffee']
    drink_milk_amount = data['recipes'][selected_drink]['milk']
    drink_water_amount = data['recipes'][selected_drink]['water']

    data['resources']['water'] = data['resources']['water'] - drink_water_amount
    data['resources']['money'] = data['resources']['money'] - drink_cost
    data['resources']['coffee'] = data['resources']['coffee'] - drink_coffee_amount
    data['resources']['milk'] = data['resources']['milk'] - drink_milk_amount
    write_json(data)


def write_json(data):
    """
    Updates the json file with new values
    """
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
