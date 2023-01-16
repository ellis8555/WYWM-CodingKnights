# tuple of menu items to be displayed via iterator
menu_items = ("1. Create a knight",)


def displayMenu():
    # display menu items
    for item in menu_items:
        print(item)
    # return length of menu to be used as max user entry for menu selection
    return len(menu_items)
