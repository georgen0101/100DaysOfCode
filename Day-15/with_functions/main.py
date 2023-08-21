"""
100 Days Of Python - Coffee Machine With Functions
George
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def resources_report(dictionary):
    for key in dictionary:
        if key == "water" or key == "milk":
            print(f"{key.capitalize()}: {dictionary[key]}ml")
        elif key == "coffee":
            print(f"{key.capitalize()}: {dictionary[key]}g")
        else:
            print(f"{key.capitalize()}: ${dictionary[key]}")


def sufficient_resources(resources_dictionary, menu_dictionary, choice):
    menu_ingredients = menu_dictionary[choice]["ingredients"]
    for ingredient in menu_ingredients:
        if menu_ingredients[ingredient] > resources_dictionary[ingredient]:
            print(f"There is not enough {ingredient}")
            return False
        return True


def process_coins():
    print("Insert the coins: ")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    total_money = quarters + dimes + nickles + pennies
    return total_money


def transaction_successful(total, menu_dictionary, choice):
    if total < menu_dictionary[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is {round(total - menu_dictionary[choice]['cost'], 2)} dollars in change.")
        return True


def make_coffee(resources_dictionary, menu_dictionary, choice):
    # Add money
    resources_dictionary["money"] += menu_dictionary[choice]["cost"]
    # Deduct the resources
    menu_ingredients = menu_dictionary[choice]["ingredients"]
    for ingredient in menu_ingredients:
        resources_dictionary[ingredient] -= menu_ingredients[ingredient]


# TODO 1: Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # user_choice = "report"

    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == "off":
        is_on = False

    # TODO 3: Print report.
    elif user_choice == "report":
        resources_report(resources)

    # TODO 4: Check if the resources are sufficient.
    elif user_choice == "latte" or user_choice == "espresso" or user_choice == "cappuccino":
        if sufficient_resources(resources_dictionary=resources, menu_dictionary=MENU, choice=user_choice):
            # TODO 5: Process coins.
            if transaction_successful(total=process_coins(), menu_dictionary=MENU, choice=user_choice):
                make_coffee(resources_dictionary=resources, menu_dictionary=MENU, choice=user_choice)
                print(f"Here is your {user_choice} ☕️. Enjoy")
    else:
        print("Error! Invalid option")
