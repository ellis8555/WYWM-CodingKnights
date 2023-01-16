from resources.utilities.create import createKnight
from resources.validations import numericWithRange


# method that checks for valid number and also falls within menus option range

# string, integer
def selectMenuOption(input_option, item_count):
    # test user input is valid
    validate_user_input = numericWithRange.numeric_with_range(
        input_option, item_count)
    if validate_user_input:
        createKnight.create_a_knight()
        return True
    else:
        print("Be sure to enter a corresponding menu item number. Try again.")
        return False

