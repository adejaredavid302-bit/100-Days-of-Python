from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on=True
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()

is_on=True

while is_on:
    option=menu.get_items()
    choice=input(f"What do you want to do?{option}:").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


