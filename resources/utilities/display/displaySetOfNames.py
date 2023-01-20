from resources.userInput.createMultipleName import createMultipleName
from resources.utilities.misc.booleans.check_if_name_exists import check_if_name_exists


def display_set_of_names(list_of_names: list):
    """
    method that removes duplicates from master names list and produces a set to be displayed
    """

    knight_names_set = set(list_of_names)

    # display the set of names
    for name in knight_names_set:
        print("- " + name)

        # get users selection and put into variable
    usersChoice = createMultipleName()

    # check if users choice is a name that a knight has
    does_name_exist = check_if_name_exists(usersChoice, knight_names_set)

    # if user input name hasn't been created previously
    # get the user to enter another name
    while not does_name_exist:
        print("\nThat name does not appear to be from the list displayed..")
        print("Try again\n")
        usersChoice = createMultipleName()
        does_name_exist = check_if_name_exists(usersChoice, knight_names_set)

    return usersChoice