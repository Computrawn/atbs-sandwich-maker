# Python3
# sandwichMaker.py — An exercise in using PyInputPlus module to validate user input.

import pyinputplus as pyip

def sandwich_maker(name):
    print(f"Hello {name}, and welcome to the Sandwich Maker.")
    # bread selection
    print(f"First off, let's pick the foundation of your sandwich.")
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'])
    # protein selection
    print(f"Let's get to the meat of things. Which protein strikes your fancy?")
    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
    # cheese selection
    print(f"Do you want cheese on your sandwich?")
    cheese = pyip.inputYesNo()
    if cheese == 'yes':
        cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
    else:
        pass
    # toppings selection
    print(f"Would you like mayo?")
    mayo = pyip.inputYesNo()
    print("How about mustard?")
    mustard = pyip.inputYesNo()
    print("Are you in the mood for lettuce?")
    lettuce = pyip.inputYesNo()
    print("Finally, would you like to add tomatoes?")
    tomatoes = pyip.inputYesNo()
    print(f"How many of this type of sandwich would you like?")
    number = pyip.inputInt(min=1)
    print(f"OK. I have {number} {protein} on {bread} with:")
    if cheese == 'yes':
        print(cheese_type)
    if mayo == 'yes':
        print('mayo')
    if mustard == 'yes':
        print('mustard')
    if lettuce == 'yes':
        print('lettuce')
    if tomatoes == 'yes':
        print('tomatoes')

user_name = pyip.inputStr('Please enter a user name: ')
sandwich_maker(user_name)