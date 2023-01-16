from resources.classes.knight import Knight
from resources.utilities.display import displayMenu as dm
from resources.utilities.selections import selectMenuOption as smo


def run():
    # display option menu. returns how many menu options there are. dm alias import
    how_many_menu_items = dm.displayMenu()
    # get user selection.
    user_selection = input("Enter a selection..")
    # validate user input is within range of menu item count. smo is alias import
    isValid = smo.selectMenuOption(user_selection, how_many_menu_items)
    # if user enters an invalid selection try again
    while not isValid:
        dm.displayMenu()
        user_selection = input("Enter a selection..")
        isValid = smo.selectMenuOption(user_selection, how_many_menu_items)

    ###################
    # just for testing
    ###################

    print(Knight.list_of_knights_names)
