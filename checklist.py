checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[int(index)]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

# PRINT ENTIRE LIST
def list_all_items():
    # Output for empty list
    if not checklist:
        print("List is empty")

    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

#def mark_completed(index):


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

    elif function_code == "U":
        item_index = user_input("Index Number? ")
        new_item_name = user_input("New item name: ")
        update(item_index, new_item_name)

    # Print all items
    elif function_code == "S":
        list_all_items()

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

    user_value = user_input("Please Enter a value: ")
    print(user_value)

    list_all_items()

#test()

running = True
while running:
    selection = user_input("Press A to add to list, R to remove, U to update an item, C to mark an item complete, and S to show the list:\nPress Q to exit.\n")
    running = select(selection)
