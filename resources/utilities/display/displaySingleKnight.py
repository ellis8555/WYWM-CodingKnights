from resources.classes.knight import Knight
from resources.userInput.createMultipleName import createMultipleName
from resources.utilities.misc import zeroKnightsSelected
from resources.utilities.misc.check_if_name_exists import check_if_name_exists
from resources.utilities.selections.mulitplesObjectsReturned import multiplesReturned


def display_single_knight():
    # get Knights class dictionary of knight objects
    knights = Knight.dict_of_knight_objects

    # get a count of how many knights have been created
    knight_count = len(knights)

    # if at least one knight exists then display knights
    if knight_count > 0:

        # display menu option message
        print("-" * 20 + "Type the name of which knight would you like to see?" + "-" * 20)

        # create a set of names for the user to choose from. duplicates are not
        # necessary to display
        knight_names = set(Knight.list_of_knights_names)

        # display the set of names
        for name in knight_names:
            print("- " + name)

        # get users selection and put into variable
        usersChoice = createMultipleName()

        # check if users choice is a name that a knight has
        does_name_exist = check_if_name_exists(usersChoice, knight_names)

        # if user input name hasn't been created previously
        # get the user to enter another name
        while not does_name_exist:
            print("\nThat name does not appear to be from the list displayed..")
            print("Try again\n")
            usersChoice = createMultipleName()
            does_name_exist = check_if_name_exists(usersChoice, knight_names)

        # initialize a list that matching knight objects will be appended to
        knights_list = []

        # filter through knights objects and find matching objects with name match
        # from users input choice
        for knights_id, knights_object in knights.items():
            knights_name = knights_object.get_name()
            if knights_name == usersChoice:
                knights_list.append(knights_object)

        # get count of object to see if user selected a name
        # that returns multiple results
        selected_knights_count = len(knights_list)

        # if some knights share the same name
        if selected_knights_count > 1:

            # method handles if name returned multiple knights
            multiplesReturned(selected_knights_count, knights_list)

        # else only a single knight has that name
        else:
            selected_knight = knights_list[0]
            selected_knight_name = selected_knight.get_name()
            selected_knight_id = selected_knight.get_id()
            print(f"name: {selected_knight_name} - id: {selected_knight_id}")

        # end dividing dash line
        print("-" * 92)
    else:
        zeroKnightsSelected.zero_knights_created()
