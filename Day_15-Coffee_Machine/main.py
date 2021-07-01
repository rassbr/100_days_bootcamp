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
    "money": 10.0,
}

def invalid_input(questions):
    print('Invalid answer!')
    print(questions)
    return input()

def insert_coins():
    """Returns the total value of the coins inserted"""
    coins = ['quarters', 'dimes', 'nickles', 'pennies']
    my_dict = dict.fromkeys(coins,None)
    for i in coins:
        questions = 'how many ' + i + '? - '
        print(questions)
        ans = input()
        while not ans.isalnum():
            ans = invalid_input(questions)
        my_dict[i] = int(ans)
    my_sum = my_dict['quarters']*0.25 + my_dict['dimes']*.1 + my_dict['nickles']*.05 + my_dict['pennies']*.01
    return round(my_sum,2)


def check_resources(drink):
    """Returns True if there are enough resources, else it returns False"""
    ingredients = MENU[drink]['ingredients']
    ings = ingredients.keys()
    for i in ings:
        if resources[i] < ingredients[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def deduct_resources(drink):
    """Executes the trade money for coffee."""
    ingredients = MENU[drink]['ingredients']
    ings = ingredients.keys()
    for i in ings:
        resources[i] = resources[i] - ingredients[i]
    resources["money"] = resources["money"] + MENU[drink]['cost']
    return

def coffee_machine():
    print('What would you like? (espresso/latte/cappuccino):')
    ans = input()

    question = "Please choose one of the options - espresso/latte/cappuccino:"
    while ans != "espresso" and ans != 'latte' and ans != 'cappuccino' and ans != 'report' and ans != 'off':
        ans = invalid_input(question)
        print(ans)

    if ans == 'report':
        print("Water: " + str(resources['water'])+'ml')
        print('Milk: ' + str(resources['milk'])+'ml')
        print('Coffee: ' + str(resources['coffee'])+'g')
        print('Money: $' + str(resources['money']))
    elif ans == 'off':
        return True
    else:
        if check_resources(ans) != True:
            return
        else:
            price = MENU[ans]['cost']
            paid = insert_coins()
            if paid > price:
                change = paid - price
                print(f"Here is your ${change} in change")
            elif paid == price:
                pass
            else:
                print(f"Sorry your selected coffee costs ${price}, so ${paid} is not enough money. Money refunded")
                return
            deduct_resources(ans)
            print(f"Here is your {ans}. Enjoy!")
            return


stop = False
while not stop == True:
    stop = coffee_machine()