# Python3
# sandwichMaker.py — An exercise in using PyInputPlus library to validate user input.

import pyinputplus as pyip


def sandwich_maker():
    user_name = pyip.inputStr('Please enter a user name: ')
    print(f"Hello, {user_name}. Welcome to the Sandwich Maker.")
    # bread selection
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], "Let's pick the foundation of your sandwich.\n")
    if bread != 'sourdough':
        bread_price = 1.5
    else:
        bread_price = 2
    # protein selection
    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], "Let's get to the meat of things. Which protein "
                                                                   "strikes your fancy?\n")
    if protein == 'chicken':
        protein_price = 3.00
    elif protein == 'turkey':
        protein_price = 3.25
    elif protein == 'ham':
        protein_price = 3.50
    else:
        protein_price = 2.75
    # cheese selection
    cheese = pyip.inputYesNo("Do you want cheese on your sandwich?\n")
    if cheese == 'yes':
        cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
    # toppings selection
    mayo = pyip.inputYesNo("Would you like mayo? ")
    mustard = pyip.inputYesNo("How about mustard? ")
    lettuce = pyip.inputYesNo("Are you in the mood for lettuce? ")
    tomatoes = pyip.inputYesNo("And tomatoes? ")
    # Amount selection
    number = pyip.inputInt("How many of this type of sandwich would you like? ", min=1)
    print(f"OK. I have {number} {protein} (${protein_price:.2f}) on {bread} (${bread_price:.2f}) with:")
    if cheese == 'yes':
        cheese_price = 1.50
        print(f'{cheese_type} (${cheese_price:.2f})')
    else:
        cheese_price = 0
    if mayo == 'yes':
        mayo_price = .25
        print(f'mayo (${mayo_price:.2f})')
    else:
        mayo_price = 0
    if mustard == 'yes':
        mustard_price = .25
        print(f'mustard (${mustard_price:.2f})')
    else:
        mustard_price = 0
    if lettuce == 'yes':
        lettuce_price = .50
        print(f'lettuce (${lettuce_price:.2f})')
    else:
        lettuce_price = 0
    if tomatoes == 'yes':
        tomato_price = .75
        print(f'tomatoes (${tomato_price:.2f})')
    else:
        tomato_price = 0
    sandwich_cost = bread_price + protein_price + cheese_price + mayo_price + \
                    mustard_price + lettuce_price + tomato_price
    total = number * sandwich_cost
    print(f"Your total will be: ${total:.2f}.")
    order_confirmation = pyip.inputYesNo("Does this order look correct? ")
    if order_confirmation == 'yes':
        print(f"Order processed. Thank you for your business, {user_name}.")
    else:
        print(f"We're sorry, {user_name}. Unable to process order.")


sandwich_maker()
