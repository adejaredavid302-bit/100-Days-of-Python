from game_data import *

def is_resource_sufficient(order_ingredient ):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"sorry, you don't have enough {item}")
            return False
    return True
def calculate_coins():
    """Returns the total amount of coins available"""
    print("Please insert coin")
    total=int(input("how many quarters?"))*0.25
    total+= int(input("how many dimes?"))*0.1
    total+= int(input("how many nickels?"))*0.05
    total+= int(input("how many pennies?"))*0.10
    return total
def is_transaction_complete(money_received,drink_cost):
    """Checks if money_received is complete for drink_cost"""
    if money_received >= drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is your change ${change}")
        global profit
        profit+=drink_cost
        return True
    else:
        print("sorry, you don't have enough money,Money refunded")
        return False
def make_coffe(drink_name,order_ingredient):
    """Makes coffe and show available resources"""
    for item in order_ingredient:
        resources[item]-=order_ingredient[item]
    print(f"Here is your coffe {drink_name}")


is_on = True
profit=0
while is_on:
    choice = input("What would you like?(espresso/latte/cappuccino:").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{resources['water']}")
        print(f"milk:{resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"money:${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=calculate_coins()
            if is_transaction_complete(payment,drink["cost"]):
                make_coffe(choice,drink["ingredients"])

