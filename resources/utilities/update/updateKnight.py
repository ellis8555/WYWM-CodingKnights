from resources.classes.knight import Knight
from resources.userInput.createMultipleName import createMultipleName
from resources.utilities.display.displaySetOfNames import display_set_of_names
from resources.utilities.misc import objects_count as oc, zeroKnightsSelected, updateKnightsListOfNames
from resources.utilities.misc.booleans import is_name_duplicate
from resources.utilities.selections.mulitplesObjectsReturned import multiplesReturned
from resources.utilities.selections.singleObjectReturned import singleObjectReturned
from resources.utilities.update.updateHelpers import updateFromMultipleKnightsObjects


def update_a_Knight(objects_container):
    """
    method that narrows down entire master objects list into a single object
    where that objects name will be changed
    """

    # get count of how many knights have been created
    knight_count = oc.objects_counts(objects_container)

    # if at least one knight exists then display knights
    if knight_count > 0:

        # display menu option message
        print("-" * 20 + "Type the name of which knight who you will be updating?" + "-" * 20)

        # create a set of names for the user to choose from. duplicates are not
        # necessary to display
        knight_names_list = Knight.list_of_knights_names

        # display list of options, return users selection
        usersChoice = display_set_of_names(knight_names_list)

        # check if name is a duplicate
        is_user_choice_a_duplicate = is_name_duplicate.searchForDuplicates(usersChoice, knight_names_list)

        # if user selection is a name multiple knights share
        if is_user_choice_a_duplicate:

            # method handles if name returned multiple knights
            knights = multiplesReturned(usersChoice, objects_container)

            # custom message displays depending on inputs
            # this dictionary is submitted as an argument in following method
            message_inputs = {
                # first message that will be displayed
                "number_of_dashes_message_1": 30,
                "MESSAGE_1": "Multiple knights share that name",
                # second message that will be displayed
                "MESSAGE_2": "\nSelect which knight you are referring to..\n",
                "number_of_dashes_message_3": 36,
            }

            # get users input as to the new name user wants to assign
            print("\nEnter a new name..")
            knights_new_name = createMultipleName()

            # set knights new name
            previous_Knights_name = updateFromMultipleKnightsObjects.update_from_multiple_objects(
                knights, objects_container, message_inputs, knights_new_name)

            # update the list of knights names
            updateKnightsListOfNames.update_knights_list_of_names(previous_Knights_name, knights_new_name)

            # alert user object has been removed
            print(f"{previous_Knights_name} has been changed to {knights_new_name}")

        # else user selection is a name that's unique
        else:

            # get knights object
            knight = singleObjectReturned(usersChoice, objects_container)

            # get knights previous name for name change message
            previous_Knights_name = knight.get_name()

            # get users input as to the new name user wants to assign
            print("\nEnter a new name..")
            knights_new_name = createMultipleName()

            # update knights object
            knight.set_name(knights_new_name)

            # update the list of knights names
            updateKnightsListOfNames.update_knights_list_of_names(previous_Knights_name, knights_new_name)

            # alert user object has been removed
            print(f"{previous_Knights_name} has been changed to {knights_new_name}")

    # if no knights have been created
    else:
        zeroKnightsSelected.zero_knights_created()