from coffee_maker import MENU, resources
import math


# TODO: 1. Print Report
def report():
    print(f"Water: {resources['water']}")
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')


# TODO: 4. Process payment
def check_payment():
    quarters = float(input('How many quarters? ')) * .25
    dimes = float(input('How many dimes? ')) * .10
    nickels = float(input('How many nickels? ')) * .05
    pennies = float(input('How many pennies? ')) * .01
    payment = quarters + dimes + nickels + pennies
    # print(payment)
    return payment


# TODO: 5. Check resources
def check_resources(drink_name):
    for ingredient in resources:
        resource_cost = MENU[drink_name]['ingredients'][ingredient]
        if resources[ingredient] < resource_cost:
            print(f'Sorry, there is not enough {ingredient}.')
            return False
        else:
            return True


# TODO: 3. Make the drink
def make_drink(prompt):
    for ingredient in resources:
        resource_cost = MENU[prompt]['ingredients'][ingredient]
        resources[ingredient] -= resource_cost
    print(f'Enjoy your {prompt}')


def coffee_machine():
    money = 0.0
    is_on = True
    while is_on:
        # TODO: 2. User Prompt
        drink_name = input('What would you like? (espresso/latte/cappuccino): ')
        if drink_name == 'report':
            report()
            print(f'${money:.2f}')
        elif drink_name == 'off':
            is_on = False
            print('Shutting down.')
        elif drink_name == 'espresso' or drink_name == 'latte' or drink_name == 'cappuccino':
            drink_cost = MENU[drink_name]['cost']
            if check_resources(drink_name):
                payment = check_payment()
                if payment >= drink_cost:
                    make_drink(drink_name)
                    money += drink_cost
                    print(f'Your change is ${payment - drink_cost:.2f}')
                else:
                    print('Insufficient funds. Money refunded.')
        else:
            print('Not an option.')
            continue


coffee_machine()
