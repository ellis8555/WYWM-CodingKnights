from resources.classes import knight
from resources.utilities.misc import zeroKnightsSelected


def display_single_knight():

    # display menu option message
    print("-" * 20 + "Choose a knight from the list" + "-" * 20)

    # get a count of how many knights have been created
    knight_count = len(knight.Knight.dict_of_knight_objects)

    if knight_count > 0:
        print("you have knights")
    else:
        zeroKnightsSelected.zero_knights_created()
