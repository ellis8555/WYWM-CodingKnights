# tuple of menu items to be displayed via iterator
menu_items = ("1. Create a knight", "2. Display all knights", "3. Display a knight",
              "4. Remove a knight", "5. Update a knights name", "0. Quit")


def displayMenu():
    """
    method that plays a role in displaying the programs main menu from the list above
    """
    # display menu items
    print()
    for item in menu_items:
        print(item)
    # return length of menu to be used as max user entry for menu selection
    return len(menu_items)
