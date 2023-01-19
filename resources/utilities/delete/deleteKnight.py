from resources.classes.knight import Knight
from resources.utilities.delete.deleteHelpers import delete_from_multiple_objects
from resources.utilities.delete.deleteHelpers.removeKnightsObject import remove_knights_object
from resources.utilities.display.displaySetOfNames import display_set_of_names
from resources.utilities.misc import objects_count as oc, zeroKnightsSelected
from resources.utilities.misc.booleans import is_name_duplicate
from resources.utilities.selections.mulitplesObjectsReturned import multiplesReturned
from resources.utilities.selections.singleObjectReturned import singleObjectReturned


def delete_a_knight(objects_container):

    # get count of how many knights have been created
    knight_count = oc.objects_counts(objects_container)

    # if at least one knight exists then display knights
    if knight_count > 0:

        # display menu option message
        print("-" * 20 + "Type the name of which knight who you will be removing?" + "-" * 20)

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

            delete_from_multiple_objects(knights, objects_container, message_inputs)
            Knight.list_of_knights_names.remove(usersChoice)

        # else user selection is a name that's unique
        else:

            # get knights object
            knight = singleObjectReturned(usersChoice, objects_container)

            # alert user object has been removed
            print(f"A moment of silence for {knight.get_name()}. {knight.get_name()} will be missed greatly!")

            # del knights object
            remove_knights_object(knight, objects_container)
            Knight.list_of_knights_names.remove(usersChoice)

    # if no knights have been created
    else:
        zeroKnightsSelected.zero_knights_created()