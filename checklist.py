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
    # FROM UMARILL ON
    # https://discuss.codecademy.com/t/how-can-i-check-if-an-index-is-valid/377316/3
    if checkForItem(index):
        checklist.pop(int(index))
    else:
        print("There is no item at this index\n")

def checkForItem(index):
    try:
        checklist[int(index)]
        return True
    except:
        return False

# PRINT ENTIRE LIST
def list_all_items():
    # Output for empty list

    index = 0
    checkForItem(index)
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_complete(index):
    # Error handle (invalid user input)
    if checkForItem(index):
        checklist[int(index)] = u'\u2713' + ' ' + checklist[int(index)]
    else:
        print("There is no item at this index\n")

def select(function_code):
    # Create item
    if function_code == "A":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number? ")
        # Remember that item_index must actually exist or our program will crash.
        destroy(item_index)

    # Update item
    elif function_code == "U":
        item_index = user_input("Index Number? ")
        new_item_name = user_input("New item name: ")
        update(item_index, new_item_name)

    # Mark complete
    elif function_code == "C":
        item_index = user_input("Index Number? ")
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

    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

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
