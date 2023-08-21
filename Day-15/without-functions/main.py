"""
Day 15 - Coffee Machine Project
George - 100 Days Of Python Bootcamp
"""
from inventory import resources, MENU


# TODO: Make it a loop
def coffee_machine():
    # TODO 1: Ask the consumer: "What would you like? (espresso/latte/cappuccino): ".
    # consumer_coffee = "latte"
    consumer_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO 2: Print the resources when 'report' in the input.
    if consumer_coffee == "report":
        for key in resources:
            if key == "coffee":
                print(f"{key.capitalize()}: {resources[key]}mg")
            elif key == "money":
                print(f"{key.capitalize()}: ${resources[key]}")
            else:
                print(f"{key.capitalize()}: {resources[key]}ml")
        coffee_machine()
    elif consumer_coffee == "off":
        quit()
    # TODO 3: Check for the answer, if is valid pass, if not ask again.
    elif consumer_coffee != "espresso" and consumer_coffee != "latte" and consumer_coffee != "cappuccino":
        coffee_machine()
    else:
        # TODO 3.1: Check if there are enough resources before the transaction, if not return: "Sorry there is not
        #  enough { ingredient}."
        menu_ingredients = MENU[consumer_coffee]["ingredients"]
        for ingredient in menu_ingredients:
            if resources[ingredient] < menu_ingredients[ingredient]:
                print(f"Sorry there is not enough {ingredient}")
        else:
            # TODO 4: If the transaction can be made, ask for the money in quarters, dimes, nickles and pennies.
            #  Example: "How many {coin}?: "
            quarters = float(input("How many quarters?: ")) * 0.25
            dimes = float(input("How many dimes?: ")) * 0.10
            nickles = float(input("How many nickles?: ")) * 0.05
            pennies = float(input("How many pennies?: ")) * 0.01
            total_money = round(quarters + dimes + nickles + pennies, 2)
            if resources["money"] > total_money:
                # TODO 4.1: Check if there is enough money if not print: "Sorry that's not enough money. Money
                #  refunded."
                print("Sorry that's not enough money. Money refunded.")
            else:
                # TODO 4.2: if there is enough money check if the quantity surpass the price return he charge,
                #  example: "Here is $3.41 in charge."
                charge = total_money - resources["money"]
                print(f"Here is your charge: ${charge}")
                # TODO 4.2.1: Print the drink
                print(f"Here is your {consumer_coffee} ☕️. Enjoy!")
                # TODO 5: Deduct the resources
                for items in menu_ingredients:
                    resources[items] -= menu_ingredients[items]
                resources["money"] += MENU[consumer_coffee]["cost"]
                coffee_machine()


coffee_machine()
