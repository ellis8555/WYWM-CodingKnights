# tuple of menu items to be displayed via iterator
menu_items = ("1. Create a knight", "2. Display all knights", "3. Display a knight", "4. Remove a knight", "0. Quit")


def displayMenu():
    # display menu items
    print()
    for item in menu_items:
        print(item)
    # return length of menu to be used as max user entry for menu selection
    return len(menu_items)
