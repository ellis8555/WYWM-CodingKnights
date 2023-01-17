from resources.utilities.create import createKnight
from resources.utilities.display import displayKnights
from resources.validations import numericWithRange


# method that checks for valid number and also falls within menus option range

def selectMenuOption(input_option: str, item_count: int):
    # object containing dual return values
    return_conditions = {"valid_input": True,
                         "exit_program": False,
                         }
    # test user input is valid
    validate_user_input = numericWithRange.numeric_with_range(
        input_option, item_count)
    if validate_user_input:
        if input_option == "1":
            createKnight.create_a_knight()
        elif input_option == "2":
            displayKnights.displayKnights()
        elif input_option == "0":
            return_conditions["exit_program"] = True
        return return_conditions
    else:
        print("Be sure to enter a corresponding menu item number. Try again.")
        return_conditions["valid_input"] = False
        return return_conditions
