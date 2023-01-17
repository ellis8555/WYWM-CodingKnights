from resources.utilities.display import displayMenu as dm
from resources.utilities.selections import selectMenuOption as smo


def run():

    # display option menu and returns how many menu options there are. dm alias import
    how_many_menu_items = dm.displayMenu()

    # get user selection.
    user_selection = input("Enter a selection..")

    # dict returned with two conditional bools. 1 valid input 2. program exit or not
    # smo is alias import
    selection_conditions = smo.selectMenuOption(user_selection, how_many_menu_items)

    # get condition that checked if input is valid
    isValid = selection_conditions.get("valid_input")

    # if user enters an invalid selection try again
    while not isValid:
        dm.displayMenu()
        user_selection = input("Enter a selection..")
        selection_conditions = smo.selectMenuOption(user_selection, how_many_menu_items)
        # get condition that checked if input is valid
        isValid = selection_conditions.get("valid_input")

    # get if user wants to exit the program
    exit_program = selection_conditions.get("exit_program")

    # return the result if user wants to continue
    return exit_program
