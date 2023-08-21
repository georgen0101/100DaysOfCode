from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    user_choice = input(f"What would you like? ({menu.get_items()}): ")
    # Exit gate for the maintenance employee
    if user_choice == "off":
        is_on = False
    # Report for the maintenance employee
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    # Check if the user typed a valid coffee
    else:
        # Save the MenuItem object "Order"
        drink = menu.find_drink(user_choice)
        if not drink:
            pass
        else:
            # Check if there is sufficient ingredients in the resources and if the payment amount is enough
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                # Make the coffee, deduct the ingredients and the money
                coffee_maker.make_coffee(menu.find_drink(user_choice))
