from data import MENU , profit , resources , logo
import sys

def exit_program():
    print("Turning off the coffee machine")
    sys.exit(0)

def report():
    """Will return the ingredients left in the vending machine"""
    water_left = resources["water"]
    milk_left = resources["milk"]
    coffee_left = resources["coffee"]
    return f"The machine has {water_left} ml water left , {coffee_left} ml coffee left , {milk_left} ml left."

def check(drink_name):
    '''will return true if all the ingredients required for the requested drink is present in the machine'''
    ingredients_required = MENU[drink_name]["ingredients"]
    for i in ingredients_required:
        if (ingredients_required[i]) > resources[i]:
            (f"Not enough ingredients. Low on {i}")
            return False
        else:
            return True

def update_menu(drink_name):
    '''updates the menu dictionary once the ingredients used for a drink'''
    ingredients_used = MENU[drink_name]["ingredients"]
    #ingredients_present = resources[]
    for i in ingredients_used:
        new_menu_value = resources[i] - ingredients_used[i]
        resources[i] = new_menu_value

def change(drink_name , total):
    '''returns change if inserted amount greater than required'''
    change_to_give = total - MENU[drink_name]["cost"]
    return round(change_to_give , 2)
              
def encash(drink_name):
    '''Calculates the total amount inserted'''
    drink_ordered = drink_name
    quarters = float(input("Inserting these many quarters: "))
    dimes = float(input("Inserting these many dimes: "))
    nickels = float(input("Inserting these many nickels: "))
    pennies = float(input("Inserting these many pennies: "))

    total_amount = 0.25*quarters + 0.10*dimes + 0.05*nickels + 0.01*pennies
    print(total_amount)
    if total_amount >= MENU[drink_name]["cost"]:
        print(change(drink_ordered , total_amount))
        return True
    else:
        print("Not enough money")
        return False
    


print(logo)

vending_machine_on = True

while vending_machine_on:
    user_choice = input("What would you like? (latte/espresso/cappuccino) ").lower()

    if user_choice == "off":
        exit_program()
    elif user_choice == "latte" and check("latte"):
            if encash("latte"):
                print("Made Latte!!")
            update_menu("latte")  
    elif user_choice == "espresso" and check("espresso"):
            if encash("espresso"):
                print("Made Espresso!!")
            update_menu("espresso")  
    elif user_choice == "cappuccino" and check("cappuccino"):
            if encash("cappuccino"):
                print("Made Cappuccino!!")        
            update_menu("cappuccino")  
    elif user_choice == "report":
        print(report())

