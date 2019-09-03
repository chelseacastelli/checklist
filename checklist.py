import os
from subprocess import call
from colorama import Fore, Back, Style

checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[int(index)]

# UPDATE
def update(index, item):
    checklist[int(index)] = item

# DESTROY
def destroy(index):
    checklist.pop(int(index))

def item_exists(index):
    try:
        checklist[int(index)]
        return True
    except:
        return False

# PRINT ENTIRE LIST
def list_all_items():
    print('\n')
    # Output for empty list
    index = 0
    if item_exists(index):
        for list_item in checklist:
            item = color_text(list_item)
            print("{} {}".format(index, item))
            index += 1
    else:
        print("The list is empty")

def color_text(list_item):
    if list_item.upper() == "RED":
        return Fore.RED + list_item + Style.RESET_ALL
    elif list_item.upper() == "ORANGE":
        return Fore.ORANGE + list_item + Style.RESET_ALL
    elif list_item.upper() == "YELLOW":
        return Fore.YELLOW + list_item + Style.RESET_ALL
    elif list_item.upper() == "GREEN":
        return Fore.GREEN + list_item + Style.RESET_ALL
    elif list_item.upper() == "BLUE":
        return Fore.BLUE + list_item + Style.RESET_ALL
    elif list_item.upper() == "PURPLE":
        return Fore.MAGENTA + list_item + Style.RESET_ALL
    else:
        return Style.RESET_ALL + list_item + Style.RESET_ALL

def mark_complete(index):
    # Error handle (invalid user input)
    if item_exists(index):
        item = checklist[int(index)]
        checklist[int(index)] = u'\u2713' + ' ' + color_text(item)
    else:
        print("There is no item at this index\n")

def select(function_code):
    clear()
    # Create item
    if function_code == "A":
        input_item = user_input("Input item: ")
        create(input_item.upper())

    # Read item
    elif function_code == "R":
        list_all_items()
        item_index = user_input("\nIndex Number? ")
        # Remember that item_index must actually exist or our program will crash.
        if item_exists(item_index):
            destroy(item_index)
        else:
            print("There is no item at this index\n")

    # Update item
    elif function_code == "U":
        list_all_items()
        item_index = user_input("\nIndex Number? ")
        if item_exists(item_index):
            new_item_name = user_input("New item name: ")
            update(item_index, new_item_name.upper())
        else:
            print("There is no item at this index\n")

    # Mark complete
    elif function_code == "C":
        list_all_items()
        item_index = user_input("\nIndex Number? ")
        mark_complete(item_index)

    # List all items
    elif function_code == "S":
        list_all_items()

    # Quit
    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")
    print('\n')
    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def clear():
    _ = call('clear' if os.name =='posix' else 'cls')

# TEST
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))

    select("C")
    list_all_items()
    select("R")

    user_value = user_input("Please enter a value: ")
    print(user_value)

    list_all_items()

#test()

running = True
while running:
    selection = user_input("Press A to add to list, R to remove, U to update an item, C to mark an item complete, and S to show the list:\nPress Q to exit.\n")
    running = select(selection.upper())
